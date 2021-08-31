class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #用python 切片 因为nums1 已经有足够的空间插入nums2
        #把nums2 直接插入在 m之后
        # 用自带的sort 进行sort
        nums1[m:] = nums2
        nums1.sort()
