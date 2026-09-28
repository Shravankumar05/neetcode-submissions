class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(i)
            else:
                anagrams[sorted_word] = [i]
        
        res = []
        for key, values in anagrams.items():
            curr = []
            for i in values:
                curr.append(strs[i])
            res.append(curr)
        
        return res