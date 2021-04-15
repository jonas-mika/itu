# playing around with different implementations of queues


# Queue Implementation using Linked Lists
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    """The Queue class represents a first-in-first-out (FIFO) queue of generic
    items.
    It supports the usual enqueue and dequeue operations, along with
    methods for peeking at the first item, testing if the queue is
    empty, and iterating through the items in FIFO order This
    implementation uses a singly linked list of linked-list nodes The
    enqueue, dequeue, peek, size, and is_empty operations all take
    constant time in the worst case
    """

    def __init__(self) -> None:
        """Initializes an empty queue."""
        self._first = None
        self._last = None
        self._n = 0

    def enqueue(self, item) -> None:
        """Adds the item to this queue.
        :param item: the item to add
        """
        old_last = self._last
        self._last = Node(item, None)
        if self.is_empty():
            self._first = self._last
        else:
            assert old_last is not None
            old_last.next = self._last
        self._n += 1

    def dequeue(self):
        """
        Removes and returns the item on this queue that was least recently added.
        :return: the item on this queue that was least recently added.
        :raises NoSuchElementException: if this queue is empty
        """
        if self.is_empty():
            raise ValueError("Queue Underflow")

        assert self._first is not None
        item = self._first.item
        self._first = self._first.next
        self._n -= 1
        if self.is_empty():
            self._last = None
        return item

    def is_empty(self) -> bool:
        """Returns true if this queue is empty.
        :return: True if this queue is empty otherwise False
        :rtype: bool
        """
        return self._first is None

    def size(self) -> int:
        """Returns the number of items in this queue.
        :return: the number of items in this queue
        :rtype: int
        """
        return self._n

    def __len__(self) -> int:
        return self.size()

    def peek(self):
        """
        Returns the item least recently added to this queue.
        :return: the item least recently added to this queue
        :raises NoSuchElementException: if this queue is empty
        """
        if self.is_empty():
            raise ValueError("Queue underflow")

        assert self._first is not None
        return self._first.item

    def __iter__(self):
        """Iterates over all the items in this queue in FIFO order."""
        curr = self._first
        while curr is not None:
            yield curr.item
            curr = curr.next

    def __repr__(self) -> str:
        """Returns a string representation of this queue.
        :return: the sequence of items in FIFO order, separated by spaces
        """
        s = []
        for item in self:
            s.append("{} ".format(item))
        return "".join(s)

def main():
    Q = Queue()
    for i in range(1,10):
        Q.enqueue(i)
    print(Q)

if __name__=='__main__':
    main()

