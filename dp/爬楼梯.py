# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶

# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

# 思路：只需要知道 n-1 阶和 n-2 阶有多少种爬法就可以了（第 n 阶台阶，无非是通过 n-1 或 n-2 阶台阶爬上去的）
# 实则是斐波拉切数列的翻版
class Solution:
    def climbStairs(self, n: int) -> int:
        climb = dict()
        climb[0], climb[1] = 1, 1
        for i in range(2, n+1):
            climb[i] = climb[i - 1] + climb[i - 2]
            print(climb[i], i)

        return climb[n]

if __name__ == '__main__':
    solution = Solution()
    solution.climbStairs(5)