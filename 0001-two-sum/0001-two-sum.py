class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in di:
                return[di[diff],i]
            di[j]=i
        



        