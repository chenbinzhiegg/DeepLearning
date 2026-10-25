# 阶跃函数图形
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0,dtype=int)  

x=np.arange(-0.5,0.5,0.001)
y=step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)  #指定y范围
plt.show()