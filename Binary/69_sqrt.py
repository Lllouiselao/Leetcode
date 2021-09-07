class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        #最后一个 等于 target的数
        while left <= right:
            mid = (left + right ) //2
            if left == right or left + 1 == right:
                break
            elif mid * mid <= x:
                left = mid
            elif mid * mid > x:
                right = mid -1
        
        #退出循环之后做寻找
        if right * right <= x:
            return right
        else:
            return left