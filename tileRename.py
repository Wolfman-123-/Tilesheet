# Created by Tyson Zwolsman
# 0.0.1

import shutil
import sys
import os
import csv

itemID = raw_input("Please enter the item id: ")
metadata = raw_input("Please enter the metadata value: ")

with open('itempanel.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        tempID = row[0]
        tempMeta = row[1]
        tempName = row[3]
        if tempID == itemID:
            if tempMeta == metadata:
                print tempName
