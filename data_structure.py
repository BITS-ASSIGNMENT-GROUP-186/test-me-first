"""
This module has the custom data structures used in the application

PatientRecord: A list containing the patient information including the patient’s name, age and the patient number (assigned by the program).

TestingQueue: A max heap containing the patient id sorted in order of next patient for testing based on the age of the patient.
"""


# Represent a node of doubly linked list
class PatientRecord:
    def __init__(self, name, age, patient_id):
        self.patient_id = patient_id        
        self.name = name
        self.age = age
        self.left = None
        self.right = None


class PatientList:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # add() will add a node to the list
    def add(self, name, age, patient_id):
        # Create a new node
        new_patient = PatientRecord(name, age, patient_id)

        # If list is empty
        if not self.head:
            # Both head and tail will point to newNode
            self.head = self.tail = new_patient
            # head's previous will point to None
            self.head.left = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.right = None
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.right = new_patient
            # newNode's previous will point to tail
            new_patient.left = self.tail
            # newNode will become new tail
            self.tail = new_patient
            # As it is last node, tail's next will point to None
            self.tail.right = None

    # display() will print out the nodes of the list
    def display(self):
        # Node current will point to head
        current = self.head
        if not self.head:
            print("List is empty")
            return
        
        print("Nodes of doubly linked list: ")
        while current is not None:
            # Prints each node by incrementing pointer.
            print(current.patient_id ,current.name, current.age)
            current = current.right

    def getPatientDetails(self, patient_id):
        # Node current will point to head
        current = self.head
        if not self.head:
            print("List is empty")
            return

        while current is not None:
            # Prints each node by incrementing pointer.
            if current.patient_id == patient_id:
                return current
            current = current.right


class TestingQueue:
    def __init__(self):
        self.size = 0
        self.heap = []

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self.heap)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self.heap)  # index beyond end of list?

    def is_empty(self):  # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self.heap) == 0

    def swap(self, i, j):
        """
        Swap the elements at indices i and j of array.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def top(self):
        return self.heap[0] if self.heap else "No patient in the queue. Heap is empty"

    def remove_max(self):
        if self.is_empty():
            raise Exception("Testing queue is empty")
        self.swap(0, len(self.heap) - 1)  # put maximum item at the end
        self.heap.pop()  # and remove it from the list
        self.size -= 1
        self.downheap(0)  # then fix new root

    # def upheap(self, j):
    #     try:
    #         parent = self._parent(j)
    #         if j > 0 and self.heap[j] % 100 > self.heap[parent] % 100:
    #             self.swap(j, parent)
    #             self.upheap(parent)  # recur at position of parent
    #     except Exception as e:
    #         raise e

    def downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            big_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self.heap[right] % 100 > self.heap[left] % 100:
                    big_child = right
            if self.heap[big_child] % 100 > self.heap[j] % 100:
                self.swap(j, big_child)
                self.downheap(big_child)  # recur at position of small child

    def upheap(self, n=None):
        start = self._parent(n if n else len(self.heap) - 1)  # start at PARENT of last leaf
        for j in range(start, -1, -1):  # going to and including the root
            self.downheap(j)

    # Function to heapify the node at pos
    def maxHeapify(self, pos):
        # If the node is a non-leaf node and smaller than any of its child
        if self._parent(pos):
            if (self.heap[pos] % 100 < self.heap[self._left(pos)] % 100 or
                    self.heap[pos] % 100 < self.heap[self._right(pos)] % 100):

                # Swap with the left child and heapify the left child
                if self.heap[self._left(pos) % 100] > self.heap[self._right(pos) % 100]:
                    self.swap(pos, self._left(pos))
                    self.maxHeapify(self._left(pos))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self._right(pos))
                    self.maxHeapify(self._right(pos))

    # def downheap(self, i):
    #     left_flag, right_flag = 0, 0
    #     largest = self.heap[i] % 100
    #     n = self.size
    #     left = i * 2 + 1
    #     right = left + 1
    #     if left <= n:  # left exists
    #         left_flag = 1
    #     if right <= n:  # right exists
    #         right_flag = 1
    #     if left_flag == 1:
    #         if largest < self.heap[left] % 100:  # compare with left child
    #             if right_flag == 1:
    #                 if (self.heap[left] % 100) < (self.heap[right] % 100):
    #                     self.swap(right, i)  # swap right with parent if its bigger than both parent and left
    #                     self.downheap(right)
    #                 else:
    #                     self.swap(left, i)  # swap left with parent if its bigger than both parent and right
    #                     self.downheap(left)
    #             else:
    #                 self.swap(left, i)  # swap left with parent if its bigger than parent and right doesnt exist
    #                 self.downheap(left)

    # sort
    def heap_sort(self):
        n = len(self.heap)

        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            if self.heap[i] % 100 == self.heap[0] % 100 and self.heap[0] > self.heap[1]:
                self.heapify(i, 0)
                continue
            self.swap(i, 0)
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = i  # largest value
        left_child = self._left(i)
        right_child = self._right(i)

        # if left child exists
        if left_child < n and self.heap[i] % 100 < self.heap[left_child] % 100:
            largest = left_child

        # if right child exits
        if right_child < n and self.heap[largest] % 100 < self.heap[right_child] % 100:
            largest = right_child

        # root
        if largest != i:
            self.swap(i, largest)
            self.heapify(n, largest)

    def insert(self, patient_id):
        self.size += 1
        self.heap.append(patient_id)
