_author_ = 'jake'
_project_ = 'datastructures'

import heapq, itertools

class Apq_heapq():
    def __init__(self):
        self.heap = []                      # underlying heap
        self.value_mapping = {}             # map from value to entry of [priority, count, value]
        self.counter = 0                    # count breaks priority ties so input/update order is preserved (stable)

    def add_value(self, value, priority=0):
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


if __name__ == "__main__":
    test_apq = Apq_heapq()
    tasks = ['s', 'd', 'r', 'x']
    priorities = [1, 3, 1, 2]

    for i in range(len(tasks)):
        test_apq.add_value(tasks[i], priorities[i])
    for i in range(len(tasks)):
        print(test_apq.pop_min())

