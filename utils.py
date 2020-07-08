"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList,TestingQueue
from Scrapbook import MaxHeap
import os

class PatientUtils:
    def __init__(self):
        self.id_count = 1001
        self.patient_list = PatientList()
        self.testingQueue = TestingQueue()
        self.sortedQueue= MaxHeap(10)

    def registerPatient(self, name, age):
        try:
            patient_id = f"{self.id_count}{age}"
            self.patient_list.add(name=name, age=age, patient_id=patient_id)
            self.id_count += 1
            # Refreshing queue
            self.enqueuePatient(patient_id)


        except Exception as e:
            raise e

    def displayPatients(self):
        self.patient_list.display()
        self.sortedQueue.Print()

    def enqueuePatient(self, PatId):
        self.sortedQueue.insert(int(PatId)%100)
        #self.testingQueue.add(str(PatId)[-2:],str(PatId))
        # Heap method to be used here is  - add(self, key, value)
        # Split patient id to get age and assign age to key and patientID to value

        # Need to check whether only the call to add() method is sufficient or
        # full functionality needs to be coded
        pass

    def nextPatient(self):
        Delete_Patient=self.sortedQueue.extractMax()
        print(Delete_Patient)
        self._dequeuePatient(Delete_Patient)
        #need to write these records in output file now

        #Heap method to use here is - remove_max(self)
        #It will output the patient id with highest priority and remove it from the heap
        #Alternate method if you dont want to remove from heap is - max(self)

        # Also  calls _dequeuePatient function below


    def _dequeuePatient(self, PatId):
        print("Pending Code to delete from queue/list??")
        # To be called from nextPatient() function
        pass
    def SearchList(self,PatID):
        print("value in heap and list need to be linked so that we can print the complete records and not just the age/patientid")