import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(12,16,200)

fy = x**2+2

fig  = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,fy,'r')

plt.show()