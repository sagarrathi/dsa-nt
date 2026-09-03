class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_list={}
        for num in nums:
            if num in hash_list:
                return True
            else:
                hash_list[num] = 1
        return False