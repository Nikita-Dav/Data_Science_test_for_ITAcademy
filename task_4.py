class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            popped = self.top
            self.top = self.top.next
            popped.next = None
            self.size -= 1
            return popped.value
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            raise IndexError("Стек пуст")

    def is_empty(self):
        return self.top is None