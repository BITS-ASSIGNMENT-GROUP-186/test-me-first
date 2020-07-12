"""
This module is the entry point of the application and initializes the patient utils method to service the patients from
both set of input files

Please read the README.md carefully before executing the program
"""

from utils import PatientUtils, Decorators


@Decorators.timer
def run():
    try:
        patient_utils = PatientUtils()
        # Read and register initial list of patients
        patient_utils.readAndOutputInitialPatients()
        # Read and service next batch of patients
        patient_utils.serviceNextPatients()
    except Exception as e:
        # For writing every exception/validation to the output file
        patient_utils.writeErrorMessage(msg=f"{str(e)}")


if __name__ == "__main__":
    run()
