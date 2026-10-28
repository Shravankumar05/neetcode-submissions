class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = {}

        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        
        res = ""
        for letter in order:
            if letter not in counts:
                continue
            else:
                res += letter * counts[letter]
                counts[letter] = 0
        
        for key, value in counts.items():
            res += key * value
        
        return res