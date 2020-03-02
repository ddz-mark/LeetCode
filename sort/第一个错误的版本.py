# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分查找
        left, right = 0, n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left