import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True) 
        heap = []
        count = 0
        
        max_day = max(end for _, end in events)
        
        for day in range(1, max_day + 1):

            while events and events[-1][0] == day:
                heapq.heappush(heap, events.pop()[1])
            
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                count += 1
        
        return count