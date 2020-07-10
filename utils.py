"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList,MaxHeap
#from Scrapbook import MaxHeap
import os

class PatientUtils:
    def __init__(self):
        self.id_count = 1001
        self.patient_list = PatientList()
        self.testingQueue = MaxHeap(20)

    def registerPatient(self, name, age):
        try:
            patient_id = f"{self.id_count}{age}"
            self.patient_list.add(name=name, age=age, patient_id=patient_id)
            self.enqueuePatient(patient_id)
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
            self.file_output.write(PatientRecord[0] + " " + PatientRecord[1] + " " + PatientRecord[2] + "\n")
        else:
            self.file_output.write("No more patients in wait list \n")
        self._dequeuePatient(patid)

    def _dequeuePatient(self, PatId):
        self.testingQueue.test_dequeMax()

    def WriteSortedPatientRecord(self):
        n=self.testingQueue.size
        arr = [None] * n
        for i in range(0, n):
            arr[i] = self.testingQueue.Heap[i+1]

        for i in range(0, n):
            maxe = arr[i]%100
            for j in range(i+1, n):
                if (arr[j]%100 > maxe):
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
                    maxe=arr[i]%100
                elif (arr[j] % 100 == maxe):
                    if (arr[j]<arr[i]):
                        temp = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
                        maxe = arr[i] % 100

        for i in range(0, n):
            PatientRecord=self.patient_list.getPatientDetails(str(arr[i]))
            if PatientRecord:
                self.file_output.write(PatientRecord[0]+" "+PatientRecord[1]+" "+PatientRecord[2]+"\n")

    def read_patient_info(self,file_path,Filetype):
        try:
            flag=0
            with open(file_path, 'r') as file:
                if str(Filetype)=="Type2":
                    patient_data = file.read().splitlines()
                    for data in patient_data:
                        if "newPatient:" in data:
                            temp, new_data = data.split(":")
                            self.write_file(1,0)
                            name, age = new_data.split(",")
                            # Add patients to Patient Record List
                            self.registerPatient(name=name.strip(), age=age.strip())
                            self.SortQueue()# if this is included in enqueue function remove from here, it increases complexity but adheres to problem statement
                            self.WriteSortedPatientRecord()
                        elif "nextPatient:" in data:
                            temp, x = data.split(":")
                            self.write_file(2,x)
                            x = int(x)
                            while x > 0:
                                self.nextPatient()
                                x-=1
                        else:
                            self.file_output.write("____________Invalid input_________\n")
                elif str(Filetype)=="Type1":
                    patient_data = file.read().splitlines()
                    for data in patient_data:
                        name, age = data.split(",")
                        # Add patients to Patient Record List
                        self.registerPatient(name=name.strip(), age=age.strip())
                        flag+=1
                    self.SortQueue()# if this is included in enqueue function remove from here, it increases complexity but adheres to problem statement
                    self.write_file(0,flag)
                    self.WriteSortedPatientRecord()
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

