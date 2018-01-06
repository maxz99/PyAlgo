import math
from random import randint

def merge(arrL, arrR):
    resultLen = len(arrL) + len(arrR)
    result = [None]*resultLen
    iL = 0
    iR = 0
    iRes = 0

    while(iL < len(arrL) or iR < len(arrR)):
        if iL < len(arrL) and iR < len(arrR):
            if arrL[iL] <= arrR[iR]:
                result[iRes] = arrL[iL]
                iL+=1
                iRes+=1
            else:
                result[iRes] = arrR[iR]
                iR+=1
                iRes+=1
        elif iL < len(arrL):
            result[iRes] = arrL[iL]
            iRes+=1
            iL+=1
        elif iR < len(arrR):
            result[iRes] = arrR[iR]
            iRes+=1
            iR+=1
    return result       
  
    

def mergeSort(arr):
    if len(arr) == 1:
        return arr

    m = int(len(arr)/2)
    arrL = arr[0:m];

    arrR = arr[m:len(arr)];
    arrL = mergeSort( arrL)

    arrR = mergeSort(arrR)

    result = merge(arrL, arrR)
    return result;


rand = []
for x in range(10):
    rand.append(randint(1,999999))

a = mergeSort(rand)
print(a)