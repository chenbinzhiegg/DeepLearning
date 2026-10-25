import numpy as np

# step_function
def setp_function(x):
    return np.array(x>0,dtype=np.int64)

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
def relu(x):
    return np.maximum(0,x)