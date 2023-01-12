import torch
import math
import matrix_rot
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 这里 t 是一个数，不是矩阵
def res(t, T1, T2, df):
    phi = 2*math.pi*df*t/1000
    E1 = torch.exp(-t/T1).to(device)	
    E2 = torch.exp(-t/T2).to(device)
    z = matrix_rot.zrot(phi)
    A = torch.Tensor([
        [E2,0,0],
        [0,E2,0],
        [0,0,E1]
    ]).to(device) @ z
    B = torch.Tensor([0,0,1-E1]).T
    return A, B