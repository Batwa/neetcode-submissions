class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        ans=[]
        if nums[0]>0:
            return []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            left,right=i+1,len(nums)-1
            while left<right:
                total=nums[left]+nums[right]
                if total - target>0:
                    right-=1
                    continue
                if total - target<0:
                    left+=1
                    continue
                if total-target==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans
        
