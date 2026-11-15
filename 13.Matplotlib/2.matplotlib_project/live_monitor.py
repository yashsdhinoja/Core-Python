"""Real-time monitor: live-updating charts with FuncAnimation.

Two data sources share the same interface (.read() -> dict):
  * SimulatedStream - works everywhere, includes random CPU spikes
  * RealStream      - real CPU / RAM / network of YOUR machine (needs psutil)
"""
import time
from collections import deque

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class SimulatedStream:
    def __init__(self, seed=None):
        self.rng = np.random.default_rng(seed)
        self.cpu, self.mem = 35.0, 55.0

    def read(self):
        self.cpu += 0.15 * (35 - self.cpu) + self.rng.normal(0, 6)
        if self.rng.random() < 0.06:  # random traffic spike
            self.cpu += self.rng.uniform(30, 50)
        self.cpu = float(np.clip(self.cpu, 2, 100))
        self.mem = float(np.clip(self.mem + 0.05 * (55 - self.mem) + self.rng.normal(0, 0.8), 5, 100))
        net = float(abs(self.rng.normal(400, 150)) + self.cpu * 5)
        return {"cpu": self.cpu, "mem": self.mem, "net": net}


class RealStream:
    def __init__(self):
        import psutil  # imported here so the simulated mode needs no extra install

        self.ps = psutil
        self.ps.cpu_percent(None)
        self._last = self.ps.net_io_counters()
        self._t = time.time()

    def read(self):
        now, net = time.time(), self.ps.net_io_counters()
        dt = max(now - self._t, 1e-6)
        moved = (net.bytes_sent + net.bytes_recv) - (self._last.bytes_sent + self._last.bytes_recv)
        self._last, self._t = net, now
        return {
            "cpu": self.ps.cpu_percent(None),
            "mem": self.ps.virtual_memory().percent,
            "net": moved / 1024 / dt,
        }


class LiveMonitor:
    def __init__(self, stream, window_s=30, interval_ms=500, cpu_alert=80):
        self.stream = stream
        self.interval_ms = interval_ms
        self.window_s = window_s
        self.cpu_alert = cpu_alert
        n = int(window_s * 1000 / interval_ms) + 5
        self.t = deque(maxlen=n)
        self.buf = {k: deque(maxlen=n) for k in ("cpu", "mem", "net")}
        self.alerts = 0
        self.paused = False
        self._tick = 0
        self._fill = None

        self.fig, (self.ax_cpu, self.ax_mem, self.ax_net) = plt.subplots(
            3, 1, figsize=(11, 8), sharex=True, constrained_layout=True
        )
        self.fig.suptitle("Live System Monitor", fontsize=16, weight="bold")
        (self.l_cpu,) = self.ax_cpu.plot([], [], color="#4C72B0", lw=2)
        (self.l_mem,) = self.ax_mem.plot([], [], color="#55A868", lw=2)
        (self.l_net,) = self.ax_net.plot([], [], color="#DD8452", lw=2)

        self.ax_cpu.set_ylim(0, 105)
        self.ax_cpu.axhline(cpu_alert, color="#C44E52", ls="--", lw=1.2)
        self.ax_cpu.text(0.01, cpu_alert + 2, f"alert > {cpu_alert}%", transform=self.ax_cpu.get_yaxis_transform(),
                         color="#C44E52", fontsize=9)
        self.ax_mem.set_ylim(0, 105)
        self.ax_net.set_xlabel("seconds since start   (SPACE = pause / resume)")
        for ax, title in ((self.ax_cpu, "CPU %"), (self.ax_mem, "Memory %"), (self.ax_net, "Network KB/s")):
            ax.set_title(title, loc="left", fontweight="bold")
            ax.grid(alpha=0.3)
        self.value_txt = {
            k: ax.text(0.99, 0.85, "", transform=ax.transAxes, ha="right", fontsize=14, weight="bold")
            for k, ax in (("cpu", self.ax_cpu), ("mem", self.ax_mem), ("net", self.ax_net))
        }
        self.status = self.fig.text(0.01, 0.005, "", fontsize=10, color="#C44E52")
        self.fig.canvas.mpl_connect("key_press_event", self._on_key)

    def _on_key(self, event):
        if event.key == " ":
            self.paused = not self.paused
            (self.anim.pause if self.paused else self.anim.resume)()

    def _update(self, _frame):
        reading = self.stream.read()
        self.t.append(self._tick * self.interval_ms / 1000)
        self._tick += 1
        for k, v in reading.items():
            self.buf[k].append(v)
        x = np.array(self.t)
        cpu = np.array(self.buf["cpu"])

        for line, key in ((self.l_cpu, "cpu"), (self.l_mem, "mem"), (self.l_net, "net")):
            line.set_data(x, self.buf[key])
        self.ax_cpu.set_xlim(max(0, x[-1] - self.window_s), max(self.window_s, x[-1]))
        self.ax_net.set_ylim(0, max(100, max(self.buf["net"]) * 1.2))

        # shade the danger zone (remove last frame's shading first)
        if self._fill is not None:
            self._fill.remove()
        self._fill = self.ax_cpu.fill_between(x, 0, cpu, where=cpu > self.cpu_alert, color="#C44E52", alpha=0.3)

        if cpu[-1] > self.cpu_alert:
            self.alerts += 1
        self.value_txt["cpu"].set_text(f"{cpu[-1]:.0f}%")
        self.value_txt["cpu"].set_color("#C44E52" if cpu[-1] > self.cpu_alert else "black")
        self.value_txt["mem"].set_text(f"{self.buf['mem'][-1]:.0f}%")
        self.value_txt["net"].set_text(f"{self.buf['net'][-1]:.0f} KB/s")
        self.status.set_text(f"High-CPU samples so far: {self.alerts}" if self.alerts else "")
        return self.l_cpu, self.l_mem, self.l_net

    def run(self):
        self.anim = FuncAnimation(self.fig, self._update, interval=self.interval_ms, cache_frame_data=False)
        plt.show()
