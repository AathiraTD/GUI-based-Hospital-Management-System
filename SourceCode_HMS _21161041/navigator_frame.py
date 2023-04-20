# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 02:51:37 2022

@author: aathira
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
import management_reports_frame as mrf

import functools


LARGE_FONT = ("Verdana", 12)


# Creating class for the GUI windows and pages
class MainWindow (tk.Tk):
    def __init__(self, admins, doctors, patients, appointments, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.set_window(self)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.admins = admins
        self.doctors = doctors
        self.appointments = appointments
        self.patients = patients

        self.frames = {}

        # All pages within the appilicaiton are listed.
        self.page_list = [
            LandingPage,
            pf.PatientPage,
            pf.BookAppointmentPage,
            pf.CheckAppointmentPage,
            mrf.DashboardPage,
            af.AdminLoginPage,
            af.DoctorManagementPage,
            af.AdminPage,
            af.PatientManagementPage,
            af.ViewAppointmentsPage,
            af.DoctorRegistrationPage,
            af.view_doctor_page,
            af.ViewAdminsPage,
            af.view_patients_page,
            af.GroupPatientsByFamily,
            af.ViewDischargedPatients,
            df.doctor_login_page,

        ]

        # Create partial function for each page with some arguments already set
        partial_funcs = {}
        for F in self.page_list:
            partial_funcs[F] = functools.partial(
                F, self.container, self, self.admins, self.doctors, self.patients, self.appointments
            )

        # Create frame for each page and store it in self.frames
        for F in self.page_list:
            frame = partial_funcs[F]()
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Load the landing page of the application
        self.show_frame(LandingPage)

    # Function to load the specific page and supress the other open pages
    def show_frame(self, cont):
        # re-loading the data
        self.data_refresh()

        # Create partial function for each page with some arguments already set
        partial_funcs = {}
        for F in self.page_list:
            partial_funcs[F] = functools.partial(
                F, self.container, self, self.admins, self.doctors, self.patients, self.appointments
            )

        # Create frame for each page and store it in self.frames
        for F in self.page_list:
            frame = partial_funcs[F]()
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Raise the frame for the specified page
        frame = self.frames[cont]
        frame.tkraise()

    # Functon defines the default dimensions of the window
    def set_window(self, cont):
        window_width = 1200
        window_height = 900

        # Get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.title("Hospital Management System")

    # Refresh the data. A better way is needed for this.
    def data_refresh(self):
        file_name = 'admin.txt'
        admin_list = fo.parse_data_file(file_name)
        self.admins = []
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
class LandingPage (tk.Frame):
    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        self.patient_icon = PhotoImage(file='./patient.png')
        button_patient = tk.Button(self,
                                   text="Patient Page",
                                   image=self.patient_icon,
                                   command=lambda: controller.show_frame(pf.PatientPage))
        button_patient.pack(side=LEFT, expand=TRUE)

        self.doctor_icon = PhotoImage(file='./doctor.png')
        button_doctor = tk.Button(self,
                                  text="Doctor Page",
                                  image=self.doctor_icon,
                                  command=lambda: controller.show_frame(df.doctor_login_page))
        button_doctor.pack(side=LEFT, expand=TRUE)

        self.admin_icon = PhotoImage(file='./admin.png')
        button_admin = tk.Button(self,
                                 text="Admin Login Page",
                                 image=self.admin_icon,
                                 command=lambda: controller.show_frame(af.AdminLoginPage))
        button_admin.pack(side=LEFT, expand=TRUE)
