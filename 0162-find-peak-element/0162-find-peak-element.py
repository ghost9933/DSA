class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], l: int, r: int) -> int:
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, l, mid)
        return self.search(nums, mid + 1, r)