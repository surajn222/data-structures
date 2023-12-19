# Define a Node with two variables - data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a LinkedList class with one variable which is the node, head assigned as None
class LinkedList:
    def __init__(self):
        self.head = None