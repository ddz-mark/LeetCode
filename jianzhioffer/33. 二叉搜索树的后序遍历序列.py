# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。
# 假设输入的数组的任意两个数字都互不相同。

# 思路：后序遍历递归处理，找到根结点，然后找到比 根结点 小的集合，和比 根结点 大的集合

class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """

        return self.judge(postorder, 0, len(postorder) - 1)

    def judge(self, postorder, i, j):

        # 递归：先写结束条件
        if i >= j:
            return True

        p = i
        while postorder[p] < postorder[j]:
            p += 1
        m = p
        while postorder[p] > postorder[j]:
            p += 1

        return p == j and self.judge(postorder, i, m - 1) and self.judge(postorder, m, j - 1)


if __name__ == '__main__':
    ob = Solution()
    print(ob.verifyPostorder([1,3,2,6,5]))
