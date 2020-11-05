# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

class Solution:
    def recursiveSearch(self, graph, path, current):
        path.append(current)
        if(current == len(graph)-1):
            nPath = list(path)
            path.pop()
            return nPath
        currentNode = graph[current]
        for i in currentNode:
            self.paths.append(self.recursiveSearch(graph, path, i))
        path.pop()
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        self.recursiveSearch(graph, [], 0)
        self.paths = [i for i in self.paths if i]
        return self.paths