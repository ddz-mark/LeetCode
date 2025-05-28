# -*- coding: utf-8 -*-
# @Time : 2025/5/28 10:18
# @Author : ddz

import torch
from torch import nn
import torch.nn.functional as F


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        # 线性变换矩阵
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def split_heads(self, x):
        # 将输入分割为多个头 [batch_size, seq_len, d_model] -> [batch_size, num_heads, seq_len, head_dim]
        batch_size, seq_len, _ = x.size()
        return x.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

    def forward(self, q, k, v, mask=None):
        # 线性变换
        Q = self.W_q(q)  # [batch_size, seq_len, d_model]
        K = self.W_k(k)
        V = self.W_v(v)

        # 分割多头
        Q = self.split_heads(Q)  # [batch_size, num_heads, seq_len, head_dim]
        K = self.split_heads(K)
        V = self.split_heads(V)

        # 计算注意力分数
        scores = torch.matmul(Q, K.transpose(-2, -1)) / torch.sqrt(torch.tensor(self.head_dim, dtype=torch.float32))

        # 应用mask (如果需要)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)

        # 计算注意力权重
        attention = F.softmax(scores, dim=-1)

        # 加权求和
        output = torch.matmul(attention, V)  # [batch_size, num_heads, seq_len, head_dim]

        # 合并多头
        batch_size, _, seq_len, _ = output.size()
        output = output.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)

        # 最终线性变换
        output = self.W_o(output)

        return output


class PositionwiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(0.1)

    def forward(self, x):
        # 两层全连接层，中间有ReLU激活和dropout
        return self.fc2(self.dropout(F.relu(self.fc1(x))))


class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.ffn = PositionwiseFeedForward(d_model, d_ff)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(0.1)
        self.dropout2 = nn.Dropout(0.1)

    def forward(self, x, mask=None):
        # 第一子层: 多头自注意力 + Add & Norm
        attn_output = self.self_attn(x, x, x, mask)
        x = x + self.dropout1(attn_output)
        x = self.norm1(x)

        # 第二子层: 前馈网络 + Add & Norm
        ffn_output = self.ffn(x)
        x = x + self.dropout2(ffn_output)
        x = self.norm2(x)

        return x
