"""
This module has the custom data structures used in the application

PatientRecord: A list containing the patient information including the patient’s name, age and the patient number (assigned by the program).

TestingQueue: A max heap containing the patient id sorted in order of next patient for testing based on the age of the patient.
"""


# Represent a node of doubly linked list
class PatientRecord:
    def __init__(self, name, age, patient_id):
        self.patient_id = str(patient_id) +str(age)
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

    def __len__(self):
        current = self.head
        if not self.head:
            raise Exception("List is empty!!")
            return

        count = 0
        while current is not None:
            count+=1
            current = current.right
        return count

    def getList(self):
        return list(self.current)


class TestingQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key # compare items based on their keys

    def is_empty(self):  # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0


class TestingQueue(TestingQueueBase):
    """
    A max-oriented priority queue implemented with a binary heap.
    """
    #------------------------------ nonpublic behaviors ------------------------------#
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data) # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data) # index beyond end of list?

    def _swap(self, i, j):
        """
        Swap the elements at indices i and j of array.
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent) # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            big_child = left # although right may be bigger
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    big_child = right
            if self._data[big_child] > self._data[j]:
                self._swap(j, big_child)
                self._downheap(big_child) # recur at position of small child

    # ------------------------------ public behaviors ------------------------------
    def __init__(self,contents=()):
        """Create a new empty Priority Queue"""
        #self._data = []
        self._data = [self._Item(k, v) for k, v in contents]  # empty by default
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1)  # start at PARENT of last leaf
        for j in range(start, -1, -1):  # going to and including the root
            self._downheap(j)

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)  # upheap newly added position

        #self._data.append(self._Item(str(key)[-2:], str(key) + ", " + value))
        #self._upheap(len(self._data) - 1)  # upheap newly added position

    def max(self):
        """
        Return but do not remove (k,v) tuple with maximum key.
        Raise exception if empty.
        """
        if self. is_empty():
            raise Exception("Priority Queue/Heap is empty. Please fill some values and try again!!!")
        item = self._data[0]
        return (item._value)

    def remove_max(self):
        """
        Remove and return (k,v) tuple with maximum key.
        Raise exception if empty.
        """
        if self. is_empty():
            raise Exception("Priority Queue/Heap is empty. Please fill some values and try again!!!")
        self._swap(0, len(self._data) - 1)  # put maximum item at the end
        item = self._data.pop(-1)  # and remove it from the list;
        self._downheap(0)  # then fix new root
        return (item._key, item._value)

    # def display(self):
    #     """
    #     Prints full testing queue
    #     """
    #     print("\nCurrently Patients in Queue:")
    #     for i in self._data:
    #         print(i._value)

    # def display_x(self,count):
    #     """
    #     Prints 'x' number of patients in testing queue
    #     """
    #     print("\n---- next patient : " + str(count) + " ---------------")
    #     i = 0
    #     while i < count:
    #         print("Next patient for testing is: " + self.max())
    #         i += 1
    #     print("----------------------------------------------")
#
# tstngQ = TestingQueue()
# tstngQ.add(100455,"John")
# tstngQ.add(100160,"Surya")    #equivalent to enqueuePatient(self, PatId)
# tstngQ.add(100357,"Rishi")
# tstngQ.add(100254,"Ajay")
#
# tstngQ.display()
#
# tstngQ.display_x(3)
#
