class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        my_hash = {}

        for i in range(len(s)):
            s_val=s[i]
            t_val=t[i]
            my_hash[s_val] = my_hash.get(s_val, 0) +1
            my_hash[t_val] = my_hash.get(t_val, 0) -1

        
        return all(count == 0 for count in my_hash.values())

        