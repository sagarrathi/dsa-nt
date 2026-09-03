class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        n_dict={}
        for n in nums:
            if n in n_dict:
                n_dict[n]+=1
            else:
                n_dict[n]=1
    
        sorted_keys = sorted(n_dict.keys(), key=lambda k: n_dict[k])

        return sorted_keys[-k:]
