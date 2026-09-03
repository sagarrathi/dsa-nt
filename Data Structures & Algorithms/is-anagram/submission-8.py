class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        abc={}
        for i in range(len(s)):
            l, r= s[i], t[i]

            if l not in abc:
                abc[l] = 1
            else: 
                abc[l] +=1
            
            if r not in abc:
                abc[r] = -1
            else: 
                abc[r] -=1
        
        for item in abc:
            if abc[item] != 0:
                return False
        return True
