"""
Following tutorial reverses the linked list. Eg
10->15->12->13->20->40
will result into
40->20->13->12->15->10
"""

"""
Creates new Node

Args:
    value: desired value in the node

Returns:
    object for the Node
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""
Linked List class
"""
class LinkedList(object):

    """
    Constructor creates the head element for our new linked list

    Args:
        head: head element for the linked list
    """
    def __init__(self, head):
        self.head = head

    """
    appends new value at the end of the list

    Args:
        new_node: new node to be appended at the end of the list

    Returns:
        None
    """
    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

        return None


    """Prints the linked list starting form the head all the way to end"""
    def printLinkedList(self):
        current = self.head
        counter = 0
        while current:
            print "value of node " + str(counter) + " is " + str(current.value)
            current = current.next
            counter += 1

    def reverseLinkedList(self):
        current = self.head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

"""Creating new nodes for the linked list"""
node1 = Node(10)
node2 = Node(15)
node3 = Node(12)
node4 = Node(13)
node5 = Node(20)
node6 = Node(14)

"""initialising and appending new values to linked list"""
linkedList = LinkedList(node1)
linkedList.append(node2)
linkedList.append(node3)
linkedList.append(node4)
linkedList.append(node5)
linkedList.append(node6)

"""print linked list"""
linkedList.printLinkedList()

"""following function call will reverse the linked list"""
linkedList.reverseLinkedList()


print "linked list after reversing is"

"""print linked list"""
linkedList.printLinkedList()