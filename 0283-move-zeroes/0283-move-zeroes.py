class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res=[]
        zer=[]
        for x in nums:
            if x!=0:
                res.append(x)
        zer=[0]*(len(nums)-len(res))
        nums[:]=res+zer
        return nums

       
        