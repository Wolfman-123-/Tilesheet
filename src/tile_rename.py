# Created by Tyson Zwolsman
# 0.0.1

import shutil
import sys
import os
import csv

item_id = raw_input("Please enter the item id: ")
metadata = raw_input("Please enter the metadata value: ")

with open('itempanel.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        temp_id = row[0]
        temp_meta = row[1]
        temp_name = row[3]
        if temp_id == itemID:
            if temp_meta == metadata:
                print temp_name
