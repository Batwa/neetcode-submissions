class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we check first and last, then append into list of areas, then we take the max out of two, and if the max is the left one, then we move right to -1, if the right one, then left +1, else left+1 and right -1, then we take the max out of the maxes
        best=0
        left,right=0, len(heights)-1
        while left<right:
            wdth=right-left
            lngth=min(heights[left], heights[right])
            area=wdth*lngth
            best=max(best,area)
            if max(heights[left], heights[right]) == heights[left]:
                right-=1
                continue
            if max(heights[left], heights[right]) == heights[right]:
                left+=1
                continue
            else:
                right-=1
                left+=1
                continue
        return best
