"""02 - Markers: marker, ms (size), mec (edge color), mfc (face color), format strings"""
import matplotlib.pyplot as plt
import numpy as np

from utils import save_and_show

# ---------- Figure 1: marker gallery ----------
markers = ["o", "*", ".", ",", "x", "X", "+", "P", "s", "D", "d", "p",
           "H", "h", "v", "^", "<", ">", "1", "2", "3", "4", "|", "_"]

plt.figure(figsize=(11, 5))
for i, m in enumerate(markers):
    col, row = i % 8, 2 - i // 8                     # 8 markers per row, 3 rows
    plt.plot(col, row, marker=m, ms=16, color="darkorange", mec="black", mfc="gold", linestyle="none")
    plt.text(col, row - 0.3, f"'{m}'", ha="center", fontsize=11)
plt.xlim(-0.7, 7.7)
plt.ylim(-0.7, 2.6)
plt.title("Matplotlib marker gallery", fontsize=16, fontweight="bold")
plt.xticks(np.arange(8), [""] * 8)       # ticks without labels so the grid still shows
plt.yticks(np.arange(3), [""] * 3)
plt.grid(True, alpha=0.3)
save_and_show("02a_marker_gallery.png")

# ---------- Figure 2: daily steps tracker with markers ----------
days = np.arange(1, 8)
day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
amit = np.array([6500, 8200, 7400, 10200, 9100, 12500, 5400])
riya = np.array([9000, 9800, 10500, 8700, 11200, 13800, 9900])

plt.figure(figsize=(10, 5))
# 'o-' = circle marker + solid line  |  's--' = square marker + dashed line
plt.plot(days, amit, "o-", color="royalblue", ms=11, mec="navy", mfc="lightskyblue", label="Amit")
plt.plot(days, riya, "s--", color="crimson", ms=11, mec="darkred", mfc="salmon", label="Riya")

plt.axhline(10000, color="green", linestyle=":", linewidth=2, label="Goal: 10,000 steps")
best = np.argmax(riya)                                      # numpy: index of the best day
plt.plot(days[best], riya[best], "*", ms=26, color="gold", mec="black", label=f"Best day: {day_names[best]}")

plt.xticks(days, day_names)
plt.title("Weekly Steps Tracker", fontsize=16, fontweight="bold")
plt.xlabel("Day of week")
plt.ylabel("Steps")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="lower right")
save_and_show("02b_steps_tracker.png")
