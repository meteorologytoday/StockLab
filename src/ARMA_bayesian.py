import ARMA
import numpy as np


# Now only AR1
x = np.loadtxt("data/000.txt")

test_lens = np.array([5, 10, 25, 50, 100, 250, 500, 1000])
phi_space = np.linspace(0.0, 1.5, num=100)

ln_p = np.zeros((len(test_lens), len(phi_space)), dtype=float) 
p = np.zeros_like(ln_p)

dphi = phi_space[1] - phi_space[0]

N = len(x)

for i, test_len in enumerate(test_lens):
    _x = x[:test_len]
    _x -= _x.mean()
    for j, phi in enumerate(phi_space):
        # remove mean
        E_vec = ARMA.getARResidual(_x, 0, [phi])
        ln_p[i, j] = - (N / 2.0 - 1.0) * np.log(np.sum(E_vec**2.0))

    ln_p[i, :] -= np.amax(ln_p[i])
    p[i] = np.exp(ln_p[i])
    p[i] /= dphi * np.sum(p[i])


import matplotlib.pyplot as plt

for i, test_len in enumerate(test_lens):
    plt.plot(phi_space, p[i], label="%d" % test_len)

plt.legend()
plt.show()






