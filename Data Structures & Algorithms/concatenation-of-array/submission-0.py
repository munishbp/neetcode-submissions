class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans:List[int]=[]
        n:int=len(nums)
        j=0
        for i in range(2*n):
            if i<n:
                ans.append(nums[i]) 
            else:
                ans.append(nums[j])
                j+=1

        return ans    