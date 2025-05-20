# -*- coding: utf-8 -*-
# @Time : 2025/5/20 15:00
# @Author : ddz
import torch
from torch import nn


class MHA(nn.Module):
    def __init__(self, C_in, dmodel, num_head=8, p_drop=0.2):
        super(MHA, self).__init__()

        self.QW = nn.Linear(C_in, dmodel)
        self.KW = nn.Linear(C_in, dmodel)
        self.VW = nn.Linear(C_in, dmodel)

        self.dp = nn.Dropout(p_drop)

        self.W_concat = nn.Linear(dmodel, dmodel)

        self.n_head = num_head
        self.p_drop = p_drop
        self.depth = dmodel // num_head

    def forward(self, X, casual=True):
        B, L, C = X.shape
        Q = self.QW(X)
        K = self.KW(X)
        V = self.VW(X)

        Q = Q.reshape((B, L, self.n_head, -1)).permute(0, 2, 1, 3)
        K = K.reshape((B, L, self.n_head, -1)).permute(0, 2, 1, 3)
        V = V.reshape((B, L, self.n_head, -1)).permute(0, 2, 1, 3)

        atten = Q.matmul(K.transpose(2, 3))

        if casual:
            mask = torch.triu(torch.ones(L, L))
            atten = torch.where(mask == 1, atten, torch.ones_like(atten) * (-2 ** 32 + 1))
        atten = torch.softmax(atten, dim=-1)

        atten = self.dp(atten)

        out = torch.matmul(atten, V) / self.depth ** (1 / 2)

        out = out.permute(0, 2, 1, 3).reshape(B, L, -1)
        out = self.W_concat(out)

        return out


if __name__ == "__main__":
    input = torch.rand(10, 5, 3)
    model = MHA(3, 64, 4)
    res = model(input)
