class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, second = [], []

        l, r = 0, len(s) - 1

        while r >= 0 and l < len(s):
            if ord('a') <= ord(s[l].lower()) <= ord('z') or ord('0') <= ord(s[l].lower()) <= ord('9'):
                first.append(s[l].lower())
            if ord('a') <= ord(s[r].lower()) <= ord('z') or ord('0') <= ord(s[r].lower()) <= ord('9'):
                second.append(s[r].lower())
            l += 1
            r -= 1

        return first == second