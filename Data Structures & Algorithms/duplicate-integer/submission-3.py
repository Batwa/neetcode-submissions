class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for x in nums:
            s.add(x)
        return len(s)!=len(nums)