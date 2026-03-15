class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx=abs(num)-1
            nums[idx]=-abs(nums[idx])
        return[i+1 for i,j in enumerate(nums)if j>0]
        