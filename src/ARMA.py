import numpy as np

def genARMATimeseries(c, phi, theta, N, rand_func):
    p = len(phi)
    q = len(theta)

    extra = max(p, q)
   
    x = np.zeros((extra + N,), dtype=float)
    epsilon = np.zeros_like(x)

    for n in range(len(epsilon)):
        epsilon[n] = rand_func()

    for n in range(extra, extra + N):

        x[n] = c + epsilon[n]

        if p > 0:
            x[n] += np.sum(phi * (x[n-p:n][::-1]))

        if q > 0:
            x[n] += np.sum(theta * (epsilon[n-q:n][::-1]))
 
   
    return x[extra:extra + N] 

def getARMAResidual(ts, c, phi, theta):
    p = len(phi)
    q = len(theta)

    extra = max(p, q)
   
    r = np.zeros((extra + N,), dtype=float)
    epsilon = np.zeros_like(x)

    for n in range(len(epsilon)):
        epsilon[n] = rand_func()

    for n in range(extra, extra + N):

        x[n] = c + epsilon[n]

        if p > 0:
            x[n] += np.sum(phi * (x[n-p:n][::-1]))

        if q > 0:
            x[n] += np.sum(theta * (epsilon[n-q:n][::-1]))
 
   
    return x[extra:extra + N] 


lines = 50
N = 100
t = list(range(100))
ts = []
for i in range(lines):
    ts.append(genARMATimeseries(0.0, [1.0], [1.0, 2.0, 3.0], N,  np.random.randn))
    np.savetxt("data/%03d.txt" % i, ts[-1])


    


import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
for i in range(lines):
    ax.plot(t, ts[i])

plt.show()