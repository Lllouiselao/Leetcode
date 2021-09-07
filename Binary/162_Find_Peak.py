class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start , end = 0, len(nums) -1

        #考虑数列只有两个值的可能性 不能start + 1 < 而需要<=
        while start + 1 <= end:
            mid = (start + end) //2

            #如果mid停留在一个升序数列当中 那么start = mid+1
            #如果 start = mid 第二轮并不会减少一半 从而进入死循环
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            #如果mid 停留在 降序数列当中 那么end = mid 减少右半边的数组
            elif nums[mid] > nums[mid+1]:
                end = mid
            else:
                end = mid
        return start