class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_hash={}
        res=0

        l=0
        for r in range(len(s)):
            my_hash[s[r]] = 1 + my_hash.get(s[r], 0)

            while (r - l + 1) - max(my_hash.values()) >k:
                my_hash[s[l]]-=1
                l +=1

            res = max(res, r-l+1)
        return res