class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start , end = 0, len(nums)-1

        while start +1 < end:
            mid = (start + end) //2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid 
            else:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        if target not in nums:
            #当target小于start 返回的应该是start
            if target < nums[start]:
                return start
            elif target > nums[end]:
                return end+1
            elif target < nums[end]:
                return end
