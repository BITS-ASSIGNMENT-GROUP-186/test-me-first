"""
This module is the entry point of the application and contains method to run and read patient information from the input
files
"""

from utils import PatientUtils


def run():
    try:
        patient_utils = PatientUtils()
        # Read and register initial list of patients
        patient_utils.readAndOutputInitialPatients()
        # Read and service next of patients
        patient_utils.servicePatients()
    except Exception as e:
        print(f"Following error occurred while running the process: {str(e)}")


if __name__ == "__main__":
    run()
