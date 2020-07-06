"""
This module has the custom data structures used in the application

PatientRecord: A list containing the patient information including the patient’s name, age and the patient number (assigned by the program).

TestingQueue: A max heap containing the patient id sorted in order of next patient for testing based on the age of the patient.
"""


class PatientRecord:
    def __init__(self, name, age, id):
        self.patient_id = str(id) + str(age)
        self.name = name
        self.age = age
        self.left = None
        self.right = None


class TestingQueue:
    def __init__(self):
        pass
