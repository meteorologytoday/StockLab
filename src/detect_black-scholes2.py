import numpy as np
import matplotlib.pyplot as plt
import BlackScholes as BS



dt  = 86400.0
sig_range = np.array([0.0, 50.0]) / dt
mu_range  = np.array([0.0, 0.1]) / dt

s = np.loadtxt("data/Black_Scholes-000.txt", unpack=True)

print("Doing posterior calculation...", end='')
p, mu_arr, sig_arr = BS.getPosterior(s, mu_range, sig_range, dt)
print(" done")
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
CS = ax.contour(mu_arr*dt, sig_arr*dt, p.T)
ax.clabel(CS)
plt.show()

