# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #这里不是一个list 有多少数就多少数 所以end = n 而不是 n-1
        start , end = 0, n

        #防止进入一个偶数死循环 并且recursion 二分
        while start + 1 < end:
            mid = (start + end) // 2
            #当mid = target/mid > target 那么继续寻找左边是不是还有第一个 没有的话就return end
            if isBadVersion(mid):
                end = mid
            #当mid <target 那么把mid变成开头 继续寻找历遍右边(进行recursion)
            else:
                start = mid
            #因为在 start+1 < end情况下停止 如果[0,1] 1的情况下 return end 
        return end