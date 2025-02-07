import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = np.random.randint(1, 50, (10, 1))

plt.plot(x, y, "green")
plt.xlabel("x değerleri")
plt.ylabel("y değerleri")
plt.title("x-y grafiği")

print("*****************************")
plt.subplot(2, 2, 1)
plt.plot(x, x ** 2, "red")
plt.subplot(2, 2, 2)
plt.plot(x, x * 2, "green")
plt.subplot(2, 2, 3)
plt.plot(x, x ** 3, "blue")
plt.subplot(2, 2, 4)
plt.plot(x, x ** (1 / 2), "black")

print("*****************************")

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(4, 4))
axes[0].plot(x, y, "green")
axes[0].set_title("axes 0")

axes[1].plot(x, y, "red")
axes[1].set_title("axes 1")
plt.tight_layout()

print("*****************************")

fig1, axes = plt.subplots(figsize=(6, 6))

axes.plot(x, x, label="x", color="red", linewidth=2, linestyle="-", marker="o", markeredgecolor="black",
          markeredgewidth=5)
axes.plot(x, x ** 2, label="x**2", color="orange", linewidth=3, linestyle="--", marker="v", markeredgecolor="black",
          markeredgewidth=5)
axes.plot(x, x ** 3, label="x**3", color="blue", linewidth=4, linestyle="-.", marker="x", markeredgecolor="black",
          markeredgewidth=5)
axes.plot(x, x ** 4, label="x**4", color="purple", linewidth=5, linestyle=":", marker="s", markeredgecolor="black",
          markeredgewidth=5)
axes.plot(x, x ** 5, label="x**5", color="pink", linewidth=6, linestyle="--", marker="d", markeredgecolor="black",
          markeredgewidth=5)

axes.legend()

# pasta grafik

letters = ["A", "B", "C", "D", "E", "F"]
numbers = [25, 45, 15, 30, 20, 10]

fig2 = plt.figure(figsize=(5, 5))
plt.pie(numbers, labels=letters)

# bar grafik

fig3 = plt.figure(figsize=(5, 5))  # Figür oluştur
ax1 = fig3.add_axes((0.1, 0.1, 0.8, 0.8))  # Ekseni ekle

letters = ["A", "B", "C", "D", "E", "F"]
numbers = [25, 45, 15, 30, 20, 10]

ax1.bar(letters, numbers)  # Çubuk grafiği çiz
# plt.show()  # Grafiği göster

# scatter grafik

x1 = np.arange(1, 21)
y1 = np.random.randint(1, 150, (20, 1))

plt.scatter(x1, y1)
# plt.show()

# histogram grafik

y1 = np.random.randint(1, 150, (20, 1))
plt.hist(y1)
plt.show()
