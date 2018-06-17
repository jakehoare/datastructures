_author_ = 'jake'
_project_ = 'datastructures'

import heapq

class Apq_heapq():
    """
    Creates an adaptable priority queue from heapq.
    Dictionary is used to track entries in priority queue so items can be located in O(1).
    Removed entries remain in heap with item of "<REMOVED>" and are ignored by pop and peek.
    Counter is used to ensure pop order is stable with respect to insert or update order.
    """
    def __init__(self):
        self.heap = []                      # underlying heap
        self.item_mapping = {}              # map from item to list of [priority, count, item]
        self.counter = 0                    # count breaks priority ties so input/update order is preserved (stable)

    def add_item(self, item, priority = 0):
        """
        Add or update item with specified priority.
        :param item:
        :param priority: float
        :return: None
        """
        if item in self.item_mapping:       # remove old item from mapping and set to "<REMOVED>" in heap
            self.remove_item(item)
        entry = [priority, self.counter, item]
        self.counter += 1
        self.item_mapping[item] = entry     # update mapping
        heapq.heappush(self.heap, entry)    # push entry to heap

    def remove_item(self, item):
        entry = self.item_mapping.pop(item)
        entry[-1] = "<REMOVED>"

    def pop_min(self):
        while self.heap:
            _, _, item = heapq.heappop(self.heap)
            if item != "<REMOVED>":        # throw away removed items
                del self.item_mapping[item]
                return item
        raise KeyError('pop from an empty priority queue')

    def peek_min(self):
        while self.heap:
            _, _, item = self.heap[0]
            if item != "<REMOVED>":
                return item
            heapq.heappop(self.heap)        # throw away removed items
        raise KeyError('peek at empty priority queue')
