"""
This module is the entry point of the application and contains method to run and read patient information from the input
files
"""
import os
from utils import PatientUtils

def run():
    #better to take user inputs and validate
    patient_utils = PatientUtils()

    file_path_output = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output', 'outputPS6.txt'))
    patient_utils.init_outputfile(file_path_output)

    file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6a.txt'))
    patient_utils.read_patient_info(str(file_path1))

    file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6b.txt'))
    patient_utils.read_patient_info(file_path2)

if __name__ == "__main__":
    run()
