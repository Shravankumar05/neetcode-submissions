class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join([char for char in s if char.isalnum()]).lower()
        return x[::-1] == x