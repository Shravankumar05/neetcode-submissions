
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        count_s = {}
        left = 0
        have = 0
        need = len(count_t)

        best = ""
        min_len = float("inf")

        for right in range(len(s)):
            c = s[right]
            count_s[c] = count_s.get(c, 0) + 1

            if c in count_t and count_s[c] == count_t[c]:
                have += 1

            while have == need:
                length = right - left + 1

                if length < min_len:
                    min_len = length
                    best = s[left:right + 1]

                left_char = s[left]
                count_s[left_char] -= 1

                if (left_char in count_t and
                        count_s[left_char] < count_t[left_char]):
                    have -= 1

                left += 1

        return best