
class Stack:

    def __init__(self):
        """Initialize empty stack"""
        self._objects = []

    def is_empty(self) -> bool:
        """Return True if stack contains no elements, otherwise False"""
        return len(self._objects) == 0

    def push(self, item) -> None:
        """Add item to top of stack"""
        self._objects.append(item)

    def pop(self):
        """Remove and return item to top of stack"""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._objects.pop()

    def peek(self):
        """Return item to top of stack without removal"""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._objects[-1]

    def size(self) -> int:
        """Return number of elements in current stack"""
        return len(self._objects)