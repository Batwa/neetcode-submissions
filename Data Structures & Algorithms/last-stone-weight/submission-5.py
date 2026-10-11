class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = [-x for x in stones]
        heapq.heapify(a)
        while len(a)>1:
            y=heapq.heappop(a)
            x=heapq.heappop(a)
            if x!=y:
                heapq.heappush(a, y-x)
        if len(a)==1:
            return -a[0]
        return 0