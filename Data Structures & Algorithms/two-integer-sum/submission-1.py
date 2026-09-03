class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash={}

        for i in range(len(nums)):
            num = nums[i]
            diff= target - num
            if diff in my_hash:
                j = my_hash[diff]
                return [j, i]
            else:
                my_hash[num]=i
        
        print(my_hash)
        return []
        
        