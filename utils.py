"""
This module has reusable functions used throughout the application to support all the processes
"""
from data_structure import PatientList,TestingQueue
from Scrapbook import MaxHeap
import os

class PatientUtils:
    def __init__(self):
        self.id_count = 1001
        self.patient_list = PatientList()
        self.testingQueue = TestingQueue()
        self.sortedQueue= MaxHeap(20)


    def registerPatient(self, name, age):
        try:
            patient_id = f"{self.id_count}{age}"
            self.patient_list.add(name=name, age=age, patient_id=patient_id)
            self.enqueuePatient(patient_id)
            self.id_count += 1
            #self.sortedQueue.Print()
        except Exception as e:
            raise e


    def enqueuePatient(self, PatId):
        self.sortedQueue.insert(int(PatId))

    def nextPatient(self):
        patid= self.sortedQueue.extractMax()
        print(self.patient_list.getPatientDetails(str(patid)))
        self._dequeuePatient(patid)

    def _dequeuePatient(self, PatId):
        self.sortedQueue.dequeMax()

    def DisplaySortedPatientRecord(self):
        n=self.sortedQueue.size
        arr = [None] * n
        for i in range(0, n):
            arr[i] = self.sortedQueue.Heap[i+1]
            #print (arr[i])

        for i in range(0, n):
            maxe = arr[i]%100
            for j in range(i+1, n):
                if (arr[j]%100 > maxe):
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
                    maxe=arr[i]%100

        for i in range(0, n):
            print(self.patient_list.getPatientDetails(str(arr[i])))

    def read_patient_info(self,file_path):
        try:
            flag=0
            #file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', ))
            with open(file_path, 'r') as file:
                patient_data = file.read().splitlines()
                #print(patient_data)
                for data in patient_data:
                    if "newPatient:" in data:
                        temp, new_data = data.split(":")
                        print("---- new patient entered---------------")
                        print("Refreshed queue:")
                        #print(new_data)
                        name, age = new_data.split(",")
                        # Add patients to Patient Record List
                        self.registerPatient(name=name.strip(), age=age.strip())
                        self.DisplaySortedPatientRecord()
                    elif "nextPatient:" in data:
                        temp, x = data.split(":")
                        #print(x)

                        print("---- next patient: "+ x +" ---------------")
                        x = int(x)
                        while x > 0:
                            self.nextPatient()
                            x-=1
                    else :
                        flag+=1
                        name, age = data.split(",")
                        # Add patients to Patient Record List
                        self.registerPatient(name=name.strip(), age=age.strip())

                if flag>0 :
                    print("---- initial queue ---------------")
                    print("No of patients added: "+ str(flag))
                    print("Refreshed queue:")
                    #print(self.sortedQueue.size)
                    self.DisplaySortedPatientRecord()
                    flag-=1
                    #self.patient_list.display()

        except Exception as e:
            raise e

    def outputRegisteredPatientInfo(self):
        try:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output', 'outputPS6.txt'))
            patients_in_queue = self.testing_queue.get_patients()
            with open(file_path, 'w') as file:
                file.write("-----------------Initial Queue-----------------\n")
                file.write(f"No of patients added: {len(patients_in_queue)}\n")
                file.write("Refreshed queue:\n")
                for patient in patients_in_queue[::-1]:
                    patient_id = patient._value
                    file.write(f"{patient_id}, {self.patient_list.getPatientName(str(patient_id))}\n")
                file.write("------------------------------------------------")
        except Exception as e:
            raise e