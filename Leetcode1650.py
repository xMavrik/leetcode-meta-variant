'''

1650. LCA III


Given two nodes of a binary tree p and q as well as a list of all nodes in the tree nodes where nodes is unordered, return their lowest common ancestor (LCA).


'''

import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node2 = Node(2)
node4 = Node(4)
node1 = Node(1)
node3 = Node(3)
node6 = Node(6)
node5 = Node(5)
node7 = Node(7)

node2.left = node5
node2.right = node4

node5.left = node1
node5.right = node3

node1.left = None
node1.right = None

node3.left = None
node3.right = node7

node4.left = node6
node4.right


nodes = [node2, node5, node4, node1, node3, node6, node7]


def lca(nodeList, p, q):

    child_to_parent = {}


    for node in nodeList:
        if node.left:
            child_to_parent[node.left] = node
        if node.right:
            child_to_parent[node.right] = node


    racer_p = p

    racer_q = q

    while racer_p != racer_q:

        if racer_p not in child_to_parent:
            racer_p = q

        else:
            racer_p = child_to_parent[racer_p]

        
        if racer_q not in child_to_parent:
            racer_q = p
        else:
            racer_q = child_to_parent[racer_q]

    return racer_p.val


print(lca(nodes, node5, node7))