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
