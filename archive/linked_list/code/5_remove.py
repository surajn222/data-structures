
# Define a LinkedList class with one variable, Node, Head assigned as None
# LinkedList(head)
class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def removeLastNode(self):
        temp = self.head        # Node 1

        # Ideally,
        # head                  -> node1.next               -> node2.next               -> node3.next(None)
        #                                                                                   1. we have to elimiat this node
        #                                                 2. We have to set this node.next to None
        # Traverse ->>>                                                                     when we reach this node, and realise that it is last, we cannot go back to Node2 to set Next as none
        # Traverse ->>>                                     when we reach this node, we have to check if next of next node is None, so we know that this has to be last
        # Traverse ->>>                                     when we reach this node, check if node.next.next == None
        # Traverse ->>>                                     In other words, stop only when node.next.next == None, and assign node.next as None, else keep going
        # Traverse ->>>                                     In other words, stop only when node.next.next exists, keep going, else assign node.next as None, since the one after this is last, and we need to remove it

        while(temp.next.next):
            temp = temp.next
        temp.next = None

# Define a Node Class with two variables, data and next. Data as input and next as None
# Node(data=input, next=None)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a new node object, assign some data and assign next as None
# node1 = Node(data=1, next=None)
node1 = Node(data=1)


# Create a Linkedlist object.
ll = LinkedList()

# The above node object should be assigned to Head
# head = node1
ll.head = node1


# Traverse to last but one node
node2 = Node(data=2)
ll.head.next = node2

ll.traverse()
ll.removeLastNode()
ll.traverse()


