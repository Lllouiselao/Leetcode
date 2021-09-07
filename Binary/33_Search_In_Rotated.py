class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        #因为模板中用了 start +1 如果出现list only1 会报错
        # len = 1情况下只有一个值 那么只有存在在list 和不存在在list中两种可能性
        if len(nums) == 1:
            if nums[start] == target:
                return 0
            elif target not in nums:
                return -1

        #九章模板
        while start +1 < end:
            mid = (start + end ) //2
            #当mid >start 在升序列表中 [6, 7 , 8 , 1 , 2] 
            if nums[start] <= nums[mid]:
                #这里说明在左上的升序列表中 去掉右边 保留 [6, 7, 8]
                if nums[start] <= target <= nums[mid]:
                    end = mid
                    #如果start > target 而 mid > start :[6, 7 , 8 , 1 , 2] 
                    #我们需要保留 [8, 1, 2] 去掉左边 所以 start = mid
                else:
                    start = mid
            else:
                #当nums[mid] < nums[start] 而且 nums[mid] < target :[7, 8, 1, 2, 3]
                #当mid 1 小于target 2 小于 end 3 去掉左边
                if nums[mid] <= target <= nums[end]:
                    start = mid
                    #当nums[mid] < nums[start] 而nums[mid] > target: [8, 1, 2, 3, 4]
                else:
                    end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1