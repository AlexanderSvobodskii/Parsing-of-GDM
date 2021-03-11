# -*- coding: utf-8 -*-

#-------------------file main.py------------------------

import schedule_parser as sp
import os

if __name__ == "__main__": 
    
    # This environment initiate inner code
    # only in case if this file was compiled directly.
    # If this file was imported to another files, this code will be ignored
    
    input_file = 'input_data_test_schedule.inc'
    output_file = 'output_data_schedule.csv'
    
    # checking of existing of .inc file in given path
    ident = os.path.exists(input_file) 
    
    keywords = ('DATES', 'COMPDAT', 'COMPDATL', 'END')
    parameters = ("Well name", "Local grid name", "I", "J", "K upper", 
                  "K lower", "Flag of connection", "Saturation table", 
                  "Transmissibility", 
                  "Well bore diameter", "Effective Kh", "Skin factor", "D_factor", "Well orientation", "Effective radius")

    if (ident == True):
        
        sp.to_csv(input_file, output_file, parameters, keywords)

    else :
        print('File does not exist in such directory')