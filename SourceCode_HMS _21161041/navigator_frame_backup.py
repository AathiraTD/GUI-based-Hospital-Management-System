#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 00:36:20 2023

@author: sgshaji
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 02:51:37 2022

@author: sgshaji
"""


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from appointment import Appointment
from doctor import Doctor
import os
import file_operations as fo

# Importing actor and operation classes
from appointment import Appointment
from doctor import Doctor
from admin import Admin
from patient import Patient

# Importing frame modules
import admin_frame as af
import doctor_frame as df
import patient_frame as pf
import doctor_management_frame as dmf
import appointment_frame as apf
import patient_management_frame as pmf
import view_doctor_frame as vdf
import management_reports_frame as mrf
import manage_admin as ma
import view_discharged_patients as vdp





LARGE_FONT = ("Verdana" , 12)



# Creating class for the GUI windows and pages
class main_window ( tk.Tk ):

    def __init__(self , admins, doctors, patients, appointments, *args , **kwargs):
        tk.Tk.__init__ ( self , *args , **kwargs )
        self.set_window ( self )
        self.container = tk.Frame ( self )
        self.container.pack ( side="top" , fill="both" , expand=True )
        self.container.grid_rowconfigure ( 0 , weight=1 )
        self.container.grid_columnconfigure ( 0 , weight=1 )
        self.admins = admins
        self.doctors = doctors
        self.appointments = appointments
        self.patients = patients

        self.frames = {}
        
        # All pages within the appilicaiton are listed.
        self.page_list = [landing_page , pf.PatientPage , df.doctor_login_page ,
                          pf.BookAppointmentPage , pf.CheckAppointmentPage, af.AdminLoginPage , af.DoctorManagementPage,
                          af.AdminPage, af.PatientManagementPage, apf.view_appointments_page, af.DoctorRegistrationPage,
                          af.view_doctor_page, mrf.DashboardPage, af.ViewAdminsPage, vdp.view_discharged_patients, af.view_patients_page, af.GroupPatientsByFamily]

        for F in self.page_list:
            try:
                if F.__name__=='confirm_appointment_page':
                    print(search_result)
                    frame = F ( self.container , self, search_result, self.admins, self.doctors, self.patients, self.appointments)
                else:
                    frame = F ( self.container , self, self.admins, self.doctors, self.patients, self.appointments)
             
                self.frames[F] = frame
    
                frame.grid ( row=0 , column=0 , sticky="nsew" )
            except KeyError:
                self.show_frame (af.confirm_appointment_page)
        
        # Loading the landing page of the application
        self.show_frame ( landing_page )
    
    # Function load the specifc page and supress the other open pages    
    def show_frame(self , cont):        
        #re-loading the data
        self.data_refresh()
        self.frames = {}
        for F in self.page_list:
            try:
                if F.__name__=='confirm_appointment_page':
                    frame = F ( self.container , self, search_result, self.admins, self.doctors, self.patients, self.appointments)
                else:
                    frame = F ( self.container , self, self.admins, self.doctors, self.patients, self.appointments)
             
                self.frames[F] = frame
    
                frame.grid ( row=0 , column=0 , sticky="nsew" )
            except KeyError:
                self.show_frame (af.confirm_appointment_page)
        
        frame = self.frames[cont]
        frame.tkraise ()
        
    # Functon defines the default dimensions of the window     
    def set_window(self , cont):
        window_width = 900
        window_height = 600

        # Get the screen dimension
        screen_width = self.winfo_screenwidth ( )
        screen_height = self.winfo_screenheight ( )

        # Find the center point
        center_x = int ( screen_width / 2 - window_width / 2 )
        center_y = int ( screen_height / 2 - window_height / 2 )

        # Set the position of the window to the center of the screen
        self.geometry ( f'{window_width}x{window_height}+{center_x}+{center_y}' )
        self.title ( "Hospital Management System" )
    
    # Refresh the data
    def data_refresh(self):
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


# Definition of landing page. Adding 3 button for the 3 roles - Patient, Doctor and Admin. Button click navigates to relevant role pages
class landing_page ( tk.Frame ):
    def __init__(self , parent , controller, admins, doctors, patients, appointments):
        tk.Frame.__init__ ( self , parent )

        self.patient_icon = PhotoImage ( file='./patient_navigate.png' )
        button_patient = tk.Button ( self ,
                                     text="Patient Page" ,
                                     image=self.patient_icon ,
                                     command=lambda: controller.show_frame ( pf.PatientPage ) )
        button_patient.pack ( side=LEFT , expand=TRUE )

        self.doctor_icon = PhotoImage ( file='./doctor_navigate.png' )
        button_doctor = tk.Button ( self ,
                                    text="Doctor Page" ,
                                    image=self.doctor_icon ,
                                    command=lambda: controller.show_frame ( df.doctor_login_page ) )
        button_doctor.pack ( side=LEFT , expand=TRUE )

        self.admin_icon = PhotoImage ( file='./admin_navigate.png' )
        button_admin = tk.Button ( self ,
                                   text="Admin Login Page" ,
                                   image=self.admin_icon ,
                                   command=lambda: controller.show_frame ( af.AdminLoginPage ) )
        button_admin.pack ( side=LEFT , expand=TRUE )

