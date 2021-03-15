import pandas as pd
import matplotlib as mpl
import numpy as np
import re
import os

def to_csv(input_file: str, output_file: str, parameters: tuple, keywords: tuple):
    
    # this function transform .inc-file to .csv file
    
    input_file_list = []
    f = open(input_file, 'r')
    for line in f:
        input_file_list.append(line)
    clean_file_list = clean_schedule(input_file_list)
        
    edit_file_list = edit_schedule(clean_file_list, keywords)
    
    blocks = extract_keyword_blocks(edit_file_list)
    
    data_list = []
    buff = []
    
    for i in blocks.keys():
        k = len(blocks[i])
        for j in range(k):
            blocks[i][j].insert(0, i)
            buff.append(blocks[i][j])
        data_list.append(buff)
        buff = []
    
    data_final = []
    for i in range(len(data_list)):
        k = len(data_list[i])
        for j in range(k):
            data_final.append(data_list[i][j])
            
    dates = []
    well_data = []
    
    for i in range(len(data_final)):
        dates.append(data_final[i][0])
        well_data.append(data_final[i][1:])
        
    df = pd.DataFrame(well_data, index = dates, columns=parameters)
    
    df.to_csv(output_file)
    
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
                
    return s2

def edit_schedule(clean_file_list: list, keywords: tuple):
    
    # function which edits uncommented schedule inc.-file
    #----------------------cleaning from excess keywords------------------
    i = 0
    while True:
        
        j = 0
        
        if (i == 0) and (clean_file_list[i][:clean_file_list[i].find("'\n'")] not in keywords):
            while (clean_file_list[i][:clean_file_list[i].find("'\n'")] not in keywords):
                clean_file_list.pop(i)
                
        if ((i > 0) and (clean_file_list[i] == '/\n') and (clean_file_list[i+1][:clean_file_list[i+1].find("'\n'")] not in keywords)):
            j = i+1
            while (clean_file_list[j][:clean_file_list[j].find("'\n'")] not in keywords):
                clean_file_list.pop(j)               
        
        if (clean_file_list[i] == 'END\n'):
            clean_file_list[i] = 'END'
            break
        i += 1
    #------------------------------------------------------------------------
    
    #--------------------cleaning from excess dates--------------------------
    i = 0
    while True:
        
        j = 0
        if (clean_file_list[i] == 'DATES\n'):
            j = i+1
            while (clean_file_list[j+1] != '/\n'):
                if (clean_file_list[j+1] != '/\n'):
                    clean_file_list.pop(j)
        
        if (clean_file_list[i] == 'END'):
            break
        i += 1
    #------------------------------------------------------------------------
    
    #ret_str = ''
    #for i in range(len(clean_file_list)):
        #ret_str += clean_file_list[i]
    
    #return ret_str
    return clean_file_list

def extract_keyword_blocks(clean_file_list: list):
    # extracting of keyword blocks from .inc-file and preparing information to writing to csv-file
    
    #TODO: я бы побил в будущем на более короткие функции - через месяц тебе будет тяжело и читать, и тестировать этот код
    
    for i in range(len(clean_file_list)):
        if (clean_file_list[i] == 'COMPDAT\n'):
            j = i+1
            while (clean_file_list[j] != '/\n'):
                clean_file_list[j] = parse_keyword_COMPDAT_line(clean_file_list[j])
                j+=1
        if (clean_file_list[i] == 'COMPDATL\n'):
            j = i+1
            while (clean_file_list[j] != '/\n'):
                clean_file_list[j] = parse_keyword_COMPDATL_line(clean_file_list[j])
                j+=1
    
    if (clean_file_list[0] == 'DATES\n'):
        
        data_dict = {}
        dates = ''
        data = []
        
        for j in range(0, len(clean_file_list), 1):
            if (clean_file_list[j] == 'DATES\n'):
                dates = parse_keyword_DATE_line(clean_file_list[j+1])
                k=j+2
                while (clean_file_list[k] != 'DATES\n'):
                    if ((clean_file_list[k] != 'COMPDAT\n') and (clean_file_list[k] != 'COMPDATL\n') and (clean_file_list[k] != '/\n')):
                        data.append(clean_file_list[k])
                   
                    k+=1              
                
                    if clean_file_list[k] == 'END':
                        break
                data_dict[dates] = data
                data = []
                dates = ''
                
        for comp_wells in data_dict.keys():
            if (data_dict[comp_wells] == []):
                data_dict[comp_wells] = [[np.nan for r in range(15)]]
        
    if (clean_file_list[0] != 'DATES\n'):
        
        data_dict = {}
        dates = ''
        data = []
        
        dates = 'INITIAL DATE'
        i = 0
        while (clean_file_list[i] != 'DATES\n'):
               if ((clean_file_list[i] != 'COMPDAT\n') and (clean_file_list[i] != 'COMPDATL\n') and (clean_file_list[i] != '/\n')):
                   data.append(clean_file_list[i])
               i+=1
        data_dict[dates] = data
        data = []
        dates = ''
        
        for j in range(i, len(clean_file_list), 1):
            if (clean_file_list[j] == 'DATES\n'):
                dates = parse_keyword_DATE_line(clean_file_list[j+1])
                k=j+2
                while (clean_file_list[k] != 'DATES\n'):
                    if ((clean_file_list[k] != 'COMPDAT\n') and (clean_file_list[k] != 'COMPDATL\n') and (clean_file_list[k] != '/\n')):
                        data.append(clean_file_list[k]) 
                   
                    k+=1              
                
                    if clean_file_list[k] == 'END':
                        break
                data_dict[dates] = data
                data = []
                dates = ''
        
        for comp_wells in data_dict.keys():
            if (data_dict[comp_wells] == []):
                data_dict[comp_wells] = [[np.nan for r in range(15)]]
            
    return data_dict

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
