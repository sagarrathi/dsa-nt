class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash={}
        my_freq=[]

        for n in nums:
            my_hash[n] = my_hash.get(n ,0)+1

         
        for key, val  in my_hash.items():
            my_freq.append([val, key]) 

        my_freq.sort()
        ans=[]

        print(my_freq)
        for _ in range(k):
            ans.append(my_freq.pop()[1])

        print(ans)
        return ans



