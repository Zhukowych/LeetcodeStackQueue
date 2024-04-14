"""Implementation of frequency stack"""
from collections import deque


class FreqStack:
    """FreqStack"""

    def __init__(self) -> None:
        """Initialize frequency stack"""
        self.stack = deque()
        self.frequencies = deque()

    def push(self, val: int) -> None:
        """Push to the FreqStack"""
        self.stack.appendleft(val)
        self.frequencies.appendleft(self.stack.count(val))

    def pop(self) -> int:
        """pop most frequent element from stack"""

        max_frequency_element = None
        max_frequency = 0

        for element, frequency in zip(self.stack, self.frequencies):
            if frequency > max_frequency:
                max_frequency_element = element
                max_frequency = frequency

        self.stack.remove(max_frequency_element)
        self.frequencies.remove(max_frequency)

        return max_frequency_element
