# -*- coding: utf-8 -*-
# @Time : 2025/5/20 15:06
# @Author : ddz

import torch
import torch.nn as nn


class LoRALayer(nn.Module):
    def __init__(self, original_layer, r=8, alpha=16):
        super().__init__()
        self.original = original_layer  # 原始线性层（冻结）
        self.r = r
        self.alpha = alpha

        # 低秩矩阵 A 和 B
        d, k = original_layer.weight.shape  # 原始权重矩阵W的维度是d×k
        self.A = nn.Parameter(torch.zeros(r, k))  # A 初始化为零
        self.B = nn.Parameter(torch.randn(d, r))  # B 随机初始化
        self.scaling = alpha / r  # 缩放系数

    def forward(self, x):
        # 原始输出 + LoRA 调整
        original_out = self.original(x)  # Wx
        # 矩阵乘法
        lora_weights = torch.matmul(self.lora_B, self.lora_A)
        lora_out = torch.matmul(x, lora_weights.T)
        return original_out + lora_out * self.scaling
