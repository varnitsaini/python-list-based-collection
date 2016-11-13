"""
Illustrating stack implementation with linked list
ADT for stack with linked list are
-push() ( push new element into the stack )
-pop() ( pop element from the stack )
-top() ( get first node value from the stack )
-isEmpty() ( check if stack is empty or not )
"""

"""
Creates new Node

Args:
    value: desired value in the node

Returns:
    object for the Node
"""
class Node(object):
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
    def __init__(self, head = None):
        self.head = head

    """
    Inserts new element into the head position of linked list

    Args:
        new_element: new element to be added to the list
    """
    def insertAtFirst(self, new_element):
        new_element.next = self.head
        self.head = new_element
        pass

    """
    Removes the head node from the linked list

    Returns:
        returns item which was removed from the list or -1 in case list is empty
    """
    def removeFromFirst(self):
        if self.head:
            removedItem = self.head
            self.head = removedItem.next
            return removedItem.value
        else:
            return -1

    """
    Returns the first node value from the list or -1 in case list is empty
    """
    def getFirstNode(self):
        if self.head:
            return self.head.value
        else:
            return -1

    """
    Checks if list is empty and returns True False accordingly
    """
    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

"""
Stack Class
"""
class Stack(object):
    """
    Initialises first element in the stack
    """
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    """
    Push new element onto the stack
    Args:
        new_element: new element to be pushed onto stack
    """
    def push(self, new_element):
        self.ll.insertAtFirst(new_element)

    """
    Pop element from the stack
    Returns:
        return the top element of the stack and removes that value from stack
    """
    def pop(self):
        return self.ll.removeFromFirst()

    """
    Returns top element from stack
    """
    def top(self):
        return self.ll.getFirstNode()

    """
    Returns True False based upon if stack is empty or not
    """
    def isEmpty(self):
        return self.ll.isEmpty()


"""Creating new nodes for the stack"""
node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node(1)
node5 = Node(2)

"""initialising new element in the stack"""
stack = Stack(node1)
stack.push(node2)
stack.push(node3)

"""print top element of the stack"""
print stack.top()

"""pop and print the value which is pop'ed out of stack"""
print stack.pop()
print stack.pop()
print stack.pop()

"""check if stack is empty or not"""
print stack.isEmpty()

"""fetch the top element from the stack"""
print stack.top()


stack.push(node5)
print stack.pop()
