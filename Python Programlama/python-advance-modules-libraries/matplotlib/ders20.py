import matplotlib.pyplot as plt
import numpy as np

# Örnek veriler oluşturun
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# İki farklı grafik çizin
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')

# Eksen etiketleri ve başlık ekleyin
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin(x) ve Cos(x) Grafikleri')

# Grafiklere bir açıklama ekleyin
plt.legend()

# Grafiği gösterin
plt.show()