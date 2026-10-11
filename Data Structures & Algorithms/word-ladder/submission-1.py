class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)

        n = len(wordList)
        m = len(wordList[0])

        graph = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                a, b = wordList[i], wordList[j]
                for k in range(m):
                    if a[:k]+a[k+1:] == b[:k]+b[k+1:]:
                        graph[a].append(b)
                        graph[b].append(a)
                        break

        q = deque([beginWord])
        d = 1
        seen = set()
        

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return d
                for x in graph[word]:
                    if x not in seen:
                        q.append(x)
                        seen.add(x)
            d += 1
        return 0
