import numpy as np
import matplotlib.pyplot as plt
import BlackScholes as BS



dt  = 86400.0
sigs = np.linspace(0.0, 100.0, num=20)[1:] / dt
mu  = 0.05 / dt 

dsig = sigs[1] - sigs[0]

s = np.loadtxt("data/Black_Scholes-000.txt", unpack=True)

test_lens = (np.array([0.1, 0.2, 0.5, 0.8, 1.0]) * len(s)).astype(int)

p = np.zeros((len(test_lens), len(sigs)), dtype=float)


for i, test_len in enumerate(test_lens):
    for j, sig in enumerate(sigs):
        p[i, j] = BS.getLogLikelihood(s[:test_len], mu, sig, dt)

    p[i] -= np.amax(p[i])
    p[i] = np.exp(p[i])
    p[i] /= np.sum(p[i]) * dsig


fig, ax = plt.subplots(2, 1, figsize=(12, 8))
for i, test_len in enumerate(test_lens):
    ax[0].plot(sigs * dt, p[i], label="%d" % test_len)

ax[0].legend()
#r = BS.getResidual(s, mu, 50.0/dt, dt)
#hist, bin_edges = np.histogram(r, density=True)
#print(hist)
#print(bin_edges)
#ax[1].bar((bin_edges[:-1] + bin_edges[1:]) / 2.0, hist)
plt.show()

