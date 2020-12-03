#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Thu Dec  3 14:49:02 CET 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.
'''

import pandas as pd
import random

def generateRandomList_of_int(nEntries = 2, vMin = 0, vMax = 1):
    return [ random.randint(vMin,vMax) for _ in range(0,nEntries)]

def generateDF(nCol = 2, nEntries = 10, vMin = 0, vMax = 1):
    colList = [chr(letter) for letter in range(65, 65+nCol)]
    dfObj = pd.DataFrame(columns=colList)
    for coln in colList:
        dfObj[coln] = generateRandomList_of_int(nEntries=nEntries, vMin = vMin, vMax = vMax)
    return dfObj

def main():
    print(generateDF( nCol = 5, nEntries = 10, vMin = 0, vMax= 1000))

if __name__ == "__main__":
    main()
