"""
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

# Create a graph according to the dict and the start and end nodes, in which each node represents
# a word in the dict and the edge between two node means that these two
# word only differ in 1 letter.

# Solution: Start from the given node, do BFS to find all the path
# to end node.

# Difficulties: How to construct the graph? What data structure should we use to represent
# this graph? (Probably Adj-List, 'coz the graph is very likely to be sparse)

# Time complexity: Mostly in constructing the graph. O(n^2)

# MODIFIED: No need to construct the graph at first, we just pair the current node with the rest
# of the nodes to find its neighbors on the fly then push them into queue.

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # Queue for storing the nodes in the next level.
        current_level = []
        next_level = []
        
        visited = set([])

        # Result List
        res = [] 

        current_level.append(start)

        while current_level:
            current_node = current_level.pop()

            # First check if the end is reachable from this node.
            if self.isAdjacent(current_node, end):
                # If so, we don't need to visit the other nodes in the next level.
                # Just generate the path and continue to the next loop.
                
                continue
            else:




    # @param n1, a string
    # @param n2, a string
    # WHERE: len(n1) == len(n2)
    # Both strings are either in set(dict, start, end)
    def isAdjacent(self, n1, n2):
        diff_count = 0

        for i in range(0, len(n1)):
            if n1[i] != n2[i]:
                diff_count += 1
                
                if diff_count > 1:
                    return False

        return True

