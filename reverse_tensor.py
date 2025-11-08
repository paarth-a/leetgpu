import torch
#https://leetgpu.com/challenges/reverse-array
# input is a tensor on the GPU
def solve(input: torch.Tensor, N: int):
    x = torch.flip(input, [0])

    input.copy_(x)