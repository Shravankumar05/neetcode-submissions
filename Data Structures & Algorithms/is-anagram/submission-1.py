class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}

        if len(s) > len(t):
            t, s = s, t

        for letter in s:
            if letter in word1:
                word1[letter] += 1
            else:
                word1[letter] = 1
        
        for letter in t:
            if letter in word1:
                word1[letter] -= 1
                if word1[letter] < 0:
                    return False
            else:
                return False
        
        return True