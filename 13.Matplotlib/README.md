# Matplotlib Basics Project

A beginner-friendly project that uses **only `numpy` and `matplotlib.pyplot`**.
It covers the core ideas of plotting: **lines, markers, labels, titles, grids, legends and subplots**,
with real-looking data (city temperatures, fitness steps, exam scores, student marks).

> No pandas, no seaborn - just the fundamentals.

---

## Table of contents
1. [Project structure](#project-structure)
2. [Setup and run](#setup-and-run)
3. [Output gallery](#output-gallery)
   - [01 - Line styles](#01---line-styles)
   - [02 - Markers](#02---markers)
   - [03 - Labels, title and grid](#03---labels-title-and-grid)
   - [04 - Subplots and math functions](#04---subplots-and-math-functions)
   - [05 - Capstone: student progress report](#05---capstone-student-progress-report)
4. [Quick cheat sheet](#quick-cheat-sheet)
5. [Common mistake: marker defined twice](#common-mistake-marker-defined-twice)
6. [What you learn](#what-you-learn)

---

## Project structure
```
matplotlib_basics_project/
├── 01_line_styles.py          # linestyle, linewidth, color
├── 02_markers.py              # marker, ms, mec, mfc, format strings
├── 03_labels_title_grid.py    # xlabel, ylabel, title, fontdict, grid, trend line
├── 04_math_functions.py       # subplot, numpy functions
├── 05_student_report.py       # capstone project
├── utils.py                   # saves each figure into images/
├── run_all.py                 # runs every script
├── requirements.txt
├── images/                    # generated charts (shown below)
└── README.md
```

## Setup and run
```bash
pip install -r requirements.txt

python 01_line_styles.py        # run one script (opens a window and saves a PNG)
python run_all.py               # run everything
python run_all.py --no-show     # only save the PNGs into images/
```

---

## Output gallery

### 01 - Line styles
`plt.plot(x, y, linestyle=..., linewidth=..., color=...)`, plus `np.mean` to build an average line.

![Average monthly temperature](images/01a_line_styles_cities.png)

![Line style gallery](images/01b_line_style_gallery.png)

### 02 - Markers
All common marker codes, then a steps tracker that uses `ms`, `mec`, `mfc`, format strings (`'o-'`, `'s--'`),
`plt.axhline` for the goal line and `np.argmax` to find the best day.

![Marker gallery](images/02a_marker_gallery.png)

![Weekly steps tracker](images/02b_steps_tracker.png)

### 03 - Labels, title and grid
Left: default grid. Right: styled grid, `axhline` / `axvline` reference lines and a
best-fit trend line from `np.polyfit` + `np.poly1d`. Fonts are customised with `fontdict`.

![Labels, title and grid](images/03_labels_title_grid.png)

### 04 - Subplots and math functions
`plt.subplot(2, 2, n)` with `np.linspace`, `np.sin`, `np.cos`, `np.exp` and `np.roots`.

![Math functions](images/04_math_functions.png)

### 05 - Capstone: student progress report
Five subjects across six monthly tests: one line per subject, a thick dashed class average,
a pass-mark line and a mid-term divider. The second chart shows each subject's improvement
using `plt.vlines` and a highlighted star marker.

![Student progress](images/05a_student_trend.png)

![Student improvement](images/05b_student_improvement.png)

---

## Quick cheat sheet

**Line styles**

| Code | Style | | Code | Style |
|---|---|---|---|---|
| `'-'` | solid | | `'-.'` | dash-dot |
| `'--'` | dashed | | `':'` | dotted |

**Common markers**

| Code | Marker | | Code | Marker |
|---|---|---|---|---|
| `'o'` | circle | | `'s'` | square |
| `'*'` | star | | `'D'` | diamond |
| `'^'` `'v'` `'<'` `'>'` | triangles | | `'p'` `'H'` `'h'` | pentagon / hexagons |
| `'x'` `'+'` `'P'` | crosses | | `'.'` | small dot |

**Marker and line options**

| Argument | Short | Meaning |
|---|---|---|
| `marker` | | marker shape |
| `markersize` | `ms` | marker size |
| `markeredgecolor` | `mec` | marker border color |
| `markerfacecolor` | `mfc` | marker fill color |
| `linestyle` | `ls` | line style |
| `linewidth` | `lw` | line thickness |

**Format string:** `'[marker][line][color]'` - for example `'o--r'` is circle markers, dashed line, red.

**Helpers used**

| Function | Purpose |
|---|---|
| `plt.xlabel()` `plt.ylabel()` `plt.title()` | labels and title (`fontdict`, `loc`) |
| `plt.grid(True)` | grid (`color`, `linestyle`, `linewidth`, `axis='x'/'y'`) |
| `plt.axhline()` `plt.axvline()` | horizontal / vertical reference line |
| `plt.legend()` | legend (`loc`, `ncol`) |
| `plt.xticks()` `plt.yticks()` | custom tick positions and labels |
| `plt.subplot(r, c, n)` | several charts in one figure |
| `plt.savefig()` | save the chart as an image |

---

## Common mistake: marker defined twice
```python
plt.plot(y, 'o-.', marker="H")     # UserWarning: marker is redundantly defined
```
The format string `'o-.'` already contains a marker (`o`), and `marker="H"` sets another one.
Matplotlib keeps the keyword (`H`) and warns you. Fix it by using only one of them:
```python
plt.plot(y, '-.', marker="H")                  # line style in the string, marker as keyword
plt.plot(y, linestyle='-.', marker="H")        # or use keywords only
```

## What you learn
- Plotting single and multiple lines on one chart
- Customising lines (style, width, color) and markers (shape, size, edge, fill)
- Adding labels, titles, legends and grids
- Drawing reference lines (`axhline`, `axvline`) and highlighting points
- Using NumPy (`linspace`, `mean`, `argmax`, `polyfit`, `roots`) to prepare data
- Building multi-chart figures with `subplot`

---
Author: **Yash Dhinoja** - [github.com/yashsdhinoja](https://github.com/yashsdhinoja)
