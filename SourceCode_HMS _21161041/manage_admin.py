#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 16:30:11 2023

@author: aathira
"""

# Tkinter libraries
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import font

#Loading Classes
from appointment import Appointment
from doctor import Doctor
from patient import Patient
from admin import Admin

#Modules and libraries for file operations
import os
import file_operations as fo

#Modules specifc to tkinter window
import navigator_frame as nf
import validator_functions as vf
import doctor_management_frame as dmf
import patient_management_frame as pmf
import manage_admin as ma

#For generating Unique ID. Need to change
from uuid import uuid4


LARGE_FONT = ("Verdana", 16)




class view_admins_page (tk.Frame):
    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.controller = controller
        self.admins = admins
        self.appointments = appointments
        
        self.view_admin_data(controller, self.admins)

    
    def input_formatter(self,entries):
         #Converting user input entries into dictionary which can be read by Classes Patient and Appointment
         admin_data_dic = {}
         for key in entries:
             try:
                 if type(entries[key]) ==str:                   
                     admin_data_dic[(key)] = entries[key]
                 elif type(entries[key]) ==list:
                     admin_data_dic[[key]] = ', '.join(entries[key])
                 else:
                     admin_data_dic[(key)] = entries[key].get()
             except AttributeError:
                 showinfo('Error', 'Error occured in processing Admin Update request. Please re-try')
         return admin_data_dic


    # Function to confirm appointment by Admin
    def update_admin(self,controller, entries,admins):
        try:
            valid = False            
            admin_data_dic = self.input_formatter(entries)
            #Calling the validator function. Retirns status. If error, return the field causing error
            is_valid, message =vf.validate_appointment_data(admin_data_dic)
            
            if (is_valid):
                # Initialisinf Patient class with user input data    and then do the backend operation for appointment booking
                # Need to handle this portion gracefully
                admin_login = self.admins[0]  
                admin_update_status = admin_login.update_details(admin_data_dic,self.admins)
                if admin_update_status:
                    showinfo('Admin', ' Admin Data Updated Successfully')
                    
            else:
                showinfo('Error', message)
        except:
            showinfo('Error', 'Error in updating Admin Data!')

    def view_admin_data(self, controller, admins):
        
        try:
            self.data_refresh()
            # Need to handle this portion gracefully. 
            admin_login = self.admins[0]       
            self.entries = {}
                
            key = 'First Name'
            self.first_name = Label(self, text=key, width=20)
            self.first_name.place(x=20, y=120)
            self.first_name_entry = Entry(self)
            self.first_name_entry.place(x=200, y=120)
            self.first_name_entry.insert(0, admin_login.get_first_name())
            self.entries[key] = self.first_name_entry
                              
    
            key = 'Last Name'
            self.last_name = Label(self, text=key, width=20)
            self.last_name.place(x=420, y=120)
            self.last_name_entry = Entry(self)
            self.last_name_entry.place(x=600, y=120)
            self.last_name_entry.insert(0, admin_login.get_last_name())
            self.entries[key] = self.last_name_entry
                    
            key = 'Email'
            self.email = Label(self, text=key, width=20)
            self.email.place(x=20, y=160)
            self.email_entry = Entry(self)
            self.email_entry.place(x=200, y=160)
            self.email_entry.insert(0, admin_login.get_email())
            self.entries[key] = self.email_entry
            
            key = 'Admin ID'
            default_value = StringVar()
            default_value.set(admin_login.get_id())
            self.admin_ID = Label(self, text=key, width=20)
            self.admin_ID.place(x=420, y=160)
            self.admin_ID_entry = Entry(self, textvariable = default_value)
            self.admin_ID_entry.place(x=600, y=160)
            self.admin_ID_entry.config(state = 'readonly')
            # self.admin_ID_entry.insert(0, admin_login.get_id())            
            self.entries[key] = self.admin_ID_entry

            key = 'Address Line 1'
            self.address_line1 = Label(self, text=key, width=20)
            self.address_line1.place(x=20, y=200)
            self.address_line1_entry = Entry(self)
            self.address_line1_entry.place(x=200, y=200)
            self.address_line1_entry.insert(0, admin_login.get_address_line1())
            self.entries[key] = self.address_line1_entry    
    
            key = 'Address Line 2'
            self.address_line2 = Label(self, text=key, width=20)
            self.address_line2.place(x=420, y=200)
            self.address_line2_entry = Entry(self)
            self.address_line2_entry.place(x=600, y=200)
            self.address_line2_entry.insert(0, admin_login.get_address_line2())
            self.entries[key] = self.address_line2_entry
            
            key = 'Post Code'
            self.post_code = Label(self, text=key, width=20)
            self.post_code.place(x=20, y=240)
            self.post_code_entry = Entry(self)
            self.post_code_entry.place(x=200, y=240)
            self.post_code_entry.insert(0, admin_login.get_post_code())
            self.entries[key] = self.post_code_entry
    
            key = 'Contact Number'
            self.contact_number = Label(self, text=key, width=20)
            self.contact_number.place(x=420, y=240)
            self.contact_number_entry = Entry(self)
            self.contact_number_entry.place(x=600, y=240)
            self.contact_number_entry.insert(0, admin_login.get_contact_number())
            self.entries[key] = self.contact_number_entry
            
            key = 'username'
            self.username = Label(self, text=key, width=20)
            self.username.place(x=20, y=280)
            self.username_entry = Entry(self)
            self.username_entry.place(x=200, y=280)
            self.username_entry.insert(0, admin_login.get_user_name())
            self.entries[key] = self.username_entry

            key = 'password'
            self.password = Label(self, text=key, width=20)
            self.password.place(x=420, y=280)
            self.password_entry = Entry(self)
            self.password_entry.place(x=600, y=280)
            self.password_entry.insert(0, admin_login.get_password())
            self.entries[key] = self.password_entry
                
    
    
            self.button_confirm_appointment = tk.Button(self, text="Update",
                                                            command=lambda: self.update_admin(controller,self.entries, self.admins)).place(x=400, y=400)
            
            self.logout = tk.Button( self , text="Logout" , command=lambda: controller.show_frame( nf.LandingPage ) ).place( x=200 , y=400 )
            
            self.button_book_appointment = tk.Button(self, text="Back Home",
                                                     command=lambda: controller.show_frame(admin_page)).place(x=600, y=400)
        except:
            showinfo('Admin', 'Error in retrieving Admin data')
            


     # Refreshoing data
    def data_refresh(self):
        try:
             file_name = 'admin.txt'
             admin_list = fo.parse_data_file(file_name)
             self.admins=[]
             # For every dictionary on the admin_list, initialise Admin class and store in a list as list of objects
             # username is 'admin', password is 'password'
             
             for adm in admin_list:
                 admin = Admin(adm)
                 self.admins.append(admin)   
             
             # Initialising Doctors - Reading from file and defined as a list of Doctor Objects
             file_name = 'doctor.txt'
             doctor_list = fo.parse_data_file(file_name)
             self.doctors = []
             # For every dictionary on the doctor_list, initialise Doctor class and store in a list as list of objects
             
             for doc in doctor_list:
                 doctor = Doctor(doc)
                 self.doctors.append(doctor)
                 
                 
             # Initialising Appointments - Reading from file and defined as a list of Appointment Objects
             file_name = 'appointment.txt'
             appointment_list = fo.parse_data_file(file_name)
             self.appointments = []
             # For every dictionary on the appointment_list, initialise Appointment class and store in a list as list of objects
             
             for app in appointment_list:
                 appointment = Appointment(app)
                 self.appointments.append(appointment)
                 
             # Initialising Patients - Reading from file and defined as a list of Patient Objects
             file_name = 'patient.txt'
             patient_list = fo.parse_data_file(file_name)
             self.patients = []
             # For every dictionary on the appointment_list, initialise Appointment class and store in a list as list of objects
             
             for pat in patient_list:
                 patient = Patient(pat)
                 self.patients.append(patient)   
        except:
            pass