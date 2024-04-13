"""Queue implementation using two stacks"""
from collections import deque


class MyQueue:
    """Queue implemented with two queues"""

    def __init__(self):
        self.direct_stack = deque()
        self.reversed_stack = deque()

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
        return self.reversed_stack[-1]

    def empty(self) -> bool:
        """Return True if queue is empty"""
        return not (self.direct_stack or self.reversed_stack)

    def _copy_from_direct_to_reversed(self):
        """Copy all data from direct to reversed queue"""
        while self.direct_stack:
            self.reversed_stack.append(self.direct_stack.pop())

    def _copy_from_reversed_to_direct(self):
        """Copy all data from reversed to direct queue"""
        while self.reversed_stack:
            self.direct_stack.append(self.reversed_stack.pop())
