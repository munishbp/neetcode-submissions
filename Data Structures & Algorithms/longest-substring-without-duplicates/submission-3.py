class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1: 
            return len(s)


        visited=[False]*128
        l,r=0,0
        result=0
        while r < (len(s)):

            while(visited[ord(s[r])-ord('a')])==True:
                visited[ord(s[l])-ord('a')]=False
                l+=1

            visited[ord(s[r])-ord('a')]=True
            result=max(result,r-l+1)
            r+=1
        print(r)
        print(l)
        return result
        