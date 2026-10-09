class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in x:
                x[sorted_word].append(word)
            else:
                x[sorted_word] = [word]
        
        res = []
        for key, words in x.items():
            curr = []
            for word in words:
                curr.append(word)
            res.append(curr)
        
        return res