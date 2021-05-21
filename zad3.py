import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,30,.1)
plt.plot(x,np.sin(x),'b',label='sin(x)')
plt.plot(x,np.cos(x),'r',label='cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x) cos(x)')
plt.legend(loc='upper right')
plt.show()
