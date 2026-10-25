# sigmoid 图形
import numpy as np
import matplotlib.pylab as plt
from functions import sigmoid


x=np.arange(-5,5,0.001)
y=sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)  #指定y范围
plt.show()