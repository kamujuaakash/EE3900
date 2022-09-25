import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-4,4,1)
y = np.zeros(len(x))
plt.stem(-3,2)
plt.stem(-2,4)
plt.stem(-1,2)
plt.stem(0,2)
plt.stem(1,0)
plt.stem(2,-2)
plt.stem(x,y)
plt.xlabel('n')
plt.xticks(np.arange(-4,4,1))
plt.ylabel('y[n]')
plt.yticks(np.arange(-3,5,1))
plt.savefig('Assignment-2/figs/y[n].eps')
plt.savefig('Assignment-2/figs/y[n].pdf')
plt.show()

