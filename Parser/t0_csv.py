# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib as mpl
import numpy as np
import re

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
            input_file_list[i] = input_file_list[i][0:input_file_list[i].find("--")]

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
    
    format_date = '\d{2}\s\w{3}\s\d{4}' # regular expression for date
    string = re.findall(format_date, current_date_line) 
    
    return string[0]

def parse_keyword_COMPDAT_line(well_comp_line: str):
    
    format_compdat = ''
    
    return