class Node: # assuming binary tree
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive approach
def dft(node, out):
    out.append(node.val)
    if node.left:
        dft(node.left, out)
    if node.right:
        dft(node.right, out)

# iterative approach
def dft_Iterative(node, out):
    stack = []
    stack.append(node)
    while stack:
        curr = stack.pop()
        out.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
