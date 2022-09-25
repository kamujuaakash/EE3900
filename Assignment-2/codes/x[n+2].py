import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3,3,1)
y = np.zeros(len(x))

plt.stem(-2,1)
plt.stem(-1,2)
plt.stem(0,0)
plt.stem(1,-1)
plt.stem(x,y)
plt.xlabel('n')
plt.xticks(np.arange(-3,3,1))
plt.ylabel('x[n+2]')
plt.yticks(np.arange(-2,2,1))
plt.savefig('Assignment-2/figs/x[n+2].eps')
plt.savefig('Assignment-2/figs/x[n+2].pdf')
plt.show()

