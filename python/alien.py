class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words: return ''
        
        graph = {}
        # Construct graph.
        for pair in zip(words, words[1:]):
            word1, word2 = pair
            if word1 == word2:
                continue
            
            i = j = 0
            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:
                    if word1[i] not in graph:
                        graph[word1[i]] = []
                    graph[word1[i]].append(word2[j])
                    break
                i += 1
                j += 1
        
        order = []
        visited = {}
        
        def dfs(node):
            visited[node] = 1
            
            if node in graph:
                for adj in graph[node]:
                    if adj not in visited: 
                        if not dfs(adj):
                            return False

                    elif visited[adj] == 1:
                        return False
            visited[node] = 2
            order.append(node)
            return True

        for letter in set(''.join(words)):
            if letter not in visited:
                if not dfs(letter):
                    
                    order = []
                    break
        return ''.join(order[::-1])

sol = Solution()
print sol.alienOrder(["a","b","a"])