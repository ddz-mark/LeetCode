# -*- coding: utf-8 -*-
# @Time : 2020/5/23 5:04 下午
# @Author : ddz

# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
# 编写一个算法来重建这个队列。
#
# 注意：
# 总人数少于1100人。
#
# 示例
#
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 第一个值降序，第二个值升序
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []

        # 因为大的值，是看不到比它小的值的，
        # 所以先将大的值排序，然后插入到 res 中，小的下标就是对应的 第二个值
        # （因为小的插入队列时，之前的都比它大，所以只需要关注自己前面有几个数就可以了）
        for v in people:
            res.insert(v[1], v)

        return res


if __name__ == '__main__':
    ob = Solution()
    ob.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
