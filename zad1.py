import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1, 21, 1)
plt.plot(x, 1/x, label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, 20, 0, 1])
plt.legend()
plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
plt.show()