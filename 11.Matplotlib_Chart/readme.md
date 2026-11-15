# Matplotlib Real-World Project: Sales Dashboard + Live Monitor

Two mini-projects that cover what Matplotlib is actually used for at work.

## 1. Static analytics dashboard (`dashboard.py`)
One figure, 7 charts + KPI cards, built with `GridSpec`:

| Chart | Matplotlib concept |
|---|---|
| Monthly revenue (line + fill + annotation) | `plot`, `fill_between`, `annotate`, date formatter |
| Category share (donut) | `pie` with `wedgeprops` |
| Revenue by category | `barh`, `bar_label`, custom `FuncFormatter` |
| Order value distribution | `hist`, `axvline` (mean / median) |
| Price vs quantity | `scatter`, colormap, `colorbar`, log scale |
| Weekday x hour heatmap | `imshow`, `pd.crosstab` |
| Order value by region | `boxplot` with styled boxes |

## 2. Live monitor (`live_monitor.py`)
Real-time CPU / memory / network charts using `FuncAnimation`:
rolling window (`deque`), alert threshold with shaded danger zone, live value labels,
SPACE key to pause/resume. Works with simulated data or your real machine (`psutil`).

## Run (Windows / any OS)
```
pip install -r requirements.txt
python main.py dashboard             # opens window + saves output/dashboard.png
python main.py dashboard --no-show   # only save the PNG
python main.py live                  # simulated live monitor
python main.py live --source real    # your real CPU / RAM / network
```

## Files
- `data.py` - synthetic sales data (replace with `pd.read_csv(...)` for real data)
- `dashboard.py` - all static charts
- `live_monitor.py` - data streams + animated monitor
- `main.py` - command-line entry point

## Practice ideas
1. Load your own CSV in `main.py` and keep the same column names.
2. Add a 4th live chart (disk usage) and an `alerts.log` file.
3. Export the dashboard to PDF with `savefig("report.pdf")`.
4. Add a `--region North` filter to the dashboard.
