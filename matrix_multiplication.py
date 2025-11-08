import torch
#https://leetgpu.com/challenges/matrix-multiplication
# A, B, C are tensors on the GPU
def solve(A: torch.Tensor, B: torch.Tensor, C: torch.Tensor, M: int, N: int, K: int):
    

    C.copy_(torch.mm(A,B))

    return C