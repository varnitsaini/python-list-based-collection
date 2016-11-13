"""
Illustrating stack implementation with arrays
ADT for stack with array's
-push() ( push new element into the stack )
-pop() ( pop element from the stack )
-top() ( get first node value from the stack )
-isEmpty() ( check if stack is empty or not )
"""


arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

"""
Push new element onto the stack
Args:
    new_element: new element to be pushed onto stack
"""
def push(new_element):
    arr.append(new_element)


"""
Pop element from the stack
Returns:
    return the top element of the stack and removes that value from stack
"""
def pop():
    return arr.pop()


"""
Returns top element from stack
"""
def top():
    return arr[len(arr) - 1]


"""
Returns True False based upon if stack is empty or not
"""
def isEmpty():
    if arr:
        return False
    else:
        return True

push("qwerty")
push(21)

print arr.pop()
print arr.pop()
print arr

print top()

print isEmpty()