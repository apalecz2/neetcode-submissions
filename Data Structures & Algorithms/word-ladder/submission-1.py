from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # process each word and hash words 1 different than a given word
        # bfs on these

        if endWord not in wordList:
            return 0


        wordList.append(beginWord)

        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)


        q = deque([])

        q.append(beginWord)

        length = 1

        visited = set([beginWord])

        while q:

            for _ in range(len(q)):

                word = q.popleft()

                if word == endWord:
                    return length

                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

            length += 1
            
        return 0


        

        
            