"""
Given that all the keys in linked list are unique

Input:  10->15->12->13->20->14,  x = 12, y = 20
Output: 10->15->20->13->12->14

1) x and y may or may not be adjacent.
2) Either x or y may be a head node.
3) Either x or y may be last node.
4) x and/or y may not be present in linked list.

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

    def swap(self, a, b):
        currX = None
        prevX = None
        currY = None
        prevY = None
        x = min(a, b)
        y = max(a,b)
        current = self.head

        if current.value == x:
            currX = current
            current = current.next

        while current.next:

            if currX is None and current.next.value == x:
                currX = current.next
                prevX = current
            elif current.next.value == y:
                currY = current.next
                prevY = current

            current = current.next


        if currX is not None and currY is not None:


            tempCurrX = currX
            tempNextX = currX.next
            tempCurrY = currY
            tempNextY = currY.next

            if prevX is None:
                self.head = tempCurrY
                self.head.next = tempNextX
            else:
                prevX.next = tempCurrY
                prevX.next.next = tempNextX

            prevY.next = tempCurrX
            prevY.next.next = tempNextY

            tempCurrX = None
            tempCurrY = None
            currX = None
            currY = None


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

"""swaps the elemets in linked list"""
linkedList.swap(12, 14)

print "prints linked list after swapping"
"""print linked list"""
linkedList.printLinkedList()
