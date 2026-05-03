class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
    
        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                
        return prefix
        



        #**************Brute Force****************
        # prefix = ""
    
        # for i in range(len(strs[0])):
        #     for x in strs:
        #         if i==len(x) or strs[0][i] != x[i]:
        #             return prefix
        #     prefix += strs[0][i]  # all words matched at position i
        
        # return prefix