class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
            
        words = set(wordList)
        if beginWord not in words:
            words.add(beginWord)

        m = len(wordList[0])

        g = defaultdict(list)
        
        for word in words:
            for i in range(m):
                g[word[:i]+"*"+word[i+1:]].append(word)

        q = deque([beginWord])
        d = 1
        seen = set()
        

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return d

                for i in range(m):
                    pattern = word[:i]+"*"+word[i+1:]
                    if pattern not in seen:
                        q.extend(g[pattern])
                        seen.add(pattern)
 
            d += 1
        return 0
