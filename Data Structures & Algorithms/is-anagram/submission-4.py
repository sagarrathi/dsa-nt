class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        my_hash = {}

        for i in range(len(s)):
            s_val=s[i]
            my_hash[s_val] = my_hash.get(s_val, 0) +1

        for i in range(len(t)):
            t_val=t[i]
            if t_val in my_hash:
                my_hash[t_val]-=1
                if my_hash[t_val]<0:
                    return False
            else:
                return False
                        
        return True
