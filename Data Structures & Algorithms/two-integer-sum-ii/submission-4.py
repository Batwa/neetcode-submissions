class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        ans=[]
        while numbers[left]+numbers[right]!=target:
            if numbers[left]+numbers[right]>target:
                right-=1
                continue
            if numbers[left]+numbers[right]<target:
                left+=1
                continue
        ans.append(left+1)
        ans.append(right+1)
        return ans