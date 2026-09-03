class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash={}

        for s in strs:
            s_sorted=''.join(sorted(s))
            if s_sorted in my_hash:
                my_hash[s_sorted].append(s)
            else: 
                my_hash[s_sorted]=[s]

        return list(my_hash.values())
