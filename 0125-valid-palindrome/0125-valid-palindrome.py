class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
        for i in range(len(clean)//2):
            if clean[i] != clean[len(clean)-1-i]:
                return False
        return True
        