class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = {}
        for task in tasks:
            if task in freq: freq[task] += 1
            else: freq[task] = 1
        
        heap = []
        for letter in freq:
            heapq.heappush_max(heap, freq[letter])

        q = deque()
        t = 0


        while heap or q:
            if not heap:
                t = q[0][1]
                heapq.heappush_max(heap, q.popleft()[0])
                continue
            
            t += 1
            task = heapq.heappop_max(heap)

            if task - 1 > 0:
                q.append((task-1, t + n))

            if q and q[0][1] == t:
                heapq.heappush_max(heap, q.popleft()[0])
        return t