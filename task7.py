import numpy as np
from scipy.stats import norm, chi2, chisquare

x = np.array([
    0.839, 1.065, 0.922, 0.916, 0.611, 1.041, 0.857, 1.375, 1.383, 1.381,
    0.853, 1.086, 0.786, 1.215, 1.147, 0.871, 1.203, 0.858, 1.126, 1.190,
    0.613, 1.406, 0.953, 0.700, 0.844, 0.896, 0.816, 1.089, 0.944, 0.962,
    1.137, 1.088, 1.284, 1.184, 0.967, 1.061, 0.872, 1.323, 0.949, 0.906,
    0.841, 0.708, 0.753, 0.888, 1.149, 1.202, 1.033, 1.034, 0.667, 1.102])
n = len(x)
a = np.mean(x)
s = np.std(x, ddof=0)

borders = [-np.inf, 0.85, 1.00, 1.15, np.inf]
freq, _ = np.histogram(x, bins=borders)

phi = norm.cdf(borders, loc=a, scale=s)
p = np.diff(phi)
e = n * p

r = chisquare(f_obs=freq, f_exp=e, ddof=2)
v = len(freq) - 3
q = chi2.ppf(1 - 0.01, df=v)

print(f"Оценка среднего: a = {a:.4f}")
print(f"Оценка сигмы: sigma = {s:.4f}")
print(f"Статистика хи-квадрат: {r.statistic:.4f}")
print(f"Критическое значение: {q:.4f}")
print(f"p-value: {r.pvalue:.4f}")
if r.statistic > q:
    print("Гипотеза отвергается.")
else:
    print("Нет оснований отвергнуть гипотезу.")
print(f"Максимальный уровень значимости: {r.pvalue:.4f}")
