"""
Following code will illustrates the implementation of two
Stacks Data Structure in Single Array

There are basically two ways of implementing two Stacks in Single Array

1) We divide the given array in two equal parts ie one part will contain
   [0:n/2] elements and the second part of the array will contain [n/2:n]
   elements.
   But this approach is not the optimum one because it might happen that
   given two stack we do push() operation only on one stack so the space
   allocated of second stack in the array will be waste.

2) The second approach is starting the stacks with the two extreme ends
   of the array ie starting stack one from one end of the array and starting
   another stack from other end of the array.
   In this approach whole space for the array will be utilised and we will
   stop the push operation once the top elements of both the stack will be
   next adjacent to each other

Here we will proceed with the first approach since its more optimum one.
"""

class Stack:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.topA = -1
        self.topB = self.size

    def pushA(self, value):

        if self.topA + 1 != self.topB:
            self.array[self.topA + 1] = value
            self.topA += 1
        else:
            print "Stack is full"
            exit()

    def pushB(self, value):

        if self.topA + 1 != self.topB:
            self.array[self.topB - 1] = value
            self.topB -= 1
        else:
            print "Stack is full"
            exit()

    def popA(self):

        if self.topA == -1:
            print "Stack A is already empty"
        else:
            topElement = self.array[self.topA]
            self.array[self.topA] = None
            self.topA -= 1
            return topElement

    def popB(self):

        if self.topB == self.size:
            print "Stack B is already empty"
        else:
            topElement = self.array[self.topB]
            self.array[self.topB] = None
            self.topB += 1
            return topElement

    def printStack(self):
        print self.array

stack = Stack(7)
stack.pushA(2)
stack.pushA(4)
stack.pushA(1)

stack.pushB(32)
stack.pushB(43)
stack.pushB(13)

stack.printStack()
print stack.popA()
print stack.popB()
stack.printStack()


