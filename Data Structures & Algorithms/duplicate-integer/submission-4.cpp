#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> dups; 
        for (int i=0; i<size(nums);i++){
            int search_value=nums[i]; 

            if(dups.find(search_value)!=dups.end()){
                return true; 
            }

            else{
                dups[nums[i]]=1; 
            }
        }

        return false; 
    }; 
};