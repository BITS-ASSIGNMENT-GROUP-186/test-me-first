"""
This module is the entry point of the application and contains method to run and read patient information from the input
files
"""

import os
from utils import PatientUtils, TestingQueue


def read_patient_info(patient_utils):
    """
    Method to read the input file and register the patients
    :return: None
    """
    try:
        #patient_utils = PatientUtils()
        patient_utils.readAndOutputInitialPatients()
    except Exception as e:
        raise e


def sort_initial_queue():
    """
    Method to sort values in the queue according to age
    :return: None
    """
    try:
        pass
        #testing_queue = TestingQueue()
    except Exception as e:
        raise e

def service_patients(patient_utils):
    """

    :return:
    """
    try:
        #patient_utils = PatientUtils()
        patient_utils.servicePatients()
    except Exception as e:
        raise e


def run():
    patient_utils = PatientUtils()
    read_patient_info(patient_utils)
    #sort_initial_queue()
    service_patients(patient_utils)


if __name__ == "__main__":
    run()
