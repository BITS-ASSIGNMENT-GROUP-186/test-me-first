"""
This module has the custom data structures used in the application

PatientRecord: A list containing the patient information including the patient’s name, age and the patient number (assigned by the program).

MaxHeap: A max heap containing the patient id sorted in order of next patient for testing based on the age of the patient.
"""


# Represent a node of doubly linked list
class PatientRecord:
    def __init__(self, name, age, patient_id):
        self.patient_id =patient_id
        #self.patient_id = str(patient_id) +str(age)
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
                return current.patient_id,current.name ,current.age
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
##_____________________________________________________________________________________________
class MaxHeap:
    def __init__(self, maxsize1):
        self.maxsize = maxsize1
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = 0
        self.FRONT = 1

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        temp=self.Heap[fpos]
        self.Heap[fpos]=self.Heap[spos]
        self.Heap[spos] = temp

    def extractMax(self):
        if self.size>0 :
            return self.Heap[self.FRONT]

    def test_dequeMax(self):
        #print(str(self.Heap[self.FRONT]) + " exchanged with " + str(self.size) + " ie :" + str(self.Heap[self.size]))
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.test_downheap(1)
        self.FRONT=1

    def test_upheap(self, i):
        i = int(i)
        parent = int(i / 2)
        # print(str(parent)+"is parent of"+str(self.Heap[i]))
        largest = self.Heap[i] % 100
        if (parent) > 0:
            if (i % 2 == 0):  # it is a left node
                if largest > (self.Heap[parent]) % 100:  # compare with parent
                    self.swap(i, parent)  # swap with parent if its bigger than parent
            else:
                if largest > (self.Heap[parent]) % 100:  # compare with parent
                    if largest > (self.Heap[i - 1]) % 100:  # compare with left sibling
                        self.swap(i, parent)  # swap with parent if its bigger than parent and left sibling
                    else:
                        self.swap(i - 1, parent)  # swap parent with left sibling
            self.test_upheap(parent)

    def test_downheap(self, i):
        FlagL=0
        FlagR=0
        largest = self.Heap[i] % 100
        n=self.size
        Left=i*2
        Right=Left+1
        if Left<=n: #Left exists
            FlagL=1
        if Right<=n: #right exists
            FlagR=1
        if FlagL==1:
            if largest < (self.Heap[Left]) % 100:  # compare with left child
                if FlagR==1:
                    if ((self.Heap[Left]) % 100)<((self.Heap[Right]) % 100):
                        self.swap(Right, i)  # swap right with parent if its bigger than both parent and left
                        self.test_downheap(Right)
                    else:
                        self.swap(Left, i)  # swap left with parent if its bigger than both parent and right
                        self.test_downheap(Left)
                else:
                    self.swap(Left, i)  # swap left with parent if its bigger than parent and right doesnt exist
                    self.test_downheap(Left)

    def test_insert(self, element):
        self.size += 1
        n=self.size
        self.Heap[n] = element
        if (n>1):
            self.test_upheap(n)



