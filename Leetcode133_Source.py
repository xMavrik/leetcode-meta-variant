"""

133. Clone Graph

Given a reference to a disconnected, unidrected graph. return a deep copy

Graph contains a List[Node] of root nodes

Each node in the graph contains a value (int) and a List[Node] of its neighbors

Input: adjList = [[1,2,3],[4,5]]
Output: [[1,2],[2,1],[1,3],[3,1],[2,3],[3,2],[4,5],[5,4]]

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Graph:
    def __init__(self):
        self.roots: List[Node] = []


Beware: Meta may ask to define the classes yourself
"""

from typing import List, Dict, Set
from collections import deque
from typing import Dict, Optional, List

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Graph:
    def __init__(self):
        self.roots: List[Node] = []

# =====================================ADD YOUR CODE HERE=====================================
def clone_graph(roots: List[Node]) -> List[Node]:
    
    if not roots:
        return []

    clone = {}

    def bfs(start: Node):

        q = deque([start])
        clone[start] = Node(start.val)

        while q:
            current = q.popleft()
            for neighbor in current.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                clone[current].neighbors.append(clone[neighbor])

    for root in roots:
        if root not in clone:
            bfs(root)

    return [clone[root] for root in roots]


# 👇 Build graph from adjacency list input like [[1,2,3],[4,5]]
def build_graph(adj_list: List[List[int]]) -> List[Node]:
    val_to_node: Dict[int, Node] = {}

    for group in adj_list:
        if not group:
            continue
        node_val = group[0]
        if node_val not in val_to_node:
            val_to_node[node_val] = Node(node_val)
        node = val_to_node[node_val]
        for neighbor_val in group[1:]:
            if neighbor_val not in val_to_node:
                val_to_node[neighbor_val] = Node(neighbor_val)
            node.neighbors.append(val_to_node[neighbor_val])

    return [val_to_node[group[0]] for group in adj_list]

# 👇 Serialize graph to list of edges for easy comparison
def graph_to_edge_list(roots: List[Node]) -> List[List[int]]:
    seen: Set[str] = set()
    result = []

    def dfs(node: Node):
        for neighbor in node.neighbors:
            edge = (node.val, neighbor.val)
            if f"{edge}" not in seen:
                result.append([node.val, neighbor.val])
                seen.add(f"{edge}")
                seen.add(f"{(neighbor.val, node.val)}")  # avoid duplicate undirected edges
            if (neighbor.val, node.val) not in seen:
                dfs(neighbor)

    for root in roots:
        dfs(root)

    return sorted(result)

# ✅ Example input
adj_list = [[1,2,3],[4,5]]
original_roots = build_graph(adj_list)
cloned_roots = clone_graph(original_roots)

# 🧾 Print results
assert(graph_to_edge_list(original_roots) == graph_to_edge_list(cloned_roots))
print("Passed All Test Cases!")

