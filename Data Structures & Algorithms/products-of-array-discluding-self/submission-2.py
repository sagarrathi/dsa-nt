class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zero_id=[]
        zero_ids=0

        for i, n in enumerate(nums):
            if n:
                prod*=n
            else:
                zero_id.append(i)
                zero_ids+=1

        print(zero_id, zero_ids)
        
        if zero_ids == len(nums):
            prod=0
        ans=[]
        for i, n in enumerate(nums):
            if zero_ids>=2:
                val=0
        
            elif zero_ids ==1:
                if i in zero_id:
                    val=prod
                else:
                    val=0
            else:
                val=int(prod/n)

            ans.append(val)
        
        return ans


        