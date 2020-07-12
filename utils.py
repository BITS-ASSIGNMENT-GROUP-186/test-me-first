"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList, TestingQueue
import os


class PatientUtils:
    def __init__(self):
        self.id_count = 1001
        self.patient_id = None
        self.patient_list = PatientList()
        self.testing_queue = TestingQueue()
        self.file_output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output', 'outputPS6.txt'))
        self.file_output = open(self.file_output_path, 'w')

    def registerPatient(self, name, age):
        """ Method to register and enqueue patients in the heap """
        try:
            self.patient_id = f"{self.id_count}{age}"
            self.patient_list.add(name=name, age=age, patient_id=self.patient_id)
            self.enqueuePatient(self.patient_id)
            self.id_count += 1
        except Exception as e:
            raise e

    def enqueuePatient(self, patient_id):
        """ Method to enqueue patients in max heap """
        try:
            self.testing_queue.insert(int(patient_id))
        except Exception as e:
            raise e

    def sortQueue(self):
        """ Method to sort the queue """
        try:
            size = self.testing_queue.size
            if size > 1:
                self.testing_queue.upheap()
        except Exception as e:
            raise e

    def nextPatient(self):
        patient_id = self.testing_queue.top()
        patient_record = self.patient_list.getPatientDetails(str(patient_id))
        if patient_record:
            self.file_output.write(f"Next patient for testing is: {patient_record.patient_id}, {patient_record.name}\n")
        else:
            self.file_output.write("No more patients in the waiting list\n")
        self.dequeuePatient()

    def dequeuePatient(self):
        self.testing_queue.remove_max()

    @staticmethod
    def get_age(patient_id):
        return patient_id % 100

    def write_complete_patient_info(self):
        patient_list = self.testing_queue.heap[::-1]
        for patient_id in patient_list:
            patient_record = self.patient_list.getPatientDetails(str(patient_id))
            if patient_record:
                self.file_output.write(f"{patient_record.patient_id}, {patient_record.name}\n")
        self.file_output.write("------------------------------------------------------\n\n")

    def read_patient_info(self, file_path, patient_type):
        try:
            count = 0
            with open(file_path, 'r') as file:
                if patient_type == "NextPatients":
                    patient_data = file.read().splitlines()
                    for data in patient_data:
                        if "newPatient:" in data:
                            new_patient_data = data.split(":")[1]
                            name, age = new_patient_data.split(",")
                            # Add patients to Patient Record List
                            self.registerPatient(name=name.strip(), age=age.strip())
                            self.write_basic_patient_info(patient_type='new',
                                                          name=name.strip(),
                                                          age=age.strip(),
                                                          patient_id=self.patient_id)
                            self.sortQueue()
                            self.write_complete_patient_info()
                        elif "nextPatient:" in data:
                            next_patients_count = int(data.split(":")[1])
                            self.write_basic_patient_info(patient_type='next', count=next_patients_count)
                            while next_patients_count > 0:
                                self.nextPatient()
                                next_patients_count -= 1
                            self.file_output.write(f"------------------------------------------------------\n\n")
                        else:
                            self.file_output.write(f"Invalid input {data}. Did not find the valid keyword "
                                                   f"'newPatient' or 'nextPatient' in the input file\n")
                elif patient_type == "InitialPatients":
                    patient_data = file.read().splitlines()
                    for data in patient_data:
                        name, age = data.split(",")
                        # Add patients to Patient Record List
                        self.registerPatient(name=name.strip(), age=age.strip())
                        count += 1
                    # Running upheap after inserting all initial patients to have the order of 'n'
                    self.testing_queue.upheap()
                    self.testing_queue.heap_sort()
                    self.write_basic_patient_info(patient_type='initial', count=count)
                    self.write_complete_patient_info()
        except Exception as e:
            raise e

    def write_basic_patient_info(self, patient_type, patient_id=None, name=None, age=None, count=None):
        if patient_type == 'initial':
            self.file_output.write("-----------------Initial Queue-----------------------\n")
            self.file_output.write(f"No of patients added: {count}\n")
            self.file_output.write("Refreshed queue:\n")
        if patient_type == 'new':
            self.file_output.write("-----------------new patient entered------------------\n")
            self.file_output.write(f"Patient details: {name}, {age}, {patient_id}\n")
            self.file_output.write("Refreshed queue:\n")
        if patient_type == 'next':
            self.file_output.write(f"---------------next patient: {count} ---------------\n")
