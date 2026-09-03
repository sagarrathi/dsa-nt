class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}

        for n in nums:
            if not n in dic:
                dic[n] =1
            else:
                return True
        return False

        