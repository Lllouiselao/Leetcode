class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0, len(nums) - 1

        #考虑到只有两个数的情况 这里改成 <=
        while start + 1 <= end:
            mid = (start + end) //2

            #判断mid在升序/降序 因为有端值情况 不能之和 mid+1进行比较
            #若end比mid 大 则 最小一定在左侧
            if nums[mid] < nums[end]:
                end = mid
            #若mid比端值大 则 最小一定在右侧 最后返回头值
            elif nums[mid] > nums[end]:
                start = mid +1
            
        return nums[start]