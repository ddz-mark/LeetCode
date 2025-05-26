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


class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        # 可学习参数：缩放 (gamma)，无偏置
        self.gamma = nn.Parameter(torch.ones(dim))  # shape: [dim]

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: 输入张量，shape 为 [batch_size, seq_len, dim] 或 [batch_size, dim]
        Returns:
            归一化后的张量，shape 与输入相同
        """
        # 计算均方根 (RMS)，不减去均值
        rms = torch.sqrt(
            x.pow(2).mean(dim=-1, keepdim=True) + self.eps)  # shape: [batch_size, seq_len, 1] 或 [batch_size, 1]

        # 归一化：除 RMS
        x_normalized = x / rms  # shape 同输入

        # 缩放（无偏置）
        return self.gamma * x_normalized  # shape 同输入


if __name__ == "__main__":
    tensor_input = torch.rand(5, 10, 8)
    model = LayerNormalization(8)
    res = model(tensor_input)
    print(res)
