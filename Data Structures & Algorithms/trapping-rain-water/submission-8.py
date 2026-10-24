class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0;
        left,right=0,len(height)-1
        leftmax,rightmax=height[left],height[right]
        ans=0
        while left<right:
            if leftmax<rightmax:
                left+=1
                leftmax=max(leftmax,height[left])
                ans+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax,height[right])
                ans+=rightmax-height[right]
        return ans





            
            