class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter={}
        for i in range(len(nums)):
            if counter.get(nums[i]):
                return True

            counter[nums[i]]=1
            
        
        return False 




        