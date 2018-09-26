import numpy as np


def generate(N, s0, mu, sig, dt):
    
    epsilon = np.random.randn(N)

    s = np.zeros((N,), dtype=float)
    s[0] = s0

    sig_adj = sig * (dt**0.5)


    for i in range(1, N):
        s[i] = s[i-1] * (1.0 + mu * dt + sig_adj * epsilon[i])

    return s


def getLogLikelihood(s, mu, sig, dt):
    
    lns = np.log(s)
    E = np.sum(((lns[1:] - lns[:-1]) - mu * dt) ** 2.0)
    N = len(lns) - 1

    return - N * (np.log(sig) + np.log(dt) / 2.0) - E / (2.0 * sig **2.0 * dt)


def getPosterior(x, mu_range, sig_range, dt, mu_n=10, sig_n=10, return_log=False):
    # Flat prior assumed
    mu_arr  = np.linspace(mu_range[0], mu_range[1], num=mu_n+1)
    sig_arr = np.linspace(sig_range[0], sig_range[1], num=sig_n+1)

    mu_arr = (mu_arr[1:] + mu_arr[:-1])/2.0
    sig_arr = (sig_arr[1:] + sig_arr[:-1])/2.0

    dsig = sig_arr[1] - sig_arr[0]
    dmu  = mu_arr[1] - mu_arr[0]

    p = np.zeros((len(mu_arr), len(sig_arr)), dtype=float)
    for i, mu in enumerate(mu_arr):
        for j, sig in enumerate(sig_arr):
            p[i, j] = getLogLikelihood(x, mu, sig, dt)

    if return_log == False:
        p -= np.amax(p)
        p = np.exp(p)
        p /= np.sum(p) * dmu * dsig

    return p, mu_arr, sig_arr


if __name__ == "__main__":


    lines = 50
    N = 1000
    t = list(range(N))
    ts = []

    dt = 86400.0
    s0  = 223.46
    sig = 10.0 / dt
    mu  = 0.05 / dt
    for i in range(lines):
        ts.append(generate(N, s0, mu, sig, dt))
        np.savetxt("data/Black_Scholes-%03d.txt" % i, ts[-1])


        


    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    for i in range(lines):
        ax.plot(t, ts[i])

#    plt.show()


