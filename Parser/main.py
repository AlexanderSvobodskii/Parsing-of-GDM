# -*- coding: utf-8 -*-

#-------------------file main.py------------------------

import schedule_parser as sp
import os

if __name__ == "__main__": 
    
    # This environment initiate inner code
    # only in case if this file was compiled directly.
    # If this file was imported to another files, this code will be ignored
    
    input_file = 'input_data_test_schedule.inc'
    output_file = ''
    
    # checking of existing of .inc file in given path
    ident = os.path.exists(input_file) 
    
    keywords = ('DATES', 'COMPDAT', 'COMPDATL')
    parameters = ("Date", "Well name", "Local grid name", "I", "J", "K upper", 
                  "K lower", "Flag of connection", "Saturation table", 
                  "Transmissibility", 
                  "Well bore diameter", "Effective Kh", "Skin factor", "D_factor")

    if (ident == True):
        
        input_file_list = []
        f = open(input_file, 'r')
        for line in f:
            input_file_list.append(line)
        str_input_file = sp.clean_schedule(input_file_list)
        
        #print(sp.parse_keyword_DATE_line(str_input_file))
        #print(sp.parse_keyword_COMPDATL_line("'W3' 'LGR1' 10 10  2   2 	OPEN 	1* 	1	2 	1 	3* 			1.0918 /"))
        #print(sp.parse_keyword_COMPDAT_line("'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"))
        #print(sp.default_params_unpacking_in_line("'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"))
    else :
        print('File does not exist in such directory')