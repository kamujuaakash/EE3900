import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-2,1,0.01)
x=np.sinc(x)
#print(x)
y=np.fft.fft(x)
plt.plot(x,y)
plt.show()