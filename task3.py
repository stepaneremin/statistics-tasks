import numpy as np

data = np.array([
    0.839, 1.065, 0.922, 0.916, 0.611, 1.041, 0.857, 1.375, 1.383, 1.381,
    0.853, 1.086, 0.786, 1.215, 1.147, 0.871, 1.203, 0.858, 1.126, 1.190,
    0.613, 1.406, 0.953, 0.700, 0.844, 0.896, 0.816, 1.089, 0.944, 0.962,
    1.137, 1.088, 1.284, 1.184, 0.967, 1.061, 0.872, 1.323, 0.949, 0.906,
    0.841, 0.708, 0.753, 0.888, 1.149, 1.202, 1.033, 1.034, 0.667, 1.102
])

n = data.size

a_mle = np.mean(data)
var_mle = np.sum((data - a_mle)**2) / n

m1 = np.mean(data)
m2 = np.mean(data**2)

a_mom = m1
var_mom = m2 - (m1**2)

bias_a = 0
bias_var = -var_mle / n

print("Оценки максимального правдоподобия параметров:")
print(f"a_mle = {a_mle:.6f}")
print(f"var_mle = {var_mle:.6f}\n")

print("Оценки ММ:")
print(f"a_mom = {a_mom:.6f}")
print(f"var_mom = {var_mom:.6f}\n")

print("Приближённое смещение оценок:")
print(f"bias(a) = {bias_a:.4f}")
print(f"bias(var_mle) ≈ {bias_var:.10f}")
