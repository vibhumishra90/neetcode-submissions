class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''.join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(c) - 1
        while left < right:
            if c[left] != c[right]:
                return False
            left += 1
            right -= 1
        return True
