#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> s_anagram; 
        std::unordered_map<char,int> t_anagram; 
        if (size(s)!=size(t)){
            return false; 
        }
        for(int i=0;i<size(s);i++){
            s_anagram[s[i]]+=1; 
            t_anagram[t[i]]+=1;
        }

        if(s_anagram==t_anagram){
            return true; 
        }
        return false; 

    }
};
