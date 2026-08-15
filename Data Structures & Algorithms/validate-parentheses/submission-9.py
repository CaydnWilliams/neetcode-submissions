class Solution:
    def isValid(self, s: str) -> bool:
        corresponding = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        if len(s) <= 1 :
            return False
        for i in range(len(s)) :
            if s[i] in corresponding.values() :
                stack.append(s[i])
            elif s[i] in corresponding  :
                if len(stack) > 0 :
                    check = stack.pop()
                    if check == corresponding[s[i]] :
                        continue
                    else :
                        return False
                else :
                    return False
        if len(stack) == 0 :
            return True
        else :
            return False 
          
