class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # d = [[0, i] for i in range(26)]
        freq = {}
        for task in tasks:
            if task in freq: freq[task] += 1
            else: freq[task] = 1
        heap = []
        for letter in freq:
            heap.append((freq[letter], letter))

        heapq.heapify_max(heap)
        t = 0
        q = deque()
        
        while heap or q:
            if not heap:
                t = max(t, q[0][2])
                # t = q[0][2]
                task = q.popleft()[:2]
                heapq.heappush_max(heap, task)
                continue
            # else:
            task = heapq.heappop_max(heap)
            
            t += 1
            if task[0]-1 > 0:
                q.append((task[0]-1, task[1], t + n))

            if q and q[0][2] == t:
                task = q.popleft()[:2]
                heapq.heappush_max(heap, task)
        

        return t
