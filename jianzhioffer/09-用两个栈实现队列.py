# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class CQueue(object):

    def __init__(self):
        self.stack = []


    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stack == []:
            return -1
        return self.stack.pop(0)



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()