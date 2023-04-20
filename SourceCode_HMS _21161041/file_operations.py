# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 03:08:28 2022

@author: aathira
"""

# Module handling file operations of the system
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo




# Storing data to a file
def store_data_to_file(data_dic, file_name):
    try:
        with open(file_name, 'a+') as file:
            # Seek to the end of the file
            file.seek(0, 2)
            # Read the lines of the file
            lines = file.readlines()
            # Check if the file is empty or the last line is not empty or contains only whitespace
            if not lines or not lines[-1].strip():
                # If the file is empty or the last line is not empty or contains only whitespace, write the data to a new line
                file.write("\n")
            # Iterate over the keys in the data dictionary
            for i, key in enumerate(data_dic, start=1):
                # Write the key and value to the file, separated by an equals sign
                file.write(f"{key}={data_dic[key]}")
                # If this is not the last key-value pair, add the delimiter
                if i < len(data_dic):
                    file.write(" || ")
        return True
    except:
        return False



# Parsing data as a list of dictionaries. This will be used in uses cases which require iteration
def parse_data_file(file_name):
    try:
        data_list = []
        if os.path.exists(file_name):
            with open(file_name) as file:
                # Iterating through every line in the file
                for line in file:
                    # Skip empty lines or lines containing only whitespac
                    if not line.strip():
                        continue
                    data_dict = {}
                    # Retrieve the contents of each line into key and value.
                    for key_value in line.split(" || "):
                        # Storing key-vaue as tuple
                        (key, value) = key_value.split("=")
                        # Storing key and values ino a dictionary. Every key-value pair in the line will be a dicionary
                        data_dict[(key)] = value.strip("\n")
                    # Appending the dictionary to a list
                    data_list.append(data_dict)
            file.close()
    except:
        showinfo('Error', 'File error. Please consult Admin')
        file.close()
    finally:
        return data_list

# Check existence of a record in a file
def check_record_existence(data_dic, file_name):
    try:
        status = False
        if os.path.exists(file_name):
            appoint_list = parse_data_file(file_name)
            for dic in appoint_list:
                counter = 0
                for key in data_dic.keys():
                    if key in dic.keys() and data_dic[key] == dic[key]:
                        counter += 1
                        continue
                    else:
                        break
            if counter == len(data_dic):
                return True
            else:
                return False
        else:
            return False
    except:
        print("error")


# Search for a specifc record in the data file
def search_data_file(file_name, data_dic):
    try:
        status = False
        if os.path.exists(file_name):
            appoint_list = parse_data_file(file_name)
            for dic in appoint_list:
                search_result = []
                counter = 0
                for key in data_dic.keys():
                    if key in dic.keys() and data_dic[key] == dic[key]:
                        counter += 1
                        continue
                    else:
                        break
            if counter == len(data_dic):
                return True
            else:
                return False
        else:
            return False
    except:
        print("error")


# Searches for data and return the result
def data_search(file_name, data_dic):
    try:
        status = False
        if os.path.exists(file_name):
            appoint_list = parse_data_file(file_name)
            for dic in appoint_list:
                is_subset = all( k in dic and data_dic[k] == v for k, v in data_dic.items())

                if (is_subset):
                    return dic
                else:
                    continue
            return None
        else:
            return None
            print("No record exist")
    except:
        print("error")
        return None

def update_data_to_file(file_name, unique_id, entries):
    if os.path.isfile(file_name):
        try:
            #Converts file data into list of dictionary
            data_list = parse_data_file(file_name)
            found_entry = False
            #Identifies the specifc record to update from the list of dictionary. Update that record to new values
            for i in range(len(data_list)):
                if data_list[i].get(unique_id) == entries[unique_id]:
                    data_list[i] = entries
                    found_entry = True
                    break
            if not found_entry:
                raise ValueError(f'No entry found with the unique_id: {unique_id}')
            #Writing back to file
            with open(file_name, 'w') as file:
                for dictionary in data_list:
                    # Create a list of strings representing the key-value pairs
                    pairs = [f'{key}={value}' for key, value in dictionary.items()]
                    # Join the key-value pairs into a single string
                    line = ' || '.join(pairs)
                    # Write the string to the file
                    file.write(line + '\n')
            return True
        except Exception as e:
            raise e
    else:
        raise FileNotFoundError(f"{file_name} does not exist.")

    

#delete_data
def delete_data (file_name,del_id, entries):
    try:
        status = False
        if os.path.exists(file_name):
            data_list = parse_data_file(file_name)
            #Identifies the specifc record to delete from the list of dictionary.Remove that record            
            for i in range(len(data_list)):
                if data_list[i][del_id] == entries[del_id]:
                    data_list.remove(data_list[i])
                    break
            with open(file_name, 'w') as file:
               for dictionary in data_list:
                   # Create a list of strings representing the key-value pairs
                   pairs = [f'{key}={value}' for key, value in dictionary.items()]
                   # Join the key-value pairs into a single string
                   line = ' || '.join(pairs)
                   # Write the string to the file
                   file.write(line + '\n')
            file.close()
            status = True
        else:
            print("No record exist")
    except:
        print("Unexpected error in updating record")
    finally:
        return status

#Writing grouped patients data to file
def store_patient_groups(file_name, data_dic):
    try:
        write_status = False
        with open(file_name, 'w') as f:
            for key, value in data_dic.items():
                f.writelines(f"{key}:{', '.join(value)}\n")
            f.writelines(f"{key}={', '.join(value)}\n")
            write_status = True           
    except:
        pass
    finally:
        return write_status
    
    
#Parse patient groups data
def parse_patient_groups(file_name):
    try:
        patient_groups ={}
        with open(file_name) as f:
            for line in f:
               key, value = line.split(':')
               patient_groups[key] = value.strip().split(', ')
    except:
        pass
    finally:
        return patient_groups
    
#Update Patient by Family grouping file

def update_patient_group(listbox_patient):
    with open('patient_group.txt', 'w') as f:
        for i in range(listbox_patient.size()):
            # Get the group string from the list box
            group_string = listbox_patient.get(i)
            # Remove the trailing comma and space
            group_string = group_string.rstrip(", ")
            # Write the modified group string to the file
            f.write(listbox_patient.get(i) + '\n')