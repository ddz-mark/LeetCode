# -*- coding: utf-8 -*-
# @Time : 2020/5/22 10:50 下午
# @Author : ddz
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]

import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 思路一：对字典按值降序排序
        # dic = (dict(sorted(dict(collections.Counter(nums)).items(), key=lambda kv: (-kv[1]))))
        # res = []
        # for i in range(0, k):
        #     res.append(list(dic.keys())[i])
        #
        # return res

        # 思路二：
        # 创建优先队列 　维护一个大小为k的最小堆，使得堆中的元素即为前k个高频元素
        # heapq.heappush(heap,item)  # heap为定义堆，item 增加的元素
        # heapq.heappop(heap)        # 删除最小的值
        # heapq.heapreplace(heap, item)     #删除最小元素值，添加新的元素值
        pq = []
        dic = collections.Counter(nums)
        for key, value in dic.items():
            # 如果 堆的大小小于 k，就入堆
            if len(pq) < k:
                heapq.heappush(pq, (value, key))
            # 最小堆
            elif value > pq[0][0]:
                heapq.heapreplace(pq, (value, key))
        res = []
        while pq:
            res.append(heapq.heappop(pq)[1])
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
