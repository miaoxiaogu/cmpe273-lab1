import os
import glob
import tempfile
import heapq
import sys
import shutil
INT_MAX = sys.maxsize

def sort():
    index = 1
    "turn the unsorted_*.txt to sorted_*.txt files by change txt num"
    for file in glob.glob("input/unsorted_*.txt"):
        data = (open(file)).readlines()
        data = [int(i) for i in data]
        data.sort()
        sortedFile = open(os.path.join('input', 'sorted_'+str(index)+'.txt'),"w")
        for i in data:
            sortedFile.write(str(i)+"\n")
        sortedFile.close()
        index = index+1
    
    listOfFile = []
    for file in glob.glob("input/sorted_*.txt"):
        listOfFile.append(file)
    outFile = open("all_sorted.txt","w")
    indexList = [0]*10
    tempList = [-1]*10
    while(min(tempList) != INT_MAX):
        for i in range(10):
            if (indexList[i] == 100):
                tempList[i] = INT_MAX
            else:
                with open(listOfFile[i]) as temp:
                    tempList[i] = int((temp.readlines())[indexList[i]])
        min_value = min(tempList)
        min_index = tempList.index(min_value)
        indexList[min_index] += 1
        if (min_value != INT_MAX):
            outFile.write(str(min_value)+"\n")


sort()  
