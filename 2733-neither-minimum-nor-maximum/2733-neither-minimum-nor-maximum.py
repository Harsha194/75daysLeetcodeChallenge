class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # sort
        nums.sort()
        # base case
        if len(nums)<=2:
            return -1
        return nums[1]
