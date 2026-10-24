class Solution:
    def trap(self, height: List[int]) -> int:
        #we find the first left one and then we look for the next bar that's the same height or higher, and then we remember the lenght of the left one, and then for each number between the bar on the left and on the right, we do height of left minus height of the block and the result adds into the variable with 0 in the beginning which is amount of water trapped between, and after we did all of the differences, we add the result into the final variable that will be returned as overall amount, and then the left one jumps into the index of the right one (so left index becomes right index) and then it does the same algorithm as before but also checks if there's nothing the same height or higher, then it just add 0 to the final return 
        n = len(height)
        ans = 0
        left = 0

        # Pass 1: left to right. From each wall, find the next bar that is as tall or taller, and fill the water between.
        while left < n - 1:
            right = left + 1
            while right < n and height[right] < height[left]:
                right += 1
            if right == n:        # nothing as tall on the right: stop here
                break
            for x in range(left + 1, right):
                ans += height[left] - height[x]
            left = right          # the right wall becomes the new left wall
        # Pass 2: the leftover part, done the same way from the right side.
        r = n - 1
        while r > left:
            l = r - 1
            while l > left and height[l] < height[r]:
            #l>left gives us the last bar we accounted for in our pass 1, so we can work from right up until that point. also we check that height of l is smaller than r's because if it's higherm then we need to do separation 
                l -= 1
            for x in range(l + 1, r):
                ans += height[r] - height[x]
            r = l
        return ans





            
            