"""
This module is the entry point of the application and contains method to run and read patient information from the input
files
"""

import os
from utils import PatientUtils


def read_patient_info():
    """
    Method to read the input file and register the patients
    :return: None
    """
    try:
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6a.txt'))
        patient_utils = PatientUtils()
        with open(file_path, 'r') as file:
            patient_data = file.read().splitlines()
            for data in patient_data:
                name, age = data.split(",")
                patient_utils.registerPatient(name=name.strip(), age=age.strip())
        patient_utils.displayPatients()
    except Exception as e:
        raise e


def run():
    read_patient_info()


if __name__ == "__main__":
    run()
