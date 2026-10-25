import numpy as np

# 阶跃函数：输入大于 0 时输出 1，否则输出 0
def step_function(x):
    # x > 0 先得到布尔数组（True/False），dtype=int 再把它转成 0/1 的整数数组
    return np.array(x>0,dtype=int)  

# sigmoid
def sigmoid(x):
    return 1/(1+np.exp(-x))

# softmax
def sofmax(a):
    c=np.max(a) 
    exp_a=np.exp(a-c)   # 防止溢出
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a

    return y

# ReLU  
# x>0 时输出 x，否则输出 0
def relu(x):
    return np.maximum(0,x)  #将x中每一个元素与0进行比较，取最大值