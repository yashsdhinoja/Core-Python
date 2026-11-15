import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, color="teal", marker="o", label="y = 2x")
ax.set_title("Simple Line Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)
plt.show()