"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList, TestingQueue
import functools
import time
import os


class Decorators:
    @staticmethod
    def timer(func):
        """Print the runtime of the decorated function"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
            return value
        return wrapper


class PatientUtils:
    """
    PatientUtils class containing various functions required for functioning of the program
    """
    def __init__(self):
        self.id_count = 1001
        self.patient_list = PatientList()
        self.testing_queue = TestingQueue()
        self.file_path_output = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output', 'outputPS6.txt'))
        self.file_output = open(self.file_path_output, 'a')
        self.file_output.truncate(0)
        self.input_file_a_errors = []
        self.input_file_b_errors = []

    def readAndOutputInitialPatients(self):
        """
        Reads initial input file "inputPS6a.txt" and stores records onto the priority queue
        """
        try:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6a.txt'))
            with open(file_path, 'r') as file:
                patient_data = file.read().splitlines()

                if not patient_data:
                    self.writeErrorMessage(msg=f"inputPS6a.txt is empty. No patients added.")
                    return

                for i, data in enumerate(patient_data):
                    try:
                        name, age = data.split(",")
                        name, age = name.strip(), age.strip()

                        # Basic validations
                        if not name.isalpha():
                            self.input_file_a_errors.append(f"inputPS6a.txt, line {i + 1}: Invalid value of name given '{name}'. "
                                                            f"Name can only be a string. Patient not registered.\n")
                            continue
                        if not age.isnumeric():
                            self.input_file_a_errors.append(f"inputPS6a.txt, line {i + 1}: Invalid value of age '{age}'. "
                                                            f"Age can only be a numeric. Patient not registered.\n")
                            continue
                        if int(age.strip()) < 1 or int(age.strip()) > 99:
                            self.input_file_a_errors.append(f"inputPS6a.txt, line {i + 1}: Age given is {age}. "
                                                            f"Age can't be lower than 1 nor greater than 99. Patient not registered.\n")
                            continue

                    except ValueError:
                        self.input_file_a_errors.append(f"inputPS6a.txt, line {i + 1}: Data '{data}' not in expected format."
                                                     f" Please input data in the format: name, age. Patient not registered.\n")
                        continue

                    # Add patients to Patient Record List
                    self.registerPatient(name=name, age=age)

            # Refreshing the testing queue once all the initial patients are registered
            self.testing_queue.heapSort()
            # Output the contents
            self.outputRegisteredPatientInfo()
            # Write all errors of input file PS6a, if any
            if self.input_file_a_errors:
                self.writeInputFileErrors(file_name="a")

        except Exception as e:
            raise e

    def registerPatient(self, name, age):
        """
        Registers the patient with name and age and assigns them a unique patient id
        :param name: name of the patient
        :param age: age of the patient
        :return: generated patient id
        """
        try:
            # Creating patient id
            patient_id = f"{self.id_count}{age}"
            # Adding patients to patientList
            self.patient_list.add(name=name, age=age, patient_id=patient_id)
            self.id_count += 1
            # Enqueuing patients in the heap
            self.enqueuePatient(PatId=int(patient_id))
            return patient_id
        except Exception as e:
            raise e

    def outputRegisteredPatientInfo(self):
        """
        Prints the already registered patients' name along with patient id on the output file "outputPS6.txt"
        """
        try:
            # Getting all patients
            patients_in_queue = self.testing_queue.get_patients()
            self.file_output.write("-----------------initial queue-----------------\n")
            self.file_output.write(f"No of patients added: {len(patients_in_queue)}\n")
            self.printFullQueue(patients_in_queue)
        except Exception as e:
            raise e

    def outputNewPatientRecords(self, name, age, patient_id):
        """
        Prints the newly registered patients' name along with patient id on the output file "outputPS6.txt"
        :param name: name of the patient
        :param age: age of the patient
        :param patient_id: patient id of the patient
        """
        try:
            self.file_output.write("\n\n")
            self.file_output.write("-----------------new patient entered-----------------\n")
            self.file_output.write(f"Patient details: {name}, {age}, {patient_id}\n")
            self.printFullQueue()
        except Exception as e:
            raise e

    def printFullQueue(self, patients_in_queue=None):
        """
        Prints all the patients currently present in the queue on the output file "outputPS6.txt"
        """
        try:
            patients_in_queue = patients_in_queue if patients_in_queue else self.testing_queue.get_patients()
            self.file_output.write("Refreshed queue:\n")
            for patient in patients_in_queue[::-1]:
                patient_id = patient.patient_id
                self.file_output.write(f"{patient_id}, {self.patient_list.getPatientName(str(patient_id))}\n")
            self.file_output.write("------------------------------------------------")
        except Exception as e:
            raise e

    def serviceNextPatients(self):
        """
        Reads the tags from the input file "inputPS6b.txt" and performs specific operation depending on the tag
        """
        try:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS6b.txt'))
            with open(file_path, 'r') as file:
                patient_data = file.read().splitlines()
                if not patient_data:
                    self.writeErrorMessage(msg=f"inputPS6b.txt is empty.")
                    return
                for i, data in enumerate(patient_data):
                    try:
                        operation, parameters = data.split(":")
                        if operation == "newPatient":
                            name, age = parameters.split(",")

                            if not name.strip().isalpha():
                                self.input_file_b_errors.append(
                                    f"inputPS6b.txt, line {i + 1}: Invalid value of name given '{name}'. "
                                    f"Name can only be a string. Patient not registered.\n")
                                continue

                            if int(age.strip()) < 1 or int(age.strip()) > 99:
                                self.input_file_b_errors.append(f"inputPS6b.txt, line {i + 1}: Age given is {age.strip()}. "
                                                                f"Age can't be lower than 1 nor greater than 99. Patient with name '{name.strip()}' not registered.\n")
                                continue

                            patient_id = self.registerPatient(name=name.strip(), age=age.strip())
                            # Refreshing the queue
                            self.testing_queue.heapSort()
                            self.outputNewPatientRecords(name=name, age=age, patient_id=patient_id)
                        elif operation == "nextPatient":
                            num_of_patients = parameters.strip()
                            self.nextPatient(num_of_patients)
                        else:
                            self.input_file_b_errors.append(f"inputPS6b.txt, line {i + 1}: Data '{data}' not in expected format. "
                                                            f"Please input data in the format: 'newPatient: name, age' or "
                                                            f"'nextPatient: number_of_patients_next_in_queue'. Input not considered.\n")
                    except ValueError:
                        self.input_file_b_errors.append(f"inputPS6b.txt, line {i + 1}: Data '{data}' not in expected format. "
                                                        f"Please input data in the format: 'newPatient: name, age' or "
                                                        f"'nextPatient: number_of_patients_next_in_queue'. Input not considered.\n")
                        continue

                    except IndexError:
                        self.file_output.write(30 * "*")
                        self.file_output.write("\n")
                        self.file_output.write("No more patients in queue!!\n")
                        self.file_output.write(30 * "*")
                        continue

                # Write all errors of input file PS6b, if any
                if self.input_file_b_errors:
                    self.writeInputFileErrors(file_name="b")
        except Exception as e:
            raise e

    def enqueuePatient(self, PatId):
        """
        Adding a new patient id onto the priority queue
        :param PatId: patient id of the patient
        :return: None
        """
        try:
            self.testing_queue.add(patient_id=int(PatId))
        except Exception as e:
            raise e

    def nextPatient(self, num_of_patients):
        """
        It will output the patient id with highest priority and remove it from the heap
        :return: None
        """
        try:
            if num_of_patients.isnumeric():
                self.file_output.write("\n\n")
                self.file_output.write(f"---- next patient : {num_of_patients} ---------------\n")
                for i in range(int(num_of_patients)):
                    max_patient_id = self.testing_queue.max()
                    # Dequeue patient who has completed testing
                    self._dequeuePatient(max_patient_id)
                    self.file_output.write(f"Next patient for testing is: {max_patient_id}, {self.patient_list.getPatientName(str(max_patient_id))}\n")
                self.file_output.write("---------------------------------------------------\n")
            else:
                raise ValueError
        except Exception as e:
            raise e

    def _dequeuePatient(self, PatId):
        """
        Removes the patient id of the patient which has been tested from the queue
        :param PatId: patient id of the patient to be removed
        :return: None
        """
        try:
            return self.testing_queue.remove_max()
        except Exception as e:
            raise e

    def writeErrorMessage(self, msg):
        """
        Writes error message, if encountered to the output file
        :param msg: error message to be written
        """
        try:
            msg_length = len(msg) if '\n' not in msg else len(msg.split("\n")[0])
            self.file_output.write("\n\n")
            self.file_output.write(msg_length * "*")
            self.file_output.write(f"\n{msg}\n")
            self.file_output.write(msg_length * "*")
            self.file_output.write("\n\n")
        except Exception as e:
            raise e

    def writeInputFileErrors(self, file_name):
        """
        Writes error message of the specific input file onto the output file
        :param file_name: file name which has encountered error
        """
        try:
            errors = self.input_file_a_errors if file_name == "a" else self.input_file_b_errors
            max_length = len(max(errors, key=len))
            self.file_output.write("\n\n")
            self.file_output.write(max_length * "*")
            self.file_output.write("\n")
            for error in errors:
                self.file_output.write(f"{error}")
            self.file_output.write(max_length * "*")
            self.file_output.write("\n\n")
        except Exception as e:
            raise e
