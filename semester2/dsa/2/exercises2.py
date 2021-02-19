# exercise 1 - circular strings

def is_circular(s, t):
    current_rotation = ''
    cha_list = [cha for cha in s] # list of characters in string s
    rotations = []

    while current_rotation != s:
        cha_list.insert(0, cha_list.pop())
        s_rot = "".join(cha_list)

        rotations.append(s_rot)
        current_rotation = s_rot
    
    if t in rotations:
        return True
    else: return False

# print(is_circular("TAG", "AGT"))
# print(is_circular("ACTGACG", "TGACGAC"))

class Node:
    def __init__(self):
        self.item = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = Node()
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def push(self, item):
        oldfirst = self.first
        self.first = Node()
        self.first.item = item
        self.first.next = oldfirst
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        assert self.first is not None
        item = self.first.item
        assert item is not None
        self.first = self.first.next
        self.n -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        assert self.first is not None
        item = self.first.item
        assert item is not None
        return item

    def delete(self, k: int):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        i = 0
        current = self.first
        while i != k:
            previous = current
            current = previous.next
            i += 1
        previous.next = current.next
        self.n -= 1

    def find(self, key):
        if self.is_empty():
            return False

        node = self.first 
        for _ in range(self.n):
            item = node.item
            if item == key:
                return True
            node = node.next
        return False

    def max(self):
        if self.is_empty():
            return 0
        max_ = 0
        node = self.first
        for _ in range(self.n):
            item = node.item
            if item > max_:
                max_ = item
            node = node.next
        return max_

    def max_rec(self, node):
        if self.is_empty():
            return 0
        max_ = node.item 
        print(max_)
        if node.item == None:
            return max_ 
        return LinkedList.max_rec(self, node.next)

    def remove_after(self, node):
        if self.is_empty():
            raise ValueError('Stack Underflow')

        previous = self.first
        current = self.first
        for _ in range(self.n):
            next_ = current.next
            if next_ == node:
                if _ == 0:
                    next_ = self.first
                else:
                    previous.next = next_
            previous = current
            current = next_
        self.n -= 1


    def __repr__(self):
        s = []
        for item in self:
            s.append(item.__repr__())
        return " ".join(s)

    def __iter__(self):
        current = self.first

        while current is not None:
            item = current.item
            assert item is not None
            yield item
            current = current.next

linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)
linked_list.push(5)
a = Node()
a.item = 3
a.next = 2
linked_list.remove_after(a)
print(linked_list.pop())
print(linked_list.pop())
print(linked_list.pop())
print("\n")
print(linked_list.max())
# print(linked_list.max_rec(linked_list.first))
linked_list.push(4)
print(linked_list.find(5))
linked_list.delete(2)
linked_list.push(7)
print(linked_list.pop())
print(linked_list.pop())
print(linked_list.pop())


# exercise 6 - code

# switches the nodes t and x in the linked list

# exercise 7 - code

# creates a loop in the linked list (isolate t, because t will point to itself)

# DOUBLE-LINKED LIST

class DoubleNode:
    def __init__(self):
        self.item =  None
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.back = None
        self.front = None
        self.n = 0
    
    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def push_to_front(self, item):
        oldfront = self.front

        self.front = DoubleNode()
        self.front.item = item
        self.front.next = oldfront
        self.n += 1

    def push_to_back(self, item):
        oldback = self.back
        self.back = DoubleNode()
        self.back.item = item
        self.back.prev = oldback
        self.n += 1

    def pop_from_front(self):
        if is_empty():
            raise ValueError('Stack Underflow')
        assert self.front is not None
        item = self.front.item
        assert item is not None
        self.front = self.front.next
        return item
        
        

dll = DoubleLinkedList()
dll.push_to_front(1)
dll.push_to_front(2)
dll.push_to_back(0)
for _ in range(2):
    dll.pop_from_front()

