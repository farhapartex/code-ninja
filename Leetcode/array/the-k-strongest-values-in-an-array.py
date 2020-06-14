import heapq

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        heap = []
        arr = sorted(arr)
        median = arr[(len(arr)-1)//2]
        
        for n in arr:
            heapq.heappush(heap, (abs(median-n),n))
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [item[1] for item in heap]
        