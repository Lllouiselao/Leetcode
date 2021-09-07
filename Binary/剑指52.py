class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 二分法 i作为头 j作为尾
        start, end = 0, len(nums) - 1
        while start <= end:
            # 取中间值
            m = (start + end) // 2
            #当每个值都能对应 start 二分往后一位
            if nums[m] == m: 
                start = m + 1
            else: 
                #当二分对应不上 说明前半段出问题 end往前寻找
                end = m - 1
        return start