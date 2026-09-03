class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n_set= set(nums)
        all_seq=[]

        for i in range(len(nums)):
            val=nums[i]

            if val-1 not in n_set:
                seq=[val]
                while val+1 in n_set:
                    val+=1
                    seq.append(val)

                all_seq.append(seq)
                seq=[]

        return max(len(ar)  for ar in all_seq ) | 0

            