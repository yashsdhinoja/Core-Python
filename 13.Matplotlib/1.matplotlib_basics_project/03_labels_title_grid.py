"""03 - Labels, title (fontdict, loc), grid options, legend, trend line with numpy"""
import matplotlib.pyplot as plt
import numpy as np

from utils import save_and_show

hours = np.arange(1, 11)
score = np.array([35, 42, 48, 55, 61, 68, 72, 79, 85, 91])

title_font = {"family": "serif", "color": "darkred", "size": 15, "weight": "bold"}
label_font = {"family": "serif", "color": "darkblue", "size": 12}

# numpy: best-fit straight line  y = m*x + c
m, c = np.polyfit(hours, score, 1)
trend = np.poly1d([m, c])

plt.figure(figsize=(12, 5))

# ----- left: default grid -----
plt.subplot(1, 2, 1)
plt.plot(hours, score, "o-", color="teal", ms=9, label="Score")
plt.title("Default grid", fontdict=title_font, loc="left")
plt.xlabel("Study hours per day", fontdict=label_font)
plt.ylabel("Exam score", fontdict=label_font)
plt.grid(True)
plt.legend()

# ----- right: styled grid + trend line + reference lines -----
plt.subplot(1, 2, 2)
plt.plot(hours, score, "D", ms=9, mec="black", mfc="orange", label="Score")
plt.plot(hours, trend(hours), "r--", linewidth=2, label=f"Trend: y = {m:.1f}x + {c:.1f}")
plt.axhline(40, color="gray", linestyle=":", label="Pass mark (40)")
plt.axvline(5, color="purple", linestyle="-.", label="5 hours")
plt.title("Custom grid + trend line", fontdict=title_font, loc="left")
plt.xlabel("Study hours per day", fontdict=label_font)
plt.ylabel("Exam score", fontdict=label_font)
plt.grid(color="green", linestyle="--", linewidth=0.6)      # styled grid
plt.legend(loc="lower right")

plt.tight_layout()
save_and_show("03_labels_title_grid.png")
