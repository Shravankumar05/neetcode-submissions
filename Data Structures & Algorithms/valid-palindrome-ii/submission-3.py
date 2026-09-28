class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                # skip left and check
                # skip right and check
                curr_l = s[left + 1 : right + 1]
                curr_r = s[left:right]
                if curr_l != curr_l[::-1] and curr_r != curr_r[::-1]:
                    return False
                else:
                    return True

            left += 1
            right -= 1

        return True
