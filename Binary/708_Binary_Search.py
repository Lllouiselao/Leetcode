class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        # start 定在第一个位置 而 end 定在最后一个
        start , end = 0, len(nums) - 1
        # start +1 < end 可以保证不会因为last position = target&偶数list而进入死循环
        while start +1 < end:
            #//2 可以保证不因为偶数除法进入死循环
            mid = (start+end) //2
            
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                end = mid
        
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
            #如果list中没有这个target 
        else:
            return -1