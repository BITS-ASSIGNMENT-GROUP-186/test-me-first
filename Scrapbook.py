# this is for testing purpose only

import sys
class MaxHeap:
    def __init__(self, maxsize1):
        self.maxsize = maxsize1
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = 0
        self.FRONT = 1

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        temp=self.Heap[fpos]
        self.Heap[fpos]=self.Heap[spos]
        self.Heap[spos] = temp

     # Function to print the contents of the heap

    def Print(self):
        #print(self.size)
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    def extractMax(self):
        if self.size>0 :
            return self.Heap[self.FRONT]

    def test_dequeMax(self):
        #print(str(self.Heap[self.FRONT]) + " exchanged with " + str(self.size) + " ie :" + str(self.Heap[self.size]))
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.test_downheap(1)
        self.FRONT=1

    def test_upheap(self, i):
        i = int(i)
        parent = int(i / 2)
        # print(str(parent)+"is parent of"+str(self.Heap[i]))
        largest = self.Heap[i] % 100
        if (parent) > 0:
            if (i % 2 == 0):  # it is a left node
                if largest > (self.Heap[parent]) % 100:  # compare with parent
                    self.swap(i, parent)  # swap with parent if its bigger than parent
            else:
                if largest > (self.Heap[parent]) % 100:  # compare with parent
                    if largest > (self.Heap[i - 1]) % 100:  # compare with left sibling
                        self.swap(i, parent)  # swap with parent if its bigger than parent and left sibling
                    else:
                        self.swap(i - 1, parent)  # swap parent with left sibling
            self.test_upheap(parent)
    def test_downheap(self, i):
        FlagL=0
        FlagR=0
        largest = self.Heap[i] % 100
        n=self.size
        Left=i*2
        Right=Left+1
        if Left<=n: #Left exists
            FlagL=1
        if Right<=n: #right exists
            FlagR=1
        if FlagL==1:
            if largest < (self.Heap[Left]) % 100:  # compare with left child
                if FlagR==1:
                    if ((self.Heap[Left]) % 100)<((self.Heap[Right]) % 100):
                        self.swap(Right, i)  # swap right with parent if its bigger than both parent and left
                        self.test_downheap(Right)
                    else:
                        self.swap(Left, i)  # swap left with parent if its bigger than both parent and right
                        self.test_downheap(Left)
                else:
                    self.swap(Left, i)  # swap left with parent if its bigger than parent and right doesnt exist
                    self.test_downheap(Left)

    def test_insert(self, element):
        self.size += 1
        n=self.size
        self.Heap[n] = element
        if (n>1):
            #self.test_upheap(n)
            x=int(n/2) # index of parent
            #print (x)
            while x>0 :
                self.test_downheap(x)
                x-=1

if __name__ == "__main__":
    minHeap=MaxHeap(20)

    minHeap.test_insert(105)
    minHeap.test_insert(123)
    minHeap.test_insert(175)
    minHeap.test_insert(193)
    minHeap.test_insert(278)
    minHeap.test_insert(178)

    #minHeap.Print()
   # minHeap.test_upheap(minHeap.size)
    #minHeap.test_downheap(1)
    print('----------The maxHeap is of size:'+str(minHeap.size)+"____________________________")
    minHeap.Print()


    #minHeap.Print()
    #print("The Max val is " + str(minHeap.extractMax()))
