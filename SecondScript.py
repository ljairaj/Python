import sys
import random
import os

## New Code
ListA = [1,2]
ListB = [10,20]
ListC = [100,200]
ListE = [1000,2000]

ListD = [ListA,ListB]

# iCnt=0
# for iVal1 in ListD[0]:
#     for iVal2 in ListD[1]:
#         for iVal3 in ListD[2]:
#             print("Output: ",str(iVal1)+" "+str(iVal2)+" "+str(iVal3))
#             iCnt += 1
# print("\nTotal Run: ", iCnt)

def recursive_fn(myList,iCnt,sVals):
    if(iCnt<len(myList)-1):
        for iVal in myList[iCnt]:
            sVals+=(str(iVal)+";")
            recursive_fn(myList, iCnt+1, sVals)
            print("iVal: ",iVal)
    elif(iCnt<len(myList)):
        for iVal in myList[iCnt]:
            print("Output: ",sVals+str(iVal))


    # if(iCnt<len(myList)):
    #     for iVal in myList[iCnt]:
    #         sVals += (str(iVal) + ";")
    #         # print("iVal1: ", iVal)
    #         # sVals += (str(iVal) + ";")
    #         recursive_fn(myList, iCnt + 1, sVals)
    #         # print("iVal2: ", iVal)
    #
    #     print("sVals: ", sVals)

sVals = ''
recursive_fn(ListD,0,sVals)

