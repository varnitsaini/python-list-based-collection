"""
Illustrating Singly Linked List implementation in Python
ADT for Linked List are
-appending ( added new node at the end of linked list )
-print all elements of linked list
-get the length of the linked list
-insert new element at the head of linked list
-check if a value exist in linked list
-deletes the node from the head
-deletes the node from desired index
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

    """Returns the length of the linked list"""
    def getLength(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next

        return counter

    """
    Inserts new node from the head

    Args:
        new_node: new node to be inserted from the head
    """
    def insertFromHead(self, new_node):
        current = self.head
        if current:
            new_node.next = current
            self.head = new_node

    """Returns the index of value if it exists in linked list else returns -1"""
    def searchValue(self, value):
        current = self.head
        counter = 0
        while current:
            if current.value == value:
                return counter
            current = current.next
            counter += 1

        return -1

    """
    Inserts new node at desired index
    Args:
        new_node: new node to be inserted
        index: index where new_node is to be inserted
    """
    def insertAtIndex(self, index, new_node):
        current = self.head
        counter = 0
        if index == 0:
            self.insertFromHead(new_node)
        else:
            while current:
                if counter + 1 == index:
                    new_node.next = current.next
                    current.next = new_node
                    return

                counter += 1
                current = current.next

    """delete the head node from the linked list"""
    def deleteFromHead(self):
        current = self.head
        self.head = current.next
        current.next = None

    def deleteFromIndex(self, index):
        current = self.head

        if index + 1 <= self.getLength():
            if index == 0:
                self.deleteFromHead()
            else:
                counter = 1
                while current:
                    if counter == index:
                        nodeToBeRemoved = current.next
                        current.next = nodeToBeRemoved.next
                        nodeToBeRemoved = None

                    counter += 1
                    current = current.next

"""Creating new nodes for the linked list"""
node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node(1)
node5 = Node(2)

"""initialising and appending new values to linked list"""
linkedList = LinkedList(node1)
linkedList.append(node2)
linkedList.append(node3)

"""print linked list"""
linkedList.printLinkedList()

"""print the length of linked list"""
print "length of linked list is"
print linkedList.getLength()

"""insert new node from the head"""
linkedList.insertFromHead(node4)
linkedList.printLinkedList()

"""search value at index if it exist else return -1"""
print "searched value at index: " + str(linkedList.searchValue('c'))

"""insert new node at desired index"""
print "inserts new node at index 4"
linkedList.insertAtIndex(2, node5)
linkedList.printLinkedList()

"""delete the node from the head"""
print "delete head node"
linkedList.deleteFromHead()
linkedList.printLinkedList()

"""delete the node at desired index"""
print "delete the node at index 2"
linkedList.deleteFromIndex(2)
linkedList.printLinkedList()