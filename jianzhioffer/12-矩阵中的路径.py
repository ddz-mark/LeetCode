#
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，
# 每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
# 例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
#
# [["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
#
# 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

# 思路：使用递归处理，遍历矩阵，如果是第一个，然后检查它的上下左右，并且通过同型的 MASK 矩阵记录是否走过。

class Solution(object):

    def judge(self, matrix, rows, cols, i, j, word, mask_matirx):

        if not word:
            return True
        # 判断条件，如果越界或者不相等或者已经走过了
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] != word[0] or mask_matirx[i][j] == True:
            return False

        mask_matirx[i][j] = True

        # 检查上下左右是否存在路径
        if (self.judge(matrix, rows, cols, i - 1, j, word[1:], mask_matirx) or
                self.judge(matrix, rows, cols, i + 1, j, word[1:], mask_matirx) or
                self.judge(matrix, rows, cols, i, j - 1, word[1:], mask_matirx) or
                self.judge(matrix, rows, cols, i, j + 1, word[1:], mask_matirx)):
            return True

        # 第一个是，但是上下左右不是，则设置未走过
        mask_matirx[i][j] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows = len(board)  # 行数
        cols = len(board[0])  # 列数
        # memo = [[1] * m for i in range(n)]
        mask_matirx = [[False] * cols for _ in range(rows)]
        # print(mask_matirx)
        for i in range(rows):
            for j in range(cols):
                if self.judge(board, rows, cols, i, j, word, mask_matirx):
                    return True
        return False


if __name__ == '__main__':
    ob = Solution()
    print(ob.exist([["a","b"],["c","d"]], "abcd"))
