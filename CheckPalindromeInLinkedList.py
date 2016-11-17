"""
This will illustrates if a gives linked list is palindrome or not

There are basically two ways of checking a Palindrome in a Linked List
These are :
1) Traverse the Linked List and push each element into stack(array).
   Then traverse the whole Linked List again and compare each element
   of array with the element from the linked list and pop that element
   from the stack. If any mismatch occurs then Linked List is not palindrome

2) Reverse a linked List and compare the original linked list with the
   the reversed linked list. If any mismatch occurs then the Linked List
   is not palindrome

In this example we will go with the first choice of pushing elements into
a stack and then comparing the values.
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

    def checkIfPalindrome(self):
        current = self.head
        compareStack = []
        isPalindrome = True
        if current:
            while current:
                compareStack.append(current.value)
                current = current.next

            current = self.head
            while current:
                if current.value != compareStack.pop():
                    isPalindrome = False
                    break
                current = current.next

            if isPalindrome is True:
                print "Given Linked List is Palindrome"
            else:
                print "Given Linked List is Not Palindrome"
        else:
            print "Linked List is Empty"



"""Creating new nodes for the linked list"""
node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('c')
node5 = Node('b')
node6 = Node('a')

"""initialising and appending new values to linked list"""
linkedList = LinkedList(node1)
linkedList.append(node2)
linkedList.append(node3)
linkedList.append(node4)
linkedList.append(node5)
linkedList.append(node6)

"""print linked list"""
linkedList.checkIfPalindrome()
