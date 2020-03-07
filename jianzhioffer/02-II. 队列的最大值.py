# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。
#
# 若队列为空，pop_front 和 max_value 需要返回 -1


class MaxQueue(object):

    def __init__(self):
        self.queue = []

    def max_value(self):
        """
        :rtype: int
        """
        if self.queue == []:
            return -1
        return max(self.queue)

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if self.queue == []:
            return -1

        return self.queue.pop(0)


if __name__ == '__main__':

    obj = MaxQueue()
    param_1 = obj.max_value()
    print(param_1)
    obj.push_back(4)
    param_3 = obj.pop_front()
    print(param_3)

    obj.push_back(5)
    obj.push_back(6)
    obj.push_back(7)
    param_4 = obj.max_value()
    print(param_4)

