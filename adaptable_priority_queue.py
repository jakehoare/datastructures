_author_ = 'jake'
_project_ = 'datastructures'

import heapq

class Apq_heapq():
    """
    Creates an adaptable priority queue from heapq.
    Dictionary is used to track entries in priority queue so items can be located in O(1).
    Removed or updated entries remain in heapq with value of "<REMOVED>" and ignored by pop and peek.
    Counter is used to ensure pop order is stable with respect to insert or update order.
    """
    def __init__(self):
        self.heap = []                      # underlying heap
        self.value_mapping = {}             # map from value to entry of [priority, count, value]
        self.counter = 0                    # count breaks priority ties so input/update order is preserved (stable)

    def add_value(self, value, priority=0):
        """
        Add or update value with specified priority.
        :param value:
        :param priority: float
        :return: None
        """
        if value in self.value_mapping:     # remove old value from mapping and set to "REMOVED" in heap
            self.remove_value(value)
        entry = [priority, self.counter, value]
        self.counter += 1
        self.value_mapping[value] = entry   # update mapping
        heapq.heappush(self.heap, entry)    # push entry to heap

    def remove_value(self, value):
        entry = self.value_mapping.pop(value)
        entry[-1] = "<REMOVED>"

    def pop_min(self):
        while self.heap:
            _, _, value = heapq.heappop(self.heap)
            if value != "<REMOVED>":        # throw away removed values
                del self.value_mapping[value]
                return value
        raise KeyError('pop from an empty priority queue')

    def peek_min(self):
        while self.heap:
            _, _, value = self.heap[0]
            if value != "<REMOVED>":
                return value
            heapq.heappop(self.heap)        # throw away removed values
        raise KeyError('peek at empty priority queue')
