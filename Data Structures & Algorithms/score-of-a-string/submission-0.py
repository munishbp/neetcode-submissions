class Solution:
    def scoreOfString(self, s: str) -> int:
        res:int=0
        for i in range(len(s)-1):
            diff:int=ord(s[i])-ord(s[i+1])
            res+=abs(diff)

        return res

