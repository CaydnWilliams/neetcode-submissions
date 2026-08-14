class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        char_of_s = sorted(list(s))
        char_of_t = sorted(list(t))
        for i in range(len(s)) :
            if char_of_s[i] != char_of_t[i] :
                return False
        return True