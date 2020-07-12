"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList,MaxHeap
#from Scrapbook import MaxHeap
import os
import functools
import time


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
    def __init__(self):
        self.id_count = 1001
        self.patient_list = PatientList()
        self.testingQueue = MaxHeap(20)
        self.flag_next = 2

    def registerPatient(self, name, age):
        try:
            patient_id = f"{self.id_count}{age}"
            self.patient_list.add(name=name, age=age, patient_id=patient_id)
            self.enqueuePatient(patient_id)
            #print(str(self.id_count)+"____________________\n")
            #self.testingQueue.Print()

            self.id_count += 1
        except Exception as e:
            raise e

    def enqueuePatient(self, PatId):
        self.testingQueue.test_insert(int(PatId))

    def SortQueue(self):
        n=self.testingQueue.size
        if (n>1):
            self.testingQueue.test_upheap(n)

    def nextPatient(self):
        patid= self.testingQueue.extractMax()
        PatientRecord= self.patient_list.getPatientDetails(str(patid))
        if PatientRecord:
            self.flag_next=1
            self.file_output.write(PatientRecord[0] + " " + PatientRecord[1] + " " + PatientRecord[2] + "\n")
            self._dequeuePatient(patid)
        elif self.flag_next==1:
            self.file_output.write("No more patients in wait list \n")
            self.flag_next=0

    def _dequeuePatient(self, PatId):
        self.testingQueue.test_dequeMax(int(PatId))

    def WriteSortedPatientRecord(self):
        n = self.testingQueue.size
        arr = [None] * n
        for i in range(0, n):
            arr[i] = self.testingQueue.Heap[i + 1]

        for i in range(0, n):
            maxe = arr[i] % 100
            for j in range(i + 1, n):
                if (arr[j] % 100 > maxe):
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    maxe = arr[i] % 100
                elif (arr[j] % 100 == maxe):
                    if (arr[j] < arr[i]):
                        temp = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
                        maxe = arr[i] % 100
            # print
        for i in range(0, n):
            PatientRecord = self.patient_list.getPatientDetails(str(arr[i]))
            if PatientRecord:
                self.file_output.write(PatientRecord[0] + " " + PatientRecord[1] + " " + PatientRecord[2] + "\n")

    def read_patient_info_and_process(self,file_path,Filetype):
        try:
            flag=0
            with open(file_path, 'r') as file:
                if str(Filetype)=="Type2":
                    ctr=0
                    patient_data = file.read().splitlines()
                    for data in patient_data:
                        ctr+=1
                        if "newPatient:" in data:
                            temp, new_data = data.split(":")
                            if temp=="newPatient":
                                if len(new_data.split(","))==2:
                                    name, age = new_data.split(",")
                                    if (age.strip().isnumeric() and int(age)<100):
                                    # Add patients to Patient Record List
                                        self.write_file(1, 0)
                                        self.registerPatient(name=name.strip(), age=age.strip())
                                        self.WriteSortedPatientRecord()
                                    else:
                                        self.file_output.write("**Error in file 2 at line: "+str(ctr) +" : Invalid input for age :Age must be numeric and less than 100\n")
                                else:
                                    self.file_output.write("**Error in file 2 at line: "+str(ctr) +" : Invalid input:new Patient should have name and age details only\n")
                            else:
                                self.file_output.write("**Error in file 2 at line: "+str(ctr) +" : Invalid Keyword :'nextPatient' and 'newPatient' are only valid\n")
                        elif "nextPatient:" in data:
                            temp, x = data.split(":")
                            if (temp=="nextPatient" and len(data.split(":"))==2 and x.strip().isnumeric()):
                                self.write_file(2,x)
                                x = int(x)
                                while x > 0:
                                    self.nextPatient()
                                    x-=1
                            else:
                                self.file_output.write("**Error in file 2 at line: "+str(ctr) +" : Invalid entry for nextPatient.Valid format is 'nextPatient:x' where x is numeric\n")
                        else:
                            self.file_output.write("**Error in file 2 at line: "+str(ctr) +" : Invalid Keyword :'nextPatient' and 'newPatient' are only valid\n")
                elif str(Filetype)=="Type1":
                    ctr=0
                    patient_data = file.read().splitlines()
                    for data in patient_data:
                        ctr+=1
                        if (len(data.split(",")) == 2):
                            name, age = data.split(",")
                            if (age.strip().isnumeric() and int(age.strip()) < 100 ):
                                # Add patients to Patient Record List
                                self.registerPatient(name=name.strip(), age=age.strip())
                                flag+=1
                            else:
                                self.file_output.write("**Error in file 1 at line: "+str(ctr) +" : Invalid input for age :Age must be numeric and less than 100 \n")
                        else:
                            self.file_output.write("**Error in file 1 at line: "+str(ctr) +" : Invalid input:Record should have name and age details only \n")
                    self.write_file(0, flag)
                    if (flag>0):
                        self.WriteSortedPatientRecord()
                    else:
                        self.file_output.write("**Error in file 1: No valid inputs in File \n")

        except Exception as e:
            raise e
    def init_outputfile(self,file_path):
        try:
            self.file_output= open(file_path, 'w')
        except Exception as e:
            raise e

    def write_file(self,flag,count):
        if flag==0: #initial patient list
            self.file_output.write("-----------------Initial Queue-----------------\n")
            self.file_output.write(f"No of patients added: "+str(count)+"\n")
            self.file_output.write("Refreshed queue:\n")
        if flag==1:#new patient
            self.file_output.write("-----------------New Patient Entered-----------------\n")
            self.file_output.write("Refreshed queue:\n")
        if flag==2:#next patient
            self.file_output.write("---- next patient: "+str(count)+" ---------------\n")

