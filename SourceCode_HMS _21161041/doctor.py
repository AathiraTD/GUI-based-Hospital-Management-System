# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 02:51:37 2022

@author: aathira
"""

# Loading Class Modules
from appointment import Appointment
from person import Person

# Loading tkinter messagebox for error display
from tkinter.messagebox import showinfo

#For generating unique ID
import uuid
import hashlib

#Loading module for file operations
import file_operations as fo


#Inherited from Person
class Doctor (Person):
    """A class that deals with the Doctor operations"""
    #doc is a dictionary
    def __init__(self, doc):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """


        # self.__postcode = doc[('Post Code')]
        self.__speciality = doc[('Speciality')]
        self.__doctor_id = doc[('Doctor ID')]
        self.patients =''
        self.add_patient(doc[('Patients')])
        
        super().__init__(doc)
        
    
    def full_name(self) :
        full_name = self.get_first_name() + ' ' + self.get_last_name()
        return full_name

    
    def get_doctor_id (self):
        return self.__doctor_id
    
    def set_speciality(self, new_speciality):
        #ToDo7
        pass
    def set_speciality(self, new_speciality):
        #ToDo7
        pass
    def get_speciality(self):
        return self.__speciality
    #Method to link patient to the doctor
    def add_patient(self, patient_id) :
        if self.patients:
           self.patients += ','+patient_id
        else:
           self.patients = patient_id
    #Method to remove the patient from Doctor once the appointment is closed
    def remove_patient(self, patient_id):
        if self.patients:
            patient_list = self.patients.split(',')
            if patient_id in patient_list:
                patient_list.remove(patient_id)
                self.patients = ','.join(patient_list)
                
            
    def retrieve_patient (self):
        return self.patients

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
