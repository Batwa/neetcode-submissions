class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ap=[]
        count=1
        l=1
        if len(nums)==0:
            return 0          
        for x in s:                 
            if x - 1 not in s:      
                while  x+l in s:
                    count+=1
                    l+=1
            ap.append(count)
            l=1
            count=1
        return max(ap)
