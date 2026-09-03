class Solution:
    def cal_vol(self, h1, h2, d):
        return min(h1, h2) * d

    def maxArea(self, heights: List[int]) -> int:
        
        l, r =  0, len(heights)-1
        max_vol = 0

        while l < r:
            vol = self.cal_vol(heights[l], heights[r], r-l)
            max_vol = max(vol, max_vol)

            if heights[l] < heights[r]:
                l+=1 
            else:
                r-=1

        return max_vol
