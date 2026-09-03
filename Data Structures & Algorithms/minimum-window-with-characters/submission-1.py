from collections import Counter
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        win_size=len(t)
        l=0
        r=0
        
        need_template = Counter(t)
        need = Counter()
        have=0
        need_count= len(need_template)
        res=""
        res_lenght=float('inf')
        
        while r < len(s):
            char= s[r]

            if char in need_template:
                need[char]+=1
                if need[char] == need_template[char]: 
                    have+=1

                while have == need_count:

                    if(r-l+1)< res_lenght:
                        res=s[l:r+1]
                        res_lenght = r-l+1
                        
                    if s[l] in need_template:
                        if need[s[l]] == need_template[s[l]]:
                            have-=1
                        need[s[l]]-=1

                    l+=1
            r+=1
        
        return res            





        

        
        