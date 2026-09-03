class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        older_dict={}

        for i in nums:
            if i in older_dict:
                return True
            else:
                older_dict[i]=1
        return False
            

