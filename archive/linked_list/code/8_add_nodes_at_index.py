# Define class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next # If this is None, while loop will not run again

    def AddNodesAtIndex(self, data, index):
        print("Add nodes at index")
        node_temp = Node(data=data)
        temp = self.head
        position = 1
        # First, traverse and find the position at where data is supposed to be added
        while(temp):
            if position == index:
                print("position is index")
                print(temp.data)
                # current next node == next(new_node)
                node_temp.next = temp.next
                # Now, new node == current node, hence next(temp)
                temp.next = node_temp
                break

            position += 1
            temp = temp.next


# Define a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define object LinkedList
ll = LinkedList()


# Define node1
node1 = Node(data=1)

# Define node2
node2 = Node(data=2)
node3 = Node(data=3)

# Assign nodes
ll.head = node1
ll.head.next = node2
ll.head.next.next = node3

# Define traverse function, make it traverse
ll.traverse()

ll.AddNodesAtIndex(data=22, index=2)

print("traverse")
ll.traverse()