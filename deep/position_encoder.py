# -*- coding: utf-8 -*-
# @Time : 2025/5/26 00:03
# @Author : ddz


import numpy as np


def getPosEncodingMatrix(max_len, d_emb):
    # 思路：PE(pos,2i) = sin(pos/10000^(2i/d_model))
    # PE(pos,2i+1) = cos(pos/10000^(2i/d_model))
    # pos_enc: 生成一个形状为 (max_len, d_emb) 的矩阵，存储位置编码。
    pos_enc = []
    for pos in range(max_len):
        if pos != 0:
            pos_enc.append([pos / np.power(10000, 2 * (j // 2) / d_emb) for j in range(d_emb)])
        else:
            pos_enc.append(np.zeros(d_emb))

    print(pos_enc)
    # pos_enc[1:, ...]: 跳过 pos=0（因为 pos=0 已被设为全 0）。
    # 0::2: 所有偶数索引的维度（如 0, 2, 4,...）用 sin。
    # 1::2: 所有奇数索引的维度（如 1, 3, 5,...）用 cos。
    pos_enc[1:, 0::2] = np.sin(pos_enc[1:, 0::2])
    pos_enc[1:, 1::2] = np.cos(pos_enc[1:, 1::2])
    return pos_enc


a = getPosEncodingMatrix(15, 6)
