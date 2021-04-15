# playing around with different implementations of stacks 


# Stack Implementation as Linked List
class Node:
    def __init__(self):
        self.item: None
        self.next: None

class Stack:
    """The Stack class represents a last-in-first-out (LIFO) stack of generic
    items. It supports the usual push and pop operations, along with methods
    for peeking at the top item, testing if the stack is empty, and iterating
    through the items in LIFO order.
    This implementation uses a singly linked list with a static nested
    class for linked-list nodes. See LinkedStack for the version from
    the textbook that uses a non-static nested class. See
    ResizingArrayStack for a version that uses a resizing array. The
    push, pop, peek, size, and is-empty operations all take constant
    time in the worst case.
    """

    def __init__(self) -> None:
        """Initializes an empty stack."""
        self._first = None
        self._n = 0

    def is_empty(self) -> bool:
        """Returns true if this stack is empty.
        :returns: true if this stack is empty false otherwise
        """
        return self._n == 0

    def size(self) -> int:
        """Returns the number of items in this stack.
        :returns: the number of items in this stack
        """
        return self._n

    def __len__(self) -> int:
        return self.size()

    def push(self, item) -> None:
        """Adds the item to this stack.
        :param item: the item to add
        """
        oldfirst = self._first
        self._first = Node()
        self._first.item = item
        self._first.next = oldfirst
        self._n += 1

    def pop(self):
        """Removes and returns the item most recently added to this stack.
        :returns: the item most recently added
        :raises ValueError: if this stack is empty
        """
        if self.is_empty():
            raise ValueError("Stack underflow")
        assert self._first is not None
        item = self._first.item
        assert item is not None
        self._first = self._first.next
        self._n -= 1
        return item

    def peek(self):
        """Returns (but does not remove) the item most recently added to this
        stack.
        :returns: the item most recently added to this stack
        :raises ValueError: if this stack is empty
        """
        if self.is_empty():
            raise ValueError("Stack underflow")
        assert self._first is not None
        item = self._first.item
        assert item is not None
        return item

    def __repr__(self) -> str:
        """Returns a string representation of this stack.
        :returns: the sequence of items in this stack in LIFO order, separated by spaces
        """
        s = []
        for item in self:
            s.append(item.__repr__())
        return " ".join(s)

    def __iter__(self):
        """Returns an iterator to this stack that iterates through the items in
        LIFO order.
        :return: an iterator to this stack that iterates through the items in LIFO order
        """
        current = self._first
        while current is not None:
            item = current.item
            assert item is not None
            yield item
            current = current.next

def main():
    S = Stack()
    print(f"Length of Stack: {len(S)}")
    for i in range(3):
        S.push(i)
    for x, i in enumerate(S):
        print(x, i)

if __name__ == '__main__':
    main()


