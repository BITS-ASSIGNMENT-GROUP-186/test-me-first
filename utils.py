"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList, TestingQueue
import functools
import time
import os


class Decorators:
    @staticmethod
    def timer(func):
        """Print the runtime of the decorated function"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
            return value
        return wrapper


class PatientUtils:
    def __init__(self):
        self.id_count = 1001
        self.patient_list = PatientList()
        self.testing_queue = TestingQueue()
        self.file_path_output = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output', 'outputPS6.txt'))
        self.file_output = open(self.file_path_output, 'a')
        self.file_output.truncate(0)

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
            # Enqueuing patients in the heap
            self.enqueuePatient(patient_id=int(patient_id))
            return patient_id
        except Exception as e:
            raise e

    def outputRegisteredPatientInfo(self):
        try:
            patients_in_queue = self.testing_queue.get_patients()
            self.file_output.write("-----------------registerPatient-----------------\n")
            self.file_output.write(f"No of patients added: {len(patients_in_queue)}\n")
            self.printFullQueue(patients_in_queue)
        except Exception as e:
            raise e

    def outputNewPatientRecords(self, name, age, patient_id):
        try:
            self.file_output.write("\n\n")
            self.file_output.write("-----------------new patient entered-----------------\n")
            self.file_output.write(f"Patient details: {name}, {age}, {patient_id}\n")
            self.printFullQueue()
        except Exception as e:
            raise e

    def printFullQueue(self, patients_in_queue=None):
        try:
            patients_in_queue = patients_in_queue if patients_in_queue else self.testing_queue.get_patients()
            self.file_output.write("Refreshed queue:\n")
            for patient in patients_in_queue[::-1]:
                patient_id = patient.patient_id
                self.file_output.write(f"{patient_id}, {self.patient_list.getPatientName(str(patient_id))}\n")
            self.file_output.write("------------------------------------------------")
        except Exception as e:
            raise e

    @Decorators.timer
    def servicePatients(self):
        try:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6b.txt'))
            with open(file_path, 'r') as file:
                patient_data = file.read().splitlines()
                for data in patient_data:
                    operation, parameters = data.split(":")
                    if operation == "newPatient":
                        name, age = parameters.split(",")
                        patient_id = self.registerPatient(name=name.strip(), age=age.strip())
                        self.testing_queue.sort()
                        self.outputNewPatientRecords(name=name, age=age, patient_id=patient_id)
                    elif operation == "nextPatient":
                        num_of_patients = parameters.strip()
                        self.nextPatient(num_of_patients)
        except Exception as e:
            raise e

    def enqueuePatient(self, patient_id):
        try:
            self.testing_queue.add(patient_id=int(patient_id))
        except Exception as e:
            raise e

    def nextPatient(self, num_of_patients):
        """
        It will output the patient id with highest priority and remove it from the heap
        :return:
        """
        self.file_output.write("\n\n")
        self.file_output.write(f"---- next patient : {num_of_patients} ---------------\n")
        for i in range(int(num_of_patients)):
            max_patient_id = self.testing_queue.max()
            # Dequeue patient who has completed testing
            self.dequeuePatient()
            self.file_output.write(f"Next patient for testing is: {max_patient_id}, {self.patient_list.getPatientName(str(max_patient_id))}\n")
        self.file_output.write("---------------------------------------------------\n")

    def dequeuePatient(self):
        return self.testing_queue.remove_max()
