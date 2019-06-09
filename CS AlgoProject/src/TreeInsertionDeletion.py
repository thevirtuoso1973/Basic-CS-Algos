class Node: # assuming binary tree
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val): # inserts it into correct position
    if val <= root.val:
        if root.left:
            insert(root.left)
        else:
            root.left = Node(val)
    else:
        if root.right:
            insert(root.right)
        else:
            root.right = Node(val)

def delete(root, val): # # TODO: add deletion algorithm
    pass
