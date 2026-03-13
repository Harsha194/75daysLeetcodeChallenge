class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for k,v in enumerate(nums):
            diff=target-v
            if diff in di:
                return[di[diff],k]
            di[v]=k
        



        