import numpy as np
def cosine_similarity(a,b): 
    a=np.mat(a)#把list转换为matrix
    b=np.mat(b)
    num=float(a * b.T)
    #linalg.norm()计算向量的范数
    denom=np.linalg.norm(a)*np.linalg.norm(a)
    return 0.5+0.5*(num/denom)#cosine similarity的范围为[-1,1],先把他归一化至[0,1]
