class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(filter(str.isalnum, s)).lower()
        return x == x[::-1]