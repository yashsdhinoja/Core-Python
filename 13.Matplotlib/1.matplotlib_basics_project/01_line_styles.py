"""01 - Lines: linestyle, linewidth, color  (Monthly temperature of 3 cities)"""
import matplotlib.pyplot as plt
import numpy as np

from utils import save_and_show

months = np.arange(1, 13)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

delhi = np.array([14, 17, 23, 30, 35, 36, 33, 32, 31, 26, 20, 15]) # means (14, 17, 23, 30, 35, 36, 33, 32, 31, 26, 20, 15) / 12 = 26
mumbai = np.array([24, 25, 28, 30, 31, 29, 27, 27, 27, 29, 28, 26]) 
shimla = np.array([3, 4, 8, 13, 17, 19, 18, 17, 15, 11, 7, 4])
average = np.mean([delhi, mumbai, shimla], axis=0)        # numpy: mean of 3 cities

# ---------- Figure 1: three cities + average ----------
plt.figure(figsize=(10, 5))
plt.plot(months, delhi, color="crimson", linestyle="-", linewidth=2.5, label="Delhi  (solid)")
plt.plot(months, mumbai, color="royalblue", linestyle="--", linewidth=2.5, label="Mumbai  (dashed)")
plt.plot(months, shimla, color="seagreen", linestyle=":", linewidth=3.5, label="Shimla  (dotted)")
plt.plot(months, average, color="black", linestyle="-.", linewidth=2, label="Average  (dash-dot)")

plt.xticks(months, month_names)
plt.title("Average Monthly Temperature", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True, alpha=0.4)
plt.legend()
save_and_show("01a_line_styles_cities.png")

# ---------- Figure 2: line style gallery ----------
x = np.linspace(0, 10, 50)
styles = ["-", "--", "-.", ":"]
names = ["solid  '-'", "dashed  '--'", "dash-dot  '-.'", "dotted  ':'"]

plt.figure(figsize=(8, 4.5))
for i, (style, name) in enumerate(zip(styles, names)):
    plt.plot(x, np.full_like(x, 4 - i), linestyle=style, linewidth=3, label=name)
plt.ylim(-0.5, 5)
plt.yticks([])
plt.title("Line style gallery", fontsize=15, fontweight="bold")
plt.xlabel("x")
plt.grid(True, axis="x", alpha=0.4)
plt.legend(loc="center right")
save_and_show("01b_line_style_gallery.png")