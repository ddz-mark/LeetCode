# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#

class Solution:
    def isValidSudoku(self, board):
        # 思路三： 思路二的另一种实现方式。代码更为简洁（借鉴）
        Cell = [[] for i in range(9)]  # 没有必要用dict,我们只某个数字关心有没有出现过
        Col = [[] for i in range(9)]
        Row = [[] for i in range(9)]

        for i, row in enumerate(board):  # 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
            for j, num in enumerate(row):
                if num != '.':
                    k = (i // 3) * 3 + j // 3  # 利用地板除，向下取余。巧妙地将矩阵划分为九块
                    if num in Row[i] + Col[j] + Cell[k]:  # list的骚操作,将三个list顺序的拼接
                        return False
                    Row[i].append(num)
                    Col[j].append(num)
                    Cell[k].append(num)

        return True
