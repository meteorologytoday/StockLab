import numpy as np


def generate(N, s0, mu, sig, dt):
    
    epsilon = np.random.randn(N)

    s = np.zeros((N,), dtype=float)
    s[0] = s0

    sig_adj = sig * (dt**0.5)


    for i in range(1, N):
        s[i] = s[i-1] * (1.0 + mu * dt + sig_adj * epsilon[i])

    return s


def getResidual(s, mu, sig, dt):
    
    epsilon = np.random.randn(N)

    s = np.zeros((N,), dtype=float)
    s[0] = s0

    sig_adj = sig * (dt**0.5)


    for i in range(1, N):
        s[i] = s[i-1] * (1.0 + mu * dt + sig_adj * epsilon[i])

    return s




lines = 50
N = 100
t = list(range(100))
ts = []

dt = 86400.0
s0  = 223.46
sig = 10.0 / dt
mu  = 0.1 / dt
for i in range(lines):
    ts.append(generate(N, s0, mu, sig, dt))
    np.savetxt("data/Black_Scholes-%03d.txt" % i, ts[-1])


    


import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
for i in range(lines):
    ax.plot(t, ts[i])

plt.show()


