class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        #因为这是一个sorted array 我们可以直接从index2开始算
        #1） nums[2]仍旧重复 [1, 1, 1, 2] left指向第三个1 之后进行改变
        #2） nums[2]不重复 [1,1,2,2] left指向第一个2 改变
        left = 2
        for right in range(2, len(nums)):
            if nums[right] != nums[left -2]:
                nums[left] = nums[right]
                left +=1

        return left