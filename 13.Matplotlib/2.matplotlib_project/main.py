"""Matplotlib project entry point.

  python main.py dashboard            # static dashboard (shows window + saves PNG)
  python main.py dashboard --no-show  # only save output/dashboard.png
  python main.py live                 # live monitor with simulated data
  python main.py live --source real   # live monitor with your real CPU/RAM (pip install psutil)
"""
import argparse
from pathlib import Path

from data import generate_sales_data

OUT = Path(__file__).parent / "output"


def main():
    p = argparse.ArgumentParser(description="Matplotlib real-world project")
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("dashboard", help="static sales analytics dashboard")
    d.add_argument("--orders", type=int, default=6000, help="number of synthetic orders")
    d.add_argument("--no-show", action="store_true", help="save only, do not open a window")

    l = sub.add_parser("live", help="real-time monitor")
    l.add_argument("--source", choices=["sim", "real"], default="sim")
    l.add_argument("--interval", type=int, default=500, help="update interval in ms")

    args = p.parse_args()

    if args.cmd == "dashboard":
        import matplotlib
        if args.no_show:
            matplotlib.use("Agg")
        from dashboard import build_dashboard

        df = generate_sales_data(args.orders)
        OUT.mkdir(exist_ok=True)
        df.to_csv(OUT / "sales_data.csv", index=False)
        build_dashboard(df, save_path=OUT / "dashboard.png", show=not args.no_show)

    elif args.cmd == "live":
        from live_monitor import LiveMonitor, RealStream, SimulatedStream

        stream = RealStream() if args.source == "real" else SimulatedStream()
        LiveMonitor(stream, interval_ms=args.interval).run()


if __name__ == "__main__":
    main()
