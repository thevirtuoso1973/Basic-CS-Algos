#Implementation of a linked list in python:

# a node of the list:
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        #self.prev = None (<--- If doubly-linked list)

# the list itself (consists of nodes)
class LinkedList:
    def __init__(self, headVal):
        self.head = Node(headVal)
        #self.tail = etc..
