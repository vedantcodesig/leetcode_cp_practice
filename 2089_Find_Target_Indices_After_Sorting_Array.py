class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sn=sorted(nums)
        sn1=[]
        for i in range(len(sn)):
            if sn[i]==target:
                sn1.append(i)
        return sorted(sn1)        
        