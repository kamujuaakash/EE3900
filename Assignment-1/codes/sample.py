import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3,4,1)
y = np.zeros(len(x))

plt.stem(-1,-2)
plt.stem(-2,-4)
plt.stem(-3,-8)
plt.stem(x,y)
plt.xlabel('n')
plt.xticks(np.arange(-3,4,1))
plt.ylabel('x(n)')
plt.yticks(np.arange(-8,4,2))
#plt.savefig('Assignment-1/figs/unitsample.eps')
#plt.savefig('Assignment-1/figs/unitsample.pdf')
plt.show()
