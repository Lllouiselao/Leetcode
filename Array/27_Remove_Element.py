class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = right = 0
        # 当快指针在历遍整个array时 慢指针等待
        # 当快指针发现 合适需要保留的 数 就替换给慢指针
        # 慢指针前进一位
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left +=1
        return left
