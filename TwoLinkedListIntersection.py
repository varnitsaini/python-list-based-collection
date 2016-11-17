"""
In this we will illustrate the intersection point of two Linked List

The procedure we will follow is:
Let there be two Linked list a and b

lenA = length of linked list a
lenB = length of linked list b

d = abs(lenA-lenB)      //get the absolute value of difference among the linked list

So among the Linked list a and b whichever is longer we will traverse
first d hops from the longer Linked List and then iterating in both
the Linked List equally
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

    def getHead(self):
        return self.head


def getIntersectionPoint(headA, headB, lenghtOfA, lenghtOfB):
    currentA = headA
    currentB = headB

    diff = abs(lenghtOfA - lenghtOfB)

    if lenghtOfA > lenghtOfB:
        while currentA and diff > 0:
            currentA = currentA.next
            diff -= 1
    elif lenghtOfB > lenghtOfA:
        while currentB and diff > 0:
            currentB = currentB.next
            diff -= 1

    while currentB and currentA:
        if currentB == currentA:
            print "Linked List intersect at address: " + str(currentA) + " and the value of intersection point is: " + str(currentA.value)
            break
        currentA = currentA.next
        currentB = currentB.next




"""Creating new nodes for the linked list"""
nodeA1 = Node('a')
nodeA2 = Node('b')
nodeB1 = Node('c')
node1 = Node(21)
node2 = Node('b')


"""initialising and appending new values to linked list"""
linkedListA = LinkedList(nodeA1)
linkedListA.append(nodeA2)
linkedListA.append(node1)

linkedListB = LinkedList(nodeB1)
linkedListB.append(node1)
linkedListB.append(node2)

lenghtOfA = linkedListA.getLength()
lenghtOfB = linkedListB.getLength()

getIntersectionPoint(linkedListA.getHead(), linkedListB.getHead(), lenghtOfA, lenghtOfB)