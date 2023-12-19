# Define LinkedList(head)
class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def update(self, index, data):
        temp = self.head
        position = 1
        while(temp):
            if position == index:
                print("Index found " + str(index))
                temp.data = data
            temp = temp.next
            position += 1

# Node(data = input, next = None)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# node1 = Node(data=1, next=None)
node1 = Node(data=1)


# Linkedlist(head)
ll = LinkedList()
ll.head = node1

# head = node1
ll.traverse()
ll.update(1, 10)
ll.traverse()
