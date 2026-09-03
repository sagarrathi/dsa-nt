class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums)) 
        local_val = 1
        max_val = 1

        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                local_val+=1
                max_val=max(local_val,max_val )
            else:
                local_val=1
        
        max_val=max(local_val,max_val )

        return max_val




        