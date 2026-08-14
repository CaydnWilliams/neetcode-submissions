class Solution:
    def isPalindrome(self, s: str) -> bool:
        cant_use = {"!", "?", ".", "'", ",", " ", ":", ";"}
        newS = ''.join(ch for ch in s if ch not in cant_use).lower()
        return  newS == ''.join(reversed(newS))
        