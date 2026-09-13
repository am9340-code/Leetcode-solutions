class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        for char in s:
            if char in seen_s:
                seen_s[char] = seen_s[char] + 1
            else:
                seen_s[char] = 1
        for char in t:
            if char in seen_t:
                seen_t[char] = seen_t[char] + 1
            else:
                seen_t[char] = 1
        if seen_s == seen_t:
            return True
        else:
            return False
