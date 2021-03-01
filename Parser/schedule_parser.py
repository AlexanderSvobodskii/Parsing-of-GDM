import pandas as pd
import matplotlib as mpl
import numpy as np
import re
import os

def to_csv(input_file, output_file, parameters, keywords):
    
    # this function transform .inc-file to .csv file
    
    
    return

def read_schedule():
    # reading of shedule file
    
    
    return

def inspection():
    # inspection of correctness of fullness of .inc file
    return

def clean_schedule(input_file_list: list):
    
    # cleaning of .inc-file from excess comments
    
    for i in range(len(input_file_list)):
        if (('--' in input_file_list[i]) and ('\n' in input_file_list[i])):
            input_file_list[i] = input_file_list[i][:input_file_list[i].find("--")]
    
    for i in range(len(input_file_list)):
        if ('/' in input_file_list[i]):
            input_file_list[i] = input_file_list[i][:input_file_list[i].find("/") + 1]

    s1 = []
    for i in range(len(input_file_list)):
        if (input_file_list[i] != ''):
            s1.append(input_file_list[i])
            
    s2 = []
    for i in range(len(s1)):
        if ('\n' not in s1[i]):
            s1[i] = s1[i] + '\n' 
        if (s1[i] != '\n'):
                s2.append(s1[i])
    
    ret_str = ''
    for i in range(len(s2)):
        ret_str += s2[i]
    
    return ret_str

def parser_schedule():

    return

def extract_keyword_blocks():
    # extracting of keyword blocks from .inc-file
    
    return

def extract_lines():
    # extracting of string of .inc-file from blocks
    return

def parse_keyword_block():
    
    return

def parse_keyword_DATE_line(current_date_line: str):
    
    format_date = r'\d{2}\s+\w{3}\s+\d{4}' # regular expression for date
    string = re.findall(format_date, current_date_line) 
    
    return string[0]

def parse_keyword_COMPDATL_line(well_comp_line: str):
    
    well_comp_line = re.sub(r"'|(\s+/$)","",well_comp_line)
    well_comp_line = re.split(r"\s+", well_comp_line)
    
    well_string =''
    
    for i in range(len(well_comp_line)):
        if (i == 0):
            well_string = well_string + well_comp_line[i]
        else:
            well_string = well_string + ' ' + str(well_comp_line[i])
    
    well_array = default_params_unpacking_in_line(well_string)
    well_array = well_array.split(' ')
    
    well_comp_line_1 = []
    for i in range(len(well_array)):
        well_comp_line_1.append(well_array[i])
    
    return well_comp_line_1
    
    #return well_comp_line

def parse_keyword_COMPDAT_line(well_comp_line: str):
    
    well_comp_line = re.sub(r"'|(\s+/$)","",well_comp_line)
    well_comp_line = re.split(r"\s+", well_comp_line)
        
    well_string =''
    
    for i in range(len(well_comp_line)):
        if (i == 0):
            well_string = well_string + well_comp_line[i]
        else:
            well_string = well_string + ' ' + str(well_comp_line[i])
    
    well_array = default_params_unpacking_in_line(well_string)
    well_array = well_array.split(' ')
    
    well_comp_line_1 = [well_array[0], np.nan]
    for i in range(1, len(well_array), 1):
        well_comp_line_1.append(well_array[i])
    
    return well_comp_line_1

#--------------------------------------------------------------------

def decode(match):
    ch_st = set("*")
    res=""
    for i in range(0, len(str(match.group(0)))):
        if not match.group(0)[i] in ch_st:
            res +=  match.group(0)[i]
    string = ""
    for i in range(0,int(res[0])):
        string += " DEFAULT"
    return str(string)

def default_params_unpacking_in_line(well_comp_line: str):
    
    output_string = re.sub('([1-9]\*)', decode, well_comp_line)
    output_string = " ".join([el for el in output_string.split(' ') if el.strip()])
    
    return output_string

#---------------------------------------------------------------------