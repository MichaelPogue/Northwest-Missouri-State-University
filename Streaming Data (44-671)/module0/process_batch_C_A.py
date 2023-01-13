import os
import csv
import pandas as pd

BASE_FILE = 'batchfile_0_farenheit.csv'
input_file_name = 'batchfile_2_kelvin.csv'
output_file_name = 'batchfile_3_farenheit.csv'

class processTemperatures:
    def __init__(self, BASE_FILE):
        self.BASE_FILE = BASE_FILE

    def convert_base_to_kelvin(self):
        isExist = os.path.exists('batchfile_2_kelvin.csv')
        if isExist is True:
            df.to_csv('batchfile_2_kelvin.csv')
        elif isExist is False:
            df = pd.DataFrame(list())
            df.to_csv('batchfile_2_kelvin.csv')


    def conver_far_to_kelvin(self):
        pass


pt = processTemperatures
pt.convert_base_to_kelvin(BASE_FILE)