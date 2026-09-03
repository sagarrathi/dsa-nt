class Solution:
    def twoSum(self, nums: List[int], target) -> List[int]:
        n= len(nums)
        l=0
        r=n-1
        res = []
        
        while l < r:
            current_sum = nums[l] + nums[r]
            if current_sum == target:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        return res

        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans=set()

        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            target=-nums[i]
            pairs=self.twoSum(nums[i+1:], target)
        
            for pair in pairs:
                ans.add(tuple([nums[i], *pair]))

        return list(ans)