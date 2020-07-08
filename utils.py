"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList, TestingQueue
import os


class PatientUtils:
    def __init__(self):
        self.id_count = 1001
        self.patient_data = None
        self.patient_list = PatientList()
        self.testing_queue = TestingQueue()

    def readAndOutputInitialPatients(self):
        try:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6a.txt'))
            with open(file_path, 'r') as file:
                patient_data = file.read().splitlines()
                for data in patient_data:
                    name, age = data.split(",")
                    # Add patients to Patient Record List
                    self.registerPatient(name=name.strip(), age=age.strip())
            # Sort the testing queue
            self.testing_queue.sort()
            # Output the contents
            self.outputRegisteredPatientInfo()
        except Exception as e:
            raise e

    def registerPatient(self, name, age):
        try:
            patient_id = f"{self.id_count}{age}"
            self.patient_list.add(name=name, age=age, patient_id=patient_id)
            self.id_count += 1
            # Enqueuing the patients in the heap
            self.enqueuePatient(patient_id=int(patient_id))
        except Exception as e:
            raise e

    def outputRegisteredPatientInfo(self):
        try:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output', 'outputPS6.txt'))
            patients_in_queue = self.testing_queue.get_patients()
            with open(file_path, 'w') as file:
                file.write("-----------------Initial Queue-----------------\n")
                file.write(f"No of patients added: {len(patients_in_queue)}\n")
                file.write("Refreshed queue:\n")
                for patient in patients_in_queue[::-1]:
                    patient_id = patient._value
                    file.write(f"{patient_id}, {self.patient_list.getPatientName(str(patient_id))}\n")
                file.write("------------------------------------------------")
        except Exception as e:
            raise e

    def enqueuePatient(self, patient_id):
        self.testing_queue.add(patient_id=int(patient_id))

    def nextPatient(self):
        #Heap method to use here is - remove_max(self)
        #It will output the patient id with highest priority and remove it from the heap
        #Alternate method if you dont want to remove from heap is - max(self)

        # Also  calls _dequeuePatient function below
        pass

    def _dequeuePatient(self, PatId):
        # To be called from nextPatient() function
        pass
