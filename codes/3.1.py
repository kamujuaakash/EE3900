import numpy as np
import matplotlib.pyplot as plt

x=np.loadtxt('codes/xn.dat')

plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.xlabel('$n$')

plt.grid()
plt.savefig('/home/aakash/Desktop/EE3900/figs/3.1.pdf')
plt.savefig('/home/aakash/Desktop/EE3900/figs/3.1.eps')
plt.show()