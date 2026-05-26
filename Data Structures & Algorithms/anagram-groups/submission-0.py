class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)

        for i in strs:
            alphabet:List[int]=[0]*26
            for char in i:
                alphabet[ord(char)-ord('a')]+=1
            result[tuple(alphabet)].append(i)

        return list(result.values())







        



