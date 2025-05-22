# -*- coding: utf-8 -*-
# @Time : 2025/5/22 16:52
# @Author : ddz


import torch
from torch import nn


class LayerNormalization(nn.Module):
    def __init__(self, hidden_dim, eps=1e-6):
        super(LayerNormalization, self).__init__()

        self.eps = eps
        self.gamma = nn.Parameter(torch.ones(hidden_dim))
        self.beta = nn.Parameter(torch.zeros(hidden_dim))

    def forward(self, x):
        B, seq_L, C = x.shape

        mean = x.mean(dim=-1, keepdim=True)
        std = x.std(dim=-1, keepdim=True)

        out = (x - mean) / (std + self.eps)
        out = out * self.gamma + self.beta
        return out


if __name__ == "__main__":
    tensor_input = torch.rand(5, 10, 8)
    model = LayerNormalization(8)
    res = model(tensor_input)
    print(res)
