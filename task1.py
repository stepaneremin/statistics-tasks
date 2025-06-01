import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

values = [
    0.839, 1.065, 0.922, 0.916, 0.611, 1.041, 0.857, 1.375, 1.383, 1.381,
    0.853, 1.086, 0.786, 1.215, 1.147, 0.871, 1.203, 0.858, 1.126, 1.190,
    0.613, 1.406, 0.953, 0.700, 0.844, 0.896, 0.816, 1.089, 0.944, 0.962,
    1.137, 1.088, 1.284, 1.184, 0.967, 1.061, 0.872, 1.323, 0.949, 0.906,
    0.841, 0.708, 0.753, 0.888, 1.149, 1.202, 1.033, 1.034, 0.667, 1.102
]

sorted_values = sorted(values)

n = len(sorted_values)
ecdf = np.arange(1, n+1) / n

#Вывод значений закомментирован во избежание спама в консоли
#for x, fn in zip(sorted_values, ecdf):
    #print(f"F_n({x:.3f}) = {fn:.2f}")


plt.figure(figsize=(10, 6))
plt.step(sorted_values, ecdf, where='post', linewidth=2, label='ЭФР')

plt.title('Эмпирическая функция распределения', fontsize=14)
plt.xlabel('Значения выборки', fontsize=12)
plt.ylabel('$F_n(x)$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

plt.savefig('ecdf_plot1.png', dpi=300, bbox_inches='tight')
plt.show()
е
data = np.array([
    0.839, 1.065, 0.922, 0.916, 0.611, 1.041, 0.857, 1.375, 1.383, 1.381,
    0.853, 1.086, 0.786, 1.215, 1.147, 0.871, 1.203, 0.858, 1.126, 1.190,
    0.613, 1.406, 0.953, 0.700, 0.844, 0.896, 0.816, 1.089, 0.944, 0.962,
    1.137, 1.088, 1.284, 1.184, 0.967, 1.061, 0.872, 1.323, 0.949, 0.906,
    0.841, 0.708, 0.753, 0.888, 1.149, 1.202, 1.033, 1.034, 0.667, 1.102
])

h = 0.05
bins = np.arange(min(data), max(data) + h, h)

plt.figure(figsize=(10, 6))

counts, bins, patches = plt.hist(
    data, 
    bins=bins, 
    edgecolor='black', 
    alpha=0.5, 
    label=f'Гистограмма (h={h})',
    color='skyblue',
    density=False
)

mid_bins = (bins[:-1] + bins[1:]) / 2
plt.plot(
    mid_bins, 
    counts, 
    'ro-', 
    linewidth=2, 
    markersize=6, 
    label='Полигон частот'
)

plt.title('Гистограмма и полигон частот', fontsize=14)
plt.xlabel('Значения', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.gca().xaxis.set_major_locator(MultipleLocator(0.1))  # Шаг 0.1 по оси X
plt.gca().yaxis.set_major_locator(MultipleLocator(2))    # Шаг 2 по оси Y

plt.tight_layout()

plt.savefig('combined_plot.pdf', bbox_inches='tight')  # Для LaTeX
plt.savefig('combined_plot.png', dpi=300, bbox_inches='tight')  # Для предпросмотра
plt.show()
