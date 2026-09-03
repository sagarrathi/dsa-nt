class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l= 0
        r= 1

        global_max=1
        my_set=set({s[l]})

        while r<len(s):
            if s[r] not in my_set:
                my_set.add(s[r])
                r+=1
                global_max=max(global_max, len(my_set))
            else:
                my_set.remove(s[l])
                l+=1

                
        
        return global_max
