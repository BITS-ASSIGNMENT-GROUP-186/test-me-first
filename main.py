"""
This module is the entry point of the application and contains method to run and read patient information from the input
files
"""

import os


def read_patient_info():
    try:
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6a.txt'))
        with open(file_path, 'r') as file:
            patient_data = file.read()
            print(patient_data)
    except Exception as e:
        raise e


def run():
    read_patient_info()


if __name__ == "__main__":
    run()
