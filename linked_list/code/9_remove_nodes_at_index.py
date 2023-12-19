# class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        position = 1
        while temp:
            print("Position: " + str(position) + " data: " + str(temp.data))
            temp = temp.next
            position += 1

    def RemoveNodesAtIndex(self, index):
        print("Remove nodes at index")
        # First, traverse and find the position at where data is supposed to be removed
        temp = self.head
        position = 1
        while(temp):
            if position == index:
                print("Position: " + str(position) + " data: " + str(temp.data))
                # 1. Next node has to be removed
                temp.next = temp.next.next
                break
            temp = temp.next
            position += 1

# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

ll = LinkedList()

# Define Node
node1 = Node(data=1)
node2 = Node(data=2)
node3 = Node(data=3)


ll.head = node1
ll.head.next = node2
ll.head.next.next = node3

print("traverse before remove nodes at index")
ll.traverse()
ll.RemoveNodesAtIndex(1)
print("traverse after remove nodes at index")
ll.traverse()

