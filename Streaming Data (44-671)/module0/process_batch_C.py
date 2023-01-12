"""
Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.

"""

import os
import csv

base_file_name = 'batchfile_0_farenheit.csv'
input_file_name = 'batchfile_2_kelvin.csv'
output_file_name = 'batchfile_3_farenheit.csv'

class processTemperatures:
    def __init__(self, base_file_name):
        self.base_file_name = base_file_name

    def convert_base_to_kelvin(self):
        isExist = os.path.exists('batchfile_2_kelvin.csv')
        if Exist = True
        pass

    def conver_far_to_kelvin(self):
        pass