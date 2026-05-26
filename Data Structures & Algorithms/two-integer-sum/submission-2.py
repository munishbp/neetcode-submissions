class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        solution=[]
        for i in range(len(nums)):
            difference=target-nums[i]
            
            if (difference in hashmap) and (hashmap[difference]!=i):
                if hashmap[difference]<i:
                    solution.append(hashmap[difference])
                    solution.append(i)
                else:
                    solution.append(i)
                    solution.append(hashmap[difference])
                return solution
            hashmap[nums[i]]=i

        