"""04 - Subplots + numpy math functions (linspace, sin, cos, exp, roots)"""
import matplotlib.pyplot as plt
import numpy as np

from utils import save_and_show

x = np.linspace(0, 2 * np.pi, 300)
plt.figure(figsize=(12, 8))

# 1) sin and cos
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), color="royalblue", linewidth=2, label="sin(x)")
plt.plot(x, np.cos(x), color="crimson", linewidth=2, linestyle="--", label="cos(x)")
plt.axhline(0, color="black", linewidth=1)
plt.title("Sine and Cosine")
plt.xlabel("x (radians)")
plt.ylabel("y")
plt.grid(True, alpha=0.4)
plt.legend()

# 2) parabola with roots and vertex marked
xp = np.linspace(-1, 5, 200)
yp = xp ** 2 - 4 * xp + 3
roots = np.roots([1, -4, 3])                                # numpy: roots of x^2 - 4x + 3
plt.subplot(2, 2, 2)
plt.plot(xp, yp, color="darkgreen", linewidth=2, label="y = x² - 4x + 3")
plt.plot(roots, np.zeros_like(roots), "ro", ms=10, label="Roots: " + ", ".join(f"{r:.0f}" for r in np.sort(roots)))
plt.plot(2, -1, "b*", ms=18, label="Vertex (2, -1)")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(2, color="gray", linestyle=":", label="Axis of symmetry")
plt.title("Quadratic function")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.4)
plt.legend(fontsize=8, loc="upper center")

# 3) exponential growth and decay
xe = np.linspace(0, 3, 100)
plt.subplot(2, 2, 3)
plt.plot(xe, np.exp(xe), "g-", linewidth=2, label="growth  eˣ")
plt.plot(xe, np.exp(-xe), "r-", linewidth=2, label="decay  e⁻ˣ")
plt.title("Exponential growth & decay")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.4)
plt.legend()

# 4) damped oscillation with envelope
xd = np.linspace(0, 10, 400)
envelope = np.exp(-xd / 3)
plt.subplot(2, 2, 4)
plt.plot(xd, envelope * np.cos(3 * xd), color="purple", linewidth=1.8, label="damped wave")
plt.plot(xd, envelope, "k--", linewidth=1.2, label="envelope")
plt.plot(xd, -envelope, "k--", linewidth=1.2)
plt.title("Damped oscillation")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid(True, alpha=0.4)
plt.legend()

plt.suptitle("Math functions with NumPy + Matplotlib", fontsize=17, fontweight="bold")
plt.tight_layout()
save_and_show("04_math_functions.png")
