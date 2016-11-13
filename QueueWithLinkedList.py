"""
Illustrating queue implementation with linked list
ADT for queue with linked list are
-enqueue() ( push new node into the queue )
-dequeue() ( remove node from the stack )
-front() ( get first node/first node inserted value from the queue )
-isEmpty() ( check if queue is empty or not )
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
        Constructor creates the head and tail node for our new linked list

        Args:
            head: head node for the linked list
            tail: tail node for the linked list
    """
    def __init__(self, head):
        self.head = head
        self.tail = head

    """
        Inserts new node into the tail position of linked list

        Args:
            newNode: new node to be added to the end of list
    """
    def insertAtTail(self, newNode):
        self.tail.next = newNode
        self.tail = newNode
        return None


    """
    Removes the head node from the linked list

    Returns:
        returns node value which was removed from the list or -1 in case list is empty
    """
    def deleteFromHead(self):
        if self.head:
            nodeRemoved = self.head
            self.head = nodeRemoved.next
            return nodeRemoved.value
        else:
            return -1

    """
        Returns the first node value from the list or -1 in case list is empty
    """
    def headNode(self):
        return self.head.value

    """
    Checks if list is empty and returns True False accordingly
    """
    def isLinkedListEmpty(self):
        if not self.head:
            return True
        else:
            return False

class Queue(object):
    """
    Initialises first element in queue
    """
    def __init__(self, head):
        self.ll = LinkedList(head)

    """
    enqueue new node onto the queue
    Args:
        newNode: new node to be enqued onto queue
    """
    def enqueue(self, newNode):
        self.ll.insertAtTail(newNode)

    """
    Dequeue node from the queue
    Returns:
        return the first node from the queue and deletes it in FIFO order
    """
    def dequeue(self):
        return self.ll.deleteFromHead()

    """
    Returns top element from queue
    """
    def front(self):
        return self.ll.headNode()

    """
    Returns True False based upon if queue is empty or not
    """
    def isEmpty(self):
        return self.ll.isLinkedListEmpty()

"""Creating new nodes for the queue"""
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node('a')
node5 = Node('b')

"""initialising and enqueuing new node in the queue"""
queue = Queue(node4)
queue.enqueue(node1)
queue.enqueue(node2)
queue.enqueue(node5)

"""print top element of the queue"""
print queue.front()

"""dequeue and print the value which is dequeued out of queue"""
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()

"""check if queue is empty or not"""
print queue.isEmpty()

