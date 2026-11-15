"""05 - Capstone: Student progress report (lines + markers + grid + labels + numpy)"""
import matplotlib.pyplot as plt
import numpy as np

from utils import save_and_show

subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]
tests = np.arange(1, 7)                       # 6 monthly tests
marks = np.array([
    [52, 58, 61, 67, 72, 80],                 # Maths
    [45, 49, 55, 53, 62, 68],                 # Physics
    [60, 57, 63, 66, 64, 71],                 # Chemistry
    [70, 72, 69, 75, 78, 82],                 # English
    [38, 47, 59, 66, 79, 90],                 # Computer
])
styles = ["o-", "s-", "^-", "D-", "p-"]
colors = ["royalblue", "darkorange", "seagreen", "crimson", "purple"]

class_average = marks.mean(axis=0)            # numpy: average of every test
pass_mark = 40

# ---------- Figure 1: trend of every subject ----------
plt.figure(figsize=(11, 6))
for row, name, style, color in zip(marks, subjects, styles, colors):
    plt.plot(tests, row, style, color=color, ms=9, linewidth=2, label=name)

plt.plot(tests, class_average, "k--", linewidth=3.5, label="Average of all subjects")
plt.axhline(pass_mark, color="red", linestyle=":", linewidth=2.5, label=f"Pass mark ({pass_mark})")
plt.axvline(3.5, color="gray", linestyle="-.", linewidth=1.5, label="Mid-term break")

plt.xticks(tests, [f"Test {t}" for t in tests])
plt.ylim(30, 100)
plt.title("Student Progress Report", fontsize=17, fontweight="bold")
plt.xlabel("Monthly test")
plt.ylabel("Marks (out of 100)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="lower right", ncol=2)
save_and_show("05a_student_trend.png")

# ---------- Figure 2: improvement from Test 1 to Test 6 ----------
improvement = marks[:, -1] - marks[:, 0]      # numpy: last test - first test
x = np.arange(len(subjects))
best = np.argmax(improvement)

plt.figure(figsize=(9, 5))
plt.vlines(x, 0, improvement, colors="gray", linewidth=3)
plt.plot(x, improvement, "o", ms=15, mec="black", mfc="deepskyblue", label="Improvement")
plt.plot(x[best], improvement[best], "*", ms=28, mec="black", mfc="gold",
         label=f"Most improved: {subjects[best]} (+{improvement[best]})")
plt.axhline(improvement.mean(), color="red", linestyle="--", label=f"Average gain (+{improvement.mean():.1f})")

plt.xticks(x, subjects)
plt.ylim(0, improvement.max() + 15)
plt.title("Improvement: Test 1 → Test 6", fontsize=16, fontweight="bold")
plt.xlabel("Subject")
plt.ylabel("Marks gained")
plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.legend(loc="upper left")
save_and_show("05b_student_improvement.png")
