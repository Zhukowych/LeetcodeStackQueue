"""Queue implementation using two stacks"""


class Node:
    """Node"""

    def __init__(self, item: int) -> None:
        """Initialize node"""
        self.item = item
        self.next = None


class Stack:
    """Stack"""

    def __init__(self) -> None:
        """Initialize stack"""
        self.top = None

    def __bool__(self) -> bool:
        """Return bool of stack"""
        return bool(self.top)

    def append(self, item: int) -> None:
        """append item to the top of stack"""
        top = Node(item)
        top.next = self.top
        self.top = top

    def pop(self) -> int:
        """Pop element from top of the stack"""
        top = self.top
        self.top = top.next
        return top.item

    def peek(self) -> int:
        """Peek element from the top of the stack"""
        return self.top.item


class MyQueue:
    """Queue implemented with two queues"""

    def __init__(self):
        self.direct_stack = Stack()
        self.reversed_stack = Stack()

    def push(self, x: int) -> None:
        """Push x to the top of queue"""
        if not self.direct_stack:
            self._copy_from_reversed_to_direct()
        self.direct_stack.append(x)

    def pop(self) -> int:
        """Pop element from end of queue"""
        if not self.reversed_stack:
            self._copy_from_direct_to_reversed()
        return self.reversed_stack.pop()

    def peek(self) -> int:
        """Peek element from end of queue"""
        if not self.reversed_stack:
            self._copy_from_direct_to_reversed()
        return self.reversed_stack.peek()

    def empty(self) -> bool:
        """Return True if queue is empty"""
        return not (self.direct_stack or self.reversed_stack)

    def _copy_from_direct_to_reversed(self):
        """Copy all data from direct to reversed stacks"""
        while self.direct_stack:
            self.reversed_stack.append(self.direct_stack.pop())

    def _copy_from_reversed_to_direct(self):
        """Copy all data from reversed to direct stacks"""
        while self.reversed_stack:
            self.direct_stack.append(self.reversed_stack.pop())


q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.peek())
print(q.pop())
print(q.pop())
print(q.pop())