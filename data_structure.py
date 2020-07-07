"""
This module has the custom data structures used in the application

PatientRecord: A list containing the patient information including the patient’s name, age and the patient number (assigned by the program).

TestingQueue: A max heap containing the patient id sorted in order of next patient for testing based on the age of the patient.
"""


# Represent a node of doubly linked list
class PatientRecord:
    def __init__(self, name, age, id):
        self.patient_id = str(id) + str(age)
        self.name = name
        self.age = age
        self.left = None
        self.right = None

class PatientList:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None;
        self.tail = None;

        # addNode() will add a node to the list

    def addNode(self,name, age, id):
        # Create a new node
        newPatient = PatientRecord(name, age, id);

        # If list is empty
        if (self.head == None):
            # Both head and tail will point to newNode
            self.head = self.tail = newPatient;
            # head's previous will point to None
            self.head.left = None;
            # tail's next will point to None, as it is the last node of the list
            self.tail.right = None;
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.right = newPatient;
            # newNode's previous will point to tail
            newPatient.left = self.tail;
            # newNode will become new tail
            self.tail = newPatient;
            # As it is last node, tail's next will point to None
            self.tail.right = None;

            # display() will print out the nodes of the list

    def display(self):
        # Node current will point to head
        current = self.head;
        if (self.head == None):
            print("List is empty");
            return;
        print("Nodes of doubly linked list: ");
        while (current != None):
            # Prints each node by incrementing pointer.
            print(current.name),;
            current = current.right;


dList = PatientList();
# Add nodes to the list
dList.addNode("abc",12,342);
dList.addNode("abc2",43,342);




# Displays the nodes present in the list
dList.display();


class TestingQueue:
    def __init__(self):
        pass
