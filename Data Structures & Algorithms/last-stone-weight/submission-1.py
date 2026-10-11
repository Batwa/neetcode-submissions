class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a=[-x for x in stones]
        heapq.heapify(a)
        while len(a)>1:
            y=heapq.heappop(a)
            x=heapq.heappop(a)
            if x!=y:
                diff=y-x
                heapq.heappush(a,diff)
        if len(a)==0:
            return 0
        return -a[0]
