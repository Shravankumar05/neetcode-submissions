class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = {}
        if len(s1) > len(s2):
            return False

        for letter in s1:
            if letter in x:
                x[letter] += 1
            else:
                x[letter] = 1
        
        n = len(s1)
        m = len(s2)
        i = 0
        curr = {}

        while i < n:
            if s2[i] in curr:
                curr[s2[i]] += 1
            else:
                curr[s2[i]] = 1
            i += 1
        
        if curr == x:
            return True

        left = 0
        right = n

        while right < m:
            outgoing = s2[left]
            curr[outgoing] -= 1

            if curr[outgoing] == 0:
                del curr[outgoing]

            incoming = s2[right]
            curr[incoming] = curr.get(incoming, 0) + 1

            if curr == x:
                return True

            left += 1
            right += 1

        return False