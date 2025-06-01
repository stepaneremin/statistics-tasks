import numpy as np
import scipy.stats as stats

data = np.array([
    0.839, 1.065, 0.922, 0.916, 0.611, 1.041, 0.857, 1.375, 1.383, 1.381,
    0.853, 1.086, 0.786, 1.215, 1.147, 0.871, 1.203, 0.858, 1.126, 1.190,
    0.613, 1.406, 0.953, 0.700, 0.844, 0.896, 0.816, 1.089, 0.944, 0.962,
    1.137, 1.088, 1.284, 1.184, 0.967, 1.061, 0.872, 1.323, 0.949, 0.906,
    0.841, 0.708, 0.753, 0.888, 1.149, 1.202, 1.033, 1.034, 0.667, 1.102
])

alpha = 0.05 
n = len(data)
mean = np.mean(data)
std = np.std(data, ddof=1)  
var = std**2

t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
mean_ci = (
    mean - t_crit * std / np.sqrt(n),
    mean + t_crit * std / np.sqrt(n)
)

chi2_lower = stats.chi2.ppf(1 - alpha / 2, df=n - 1)
chi2_upper = stats.chi2.ppf(alpha / 2, df=n - 1)
var_ci = (
    (n - 1) * var / chi2_lower,
    (n - 1) * var / chi2_upper
)

print(f"Доверительный интервал для математического ожидания: ({mean_ci[0]:.4f}, {mean_ci[1]:.4f})")
print(f"Доверительный интервал для дисперсии: ({var_ci[0]:.4f}, {var_ci[1]:.4f})")


