"""Stack implementation using two queues"""

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
