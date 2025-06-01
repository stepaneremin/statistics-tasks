import numpy as np
from scipy.stats import norm, chi2

data = np.array([
    0.839, 1.065, 0.922, 0.916, 0.611, 1.041, 0.857, 1.375, 1.383, 1.381,
    0.853, 1.086, 0.786, 1.215, 1.147, 0.871, 1.203, 0.858, 1.126, 1.190,
    0.613, 1.406, 0.953, 0.700, 0.844, 0.896, 0.816, 1.089, 0.944, 0.962,
    1.137, 1.088, 1.284, 1.184, 0.967, 1.061, 0.872, 1.323, 0.949, 0.906,
    0.841, 0.708, 0.753, 0.888, 1.149, 1.202, 1.033, 1.034, 0.667, 1.102
])

a0, sigma0 = 1.00, 0.20
alpha = 0.05
n = len(data)

bins = np.arange(0.6, 1.5 + 0.05, 0.05)

observed, _ = np.histogram(data, bins=bins)

probs = norm.cdf((bins[1:] - a0)/sigma0) - norm.cdf((bins[:-1] - a0)/sigma0)
expected = probs * n

for i in range(len(expected)):
    if expected[i] < 5:
        observed[i+1] += observed[i]
        expected[i+1] += expected[i]
        observed = np.delete(observed, i)
        expected = np.delete(expected, i)
        bins = np.delete(bins, i)
        break

chi2_stat = np.sum((observed - expected)**2 / expected)
dof = len(observed) - 1 

crit_value = chi2.ppf(1 - alpha, df=dof)
p_value = 1 - chi2.cdf(chi2_stat, df=dof)

print(f"χ² = {chi2_stat:.4f}")
print(f"Критическое значение = {crit_value:.4f}")
print(f"p-value = {p_value:.4f}")
print(f"Степени свободы = {dof}")
