"""Stack implementation using two queues"""


class Node:
    """Node"""

    def __init__(self, item: int) -> None:
        """Initialize node"""
        self.item = item
        self.next = None
        self.prev = None



class Queue:
    """Queue implementation"""

    def __init__(self) -> None:
        """Initialize queue"""
        self.front = None
        self.back = None

    def push(self, item: int) -> None:
        """Push element to back of the queue"""
        if not self.back:
            self.front = self.back = Node(item)
            return

        back = Node(item)
        back.next = self.back
        self.back.prev = back
        self.back = back

    def pop(self) -> int:
        """Pop element from front of queue"""        
        front = self.front
        self.front = self.front.prev
        self.front.next = None
        return front.item

    def peek(self) -> int:
        """Peek element from front of queue"""
        return self.front.item


class MyStack:
    """Stack implementation using two queues"""

    def __init__(self):
        self.first_queue = []
        self.second_queue = []

    def push(self, x: int) -> None:
        """Push to the stack"""
        self.first_queue.append(x)

    def pop(self) -> int:
        """Pop from the top of the stack"""
        while self.first_queue:
            current = self.first_queue.pop(0)
            if len(self.first_queue) != 0:
                self.second_queue.append(current)
        self.first_queue, self.second_queue = self.second_queue, []
        return current

    def top(self) -> int:
        """Return element from top of stack"""
        while self.first_queue:
            current = self.first_queue.pop(0)
            self.second_queue.append(current)
        self.first_queue, self.second_queue = self.second_queue, []
        return current

    def empty(self) -> bool:
        """Return True if stack is empty"""
        return not self.first_queue
