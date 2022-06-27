class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1=0
        new_sum=[]
        for i in range(len(nums)):
            sum1+=nums[i]
            new_sum.append(sum1)
        return new_sum