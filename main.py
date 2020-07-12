"""
This module is the entry point of the application and initializes the patient utils method to service the patients from
both set of input files

Please read the README.md carefully before executing the program
"""

from utils import PatientUtils


def run():
    """
    Starting point of the whole program, calls out PatientUtils class and performs intended operations
    Raise exception in event of unexpected behavior
    """
    try:
        patient_utils = PatientUtils()
        # Read and register initial list of patients
        patient_utils.readAndOutputInitialPatients()
        # Read and service next batch of patients
        patient_utils.serviceNextPatients()
        print("Program finished successfully. Please check the results in 'outputPS6.txt' file")
    except Exception as e:
        # For writing every exception/validation to the output file
        patient_utils.writeErrorMessage(msg=f"{str(e)}")


if __name__ == "__main__":
    run()
