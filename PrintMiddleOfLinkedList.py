"""
To prine middle element in the list we will take two pointers
for each iteration one hop will travel one hop whereas other pointer
will travel two hops.

So till the time pointer with two hops reaches the end our single hop
pointer will reach to the middle element

In case number of values are even the middle elements will be two
and in case number of input values are odd the middle elmenet will be single
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

    def printMiddleElement(self):
        singleHop = self.head
        doubleHop = self.head
        evenValue = False

        while doubleHop:

            if doubleHop.next == None:
                break
            if doubleHop.next.next:
                doubleHop = doubleHop.next.next
                singleHop = singleHop.next
            elif doubleHop.next:
                evenValue = True
                doubleHop = doubleHop.next

        if evenValue == True:
            return (singleHop.value, singleHop.next.value)
        else:
            return str(singleHop.value)


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

print "middle element is " + str(linkedList.printMiddleElement())