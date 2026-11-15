"""Static analytics dashboard: 7 charts + KPI strip in one figure (GridSpec)."""
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyBboxPatch
from matplotlib.ticker import FuncFormatter

from data import WEEKDAYS

PALETTE = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3"]
ACCENT = "#4C72B0"


def money(x, _pos=None):
    """Format numbers as $1.2K / $3.4M (used for axis ticks and labels)."""
    if abs(x) >= 1e6:
        return f"${x / 1e6:.1f}M"
    if abs(x) >= 1e3:
        return f"${x / 1e3:.0f}K"
    return f"${x:.0f}"


def _style():
    plt.rcParams.update(
        {
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.titleweight": "bold",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "figure.facecolor": "white",
        }
    )


def _kpi_strip(fig, df):
    ax = fig.add_axes([0.06, 0.87, 0.91, 0.07])
    ax.axis("off")
    top_cat = df.groupby("category")["revenue"].sum().idxmax()
    kpis = [
        ("Total revenue", money(df["revenue"].sum())),
        ("Orders", f"{len(df):,}"),
        ("Avg order value", f"${df['revenue'].mean():,.2f}"),
        ("Top category", top_cat),
    ]
    w = 0.22
    for i, (label, value) in enumerate(kpis):
        x = 0.01 + i * (w + 0.03)
        ax.add_patch(
            FancyBboxPatch(
                (x, 0.05), w, 0.9, boxstyle="round,pad=0.01,rounding_size=0.04",
                fc="#f4f6fb", ec="#d0d7e6", transform=ax.transAxes,
            )
        )
        ax.text(x + 0.02, 0.68, label, transform=ax.transAxes, fontsize=9, color="#667")
        ax.text(x + 0.02, 0.25, value, transform=ax.transAxes, fontsize=16, weight="bold")


def build_dashboard(df: pd.DataFrame, save_path=None, show=True):
    _style()
    fig = plt.figure(figsize=(18, 11))
    fig.suptitle("Sales Analytics Dashboard - 2025", fontsize=20, weight="bold", x=0.06, ha="left", y=0.985)
    _kpi_strip(fig, df)
    gs = fig.add_gridspec(3, 3, left=0.06, right=0.97, bottom=0.06, top=0.82, hspace=0.5, wspace=0.28)

    # 1) Monthly revenue trend (spans 2 columns) -------------------------
    ax = fig.add_subplot(gs[0, :2])
    monthly = df.groupby("month")["revenue"].sum()
    ax.plot(monthly.index, monthly.values, marker="o", lw=2.5, color=ACCENT)
    ax.fill_between(monthly.index, monthly.values, alpha=0.15, color=ACCENT)
    peak_x, peak_y = monthly.idxmax(), monthly.max()
    ax.annotate(
        f"Peak: {money(peak_y)}", xy=(peak_x, peak_y), xytext=(-90, -5),
        textcoords="offset points", arrowprops=dict(arrowstyle="->", color="#C44E52"),
        color="#C44E52", weight="bold",
    )
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    ax.yaxis.set_major_formatter(FuncFormatter(money))
    ax.set_title("Monthly revenue")

    # 2) Category share donut -------------------------------------------
    ax = fig.add_subplot(gs[0, 2])
    cat = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    ax.pie(
        cat.values, labels=cat.index, colors=PALETTE, startangle=90, counterclock=False,
        autopct="%1.0f%%", pctdistance=0.78, labeldistance=1.12, wedgeprops=dict(width=0.45, edgecolor="white"),
    )
    ax.set_title("Revenue share by category")

    # 3) Revenue by category (horizontal bars with labels) ---------------
    ax = fig.add_subplot(gs[1, 0])
    cat_sorted = cat.sort_values()
    bars = ax.barh(cat_sorted.index, cat_sorted.values, color=ACCENT)
    ax.bar_label(bars, labels=[money(v) for v in cat_sorted.values], padding=3)
    ax.xaxis.set_major_formatter(FuncFormatter(money))
    ax.set_xlim(0, cat_sorted.max() * 1.18)
    ax.set_title("Revenue by category")
    ax.grid(axis="y", visible=False)

    # 4) Order value distribution ----------------------------------------
    ax = fig.add_subplot(gs[1, 1])
    vals = df["revenue"].clip(upper=df["revenue"].quantile(0.99))
    ax.hist(vals, bins=40, color="#55A868", edgecolor="white")
    ax.axvline(df["revenue"].mean(), color="#C44E52", ls="--", lw=2, label=f"Mean ${df['revenue'].mean():,.0f}")
    ax.axvline(df["revenue"].median(), color="#333", ls=":", lw=2, label=f"Median ${df['revenue'].median():,.0f}")
    ax.set_xlabel("Order value ($)")
    ax.set_ylabel("Orders")
    ax.legend(frameon=False)
    ax.set_title("Order value distribution")

    # 5) Price vs quantity scatter coloured by discount ------------------
    ax = fig.add_subplot(gs[1, 2])
    sample = df.sample(min(900, len(df)), random_state=1)
    sc = ax.scatter(
        sample["unit_price"], sample["quantity"] + np.random.default_rng(0).uniform(-0.15, 0.15, len(sample)),
        c=sample["discount"] * 100, cmap="viridis", s=18, alpha=0.7,
    )
    fig.colorbar(sc, ax=ax, label="Discount %", pad=0.02)
    ax.set_xscale("log")
    ax.set_xlabel("Unit price ($, log scale)")
    ax.set_ylabel("Quantity")
    ax.set_title("Price vs quantity")

    # 6) Heatmap weekday x hour (spans 2 columns) ------------------------
    ax = fig.add_subplot(gs[2, :2])
    grid = pd.crosstab(df["weekday"], df["hour"]).reindex(WEEKDAYS).reindex(columns=range(24), fill_value=0)
    im = ax.imshow(grid.values, aspect="auto", cmap="YlOrRd")
    ax.set_xticks(range(0, 24, 2), [f"{h:02d}:00" for h in range(0, 24, 2)])
    ax.set_yticks(range(7), WEEKDAYS)
    ax.grid(False)
    fig.colorbar(im, ax=ax, label="Orders", pad=0.01)
    ax.set_title("When do customers order? (weekday x hour)")

    # 7) Revenue distribution by region (box plot) -----------------------
    ax = fig.add_subplot(gs[2, 2])
    regions = sorted(df["region"].unique())
    data = [df.loc[df["region"] == r, "revenue"].clip(upper=df["revenue"].quantile(0.97)) for r in regions]
    bp = ax.boxplot(data, tick_labels=regions, patch_artist=True, showmeans=True, widths=0.6)
    for patch, color in zip(bp["boxes"], PALETTE):
        patch.set(facecolor=color, alpha=0.6)
    ax.set_ylabel("Order value ($)")
    ax.set_title("Order value by region")

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"Saved dashboard -> {save_path}")
    if show:
        plt.show()
    return fig
