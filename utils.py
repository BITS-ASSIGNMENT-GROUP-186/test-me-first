"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList


class PatientUtils:
    def __init__(self):
        self.id_count = 1001
        self.patient_list = PatientList()

    def registerPatient(self, name, age):
        try:
            patient_id = f"{self.id_count}{age}"
            self.patient_list.add(name=name, age=age, patient_id=patient_id)
            self.id_count += 1
        except Exception as e:
            raise e

    def displayPatients(self):
        return self.patient_list.display()

    def enqueuePatient(self, PatId):
        # Heap method to be used here is  - add(self, key, value)
        # Split patient id to get age and assign age to key and patientID to value

        # Need to check whether only the call to add() method is sufficient or
        # full functionality needs to be coded
        pass

    def nextPatient(self):
        #Heap method to use here is - remove_max(self)
        #It will output the patient id with highest priority and remove it from the heap
        #Alternate method if you dont want to remove from heap is - max(self)

        # Also  calls _dequeuePatient function below
        pass

    def _dequeuePatient(self, PatId):
        # To be called from nextPatient() function
        pass
