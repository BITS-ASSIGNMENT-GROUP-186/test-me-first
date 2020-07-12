"""
This module is the entry point of the application and contains method to run and read patient information from the input
files
"""
import os
from utils import PatientUtils


def run():
    patient_utils = PatientUtils()

    initial_patients_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6a.txt'))
    patient_utils.read_patient_info(file_path=initial_patients_file_path, patient_type="InitialPatients")

    next_patients_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6b.txt'))
    patient_utils.read_patient_info(file_path=next_patients_file_path, patient_type="NextPatients")


if __name__ == "__main__":
    run()
