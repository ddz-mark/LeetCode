# -*- coding: utf-8 -*-
# @Time : 2020/6/27 1:09 下午
# @Author : ddz
# 185 ?

# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路：dp
        # 1. 可以遍历每个数字 i，将该数字作为树根，1 ... (i-1) 序列将成为左子树，(i+1) ... n 序列将成为右子树。
        # G(n): 长度为n的序列的不同二叉搜索树个数
        # F(i,n): 以i为根的不同二叉搜索树个数(1 <= i <= n)
        # 2. G(n)= F(1,n)+F(2,n) +...+F(n,n)
        # 3. 当 i 为根节点时，其左子树节点个数为 i-1 个，右子树节点为 n-i，则有 F(i,n)=G(i−1)⋅G(n−i)
        # 则结合上面：G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]


if __name__ == '__main__':
    obj = Solution()
    print(obj.numTrees(3))
