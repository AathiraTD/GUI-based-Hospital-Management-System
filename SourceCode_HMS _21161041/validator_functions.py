#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:40:34 2022

@author: aathira
"""

#For messages
from tkinter.messagebox import showinfo


def numeric_field_validate (entries):
    if entries.get().isdigit():
        return True
    else:
        return False
    
def numeric_field_validator (entries):
    if entries.isdigit():
        return True
    else:
        return False
    
def validate_appointment_data(entries):
    try:
        for field, value in entries.items():
            #Receiving tuple value from the function
            is_valid, message = validate(field, value)
            if not is_valid:
                break
    except:
        showinfo('Error', 'Error validating the field. Please re-try')
    finally:
        return is_valid, message
    


def validate(field, value):
    try:
        #Defining field types and validation types
        fields = {
        'First Name': {'type': 'string'},
        'userame': {'type': 'string'},
        'Symptoms': {'type': 'string'},
        'password': {'type': 'string'},
        'Last Name': {'type': 'string'},
        'Address Line 1': {'type': 'string'},
        'Address Line 2': {'type': 'string'},
        'Post Code': {'type': 'string'},
        'Age': {'type': 'numeric', 'max_digits': 3},
        'Email': {'type': 'email'},
        'Contact Number': {'type': 'phone_number'},}
        
        # Get the field definition from the fields dictionary
        if field in fields:
            field_def = fields[field]
        else:
            #Validation is not neeed for the field type
            return True, ''
        
        # Validate that the value is not empty. All field must be entered
        if not value:
            return False, f'{field} cannot be empty'
        
        # Validate the field type
        if field_def['type'] == 'string':
            # No additional validations for strings
            pass
        elif field_def['type'] == 'numeric':
            # Validate that the value is numeric
            if not value.isdigit():
                return False, f'{field} must be a number'
            # Validate the maximum number of digits
            if 'max_digits' in field_def and len(value) > field_def['max_digits']:
                return False, '{} cannot have more than {} digits'.format(field, field_def['max_digits'])
        elif field_def['type'] == 'email':
            # Validate that the value is a valid email address
            if '@' not in value or '.' not in value:
                return False, f'{field} is not a valid email address'
        elif field_def['type'] == 'phone_number':
            # Validate that the value is a phone number
            if not value.isdigit():
                return False, f'{field} must be a number'
            # Validate that the value is a 10-digit phone number
            if len(value) != 10:
                return False, f'{field} must be a 10-digit phone number'
        else:
            # Unknown field type
            return False, f'{field} has an unknown field type'
        
        # If all validations pass, return True
        return True, ''
    except:
        pass