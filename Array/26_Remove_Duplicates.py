class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)

        #允许重复几次 就从第几次开始
        left = right = 1
        #right 指针历遍数组 left指针指向需要改变的index
        for right in range(len(nums)):
            #当right指针找到不同的数 与left 前一个 index进行对比
            if nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                # 改变内容后 left指向下一个需要改变的index
                left +=1 
        return left