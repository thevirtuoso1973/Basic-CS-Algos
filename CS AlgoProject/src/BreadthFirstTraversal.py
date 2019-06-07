class Node: # assuming binary tree
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bft(node, out): # uses a queue (FIFO)
    q = []
    q.append(node)
    while stack:
        curr = q.pop(0)
        out.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
