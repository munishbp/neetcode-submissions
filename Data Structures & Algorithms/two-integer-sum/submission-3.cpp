#import <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //diff, index
        std::unordered_map<int,int> two_sum;

        for (int i=0;i<size(nums);i++){
            int diff=target-nums[i]; 

        

            

            if(two_sum.find(diff)!=two_sum.end()){
                return {two_sum[diff],i}; 
            }

            two_sum[nums[i]]=i; 
        }
    }
};
