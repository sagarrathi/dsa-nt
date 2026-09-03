from collections import Counter
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        win_size=len(t)
        l=0
        r=0
        
        need_template = Counter(t)
        need = need_template.copy()
        max_vals=[]

        while r < len(s):
            char= s[r]

            if char in need:
                need[char]-=1


                while all(v <= 0 for v in need.values()):
                    max_vals.append(s[l:r+1])

                    if s[l] in need_template:
                        need[s[l]]+=1
                    
                    l+=1
            r+=1
        
        if not max_vals:
            return ""
        else:
            return min(max_vals, key=len)

                    





        

        
        