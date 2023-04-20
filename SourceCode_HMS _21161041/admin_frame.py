# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:00:26 2022

@author: aathira
"""

# Tkinter libraries
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import font

# Loading Classes
from appointment import Appointment
from doctor import Doctor
from patient import Patient
from admin import Admin

# Modules and libraries for file operations
import os
import file_operations as fo

# Modules specifc to tkinter window
import navigator_frame as nf
import validator_functions as vf
import management_reports_frame as mrf

# For generating Unique ID. Need to change
from uuid import uuid4

# Calendar module for appointment date picking
import calendar
from datetime import datetime

LARGE_FONT = ("Verdana", 16)


# Propery definition of Admin login page

class AdminLoginPage (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        self.login_check(controller, admins)

    def login_check(self, controller, admins):
        self.login_form(controller, admins)

    def login_form(self, controller, admins):
        try:
            label = tk.Label(self, text="Admin Login Page", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            user_name = Label(self, text="User Name", width=20)
            user_name.place(x=20, y=120)
            self.__user_name_entry = Entry(self)
            self.__user_name_entry.place(x=200, y=120)

            password = Label(self, text="Password", width=20)
            password.place(x=20, y=160)
            self.__password_entry = Entry(self, show='*')
            self.__password_entry.place(x=200, y=160)

            self.__login = tk.Button(
                self, text="Login", command=lambda: self.login_validator(controller, admins))
            self.__login.pack(side=BOTTOM, anchor='center', pady=100)

        except:
            showinfo('Login', 'Unexpected Error in Login')

    # Clears the login credential in the form
    def login_form_clear(self, controller, admins):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.login_check(controller, admins)
        except ValueError:
            showinfo('Login', 'Unexpected Error')

    def clear_widgets(self):
        for widgets in self.winfo_children():
            widgets.destroy()

# Admin login validator. Initialises the class Admin to trigger login method of the class Admin
    def login_validator(self, controller, admins):
        try:

            admin_object_initiator = {}
            admin_object_initiator[('username')] = self.__user_name_entry.get()
            admin_object_initiator[('password')] = self.__password_entry.get()
            admin_object_initiator[('First Name')] = ''
            admin_object_initiator[('Last Name')] = ''
            admin_object_initiator[('Email')] = ''
            admin_object_initiator[('Age')] = ''
            admin_object_initiator[('Contact Number')] = ''
            admin_object_initiator[('Address Line 1')] = ''
            admin_object_initiator[('Address Line 2')] = ''
            admin_object_initiator[('Post Code')] = ''
            admin_object_initiator[('Admin ID')] = ''

            # This attribute will be used in all context of the logged in Admin
            self.admin_login = Admin(admin_object_initiator)
            
            # Calling the login() funciton defined in Admin class
            login_staus = self.admin_login.login(admin_object_initiator[(
                'username')], admin_object_initiator[('password')], admins)
            if (login_staus):
                self.login_form_clear(controller, admins)
                controller.show_frame(AdminPage)
            else:
                showinfo('Login', 'Invalid Login Credentials. Please try again')
        except:
            showinfo('Login', 'Unexpected Error in Login')

    # Refreshoing data
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
            

# Definition of landing page of admin. Inherited from AdminLoginPage

class AdminPage (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        self.data_refresh()
        self.admin_page_config(controller)

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

    # To override the method in super class. Doing nothing.
    def login_check(self, controller, admins):
        pass

    def admin_page_config(self, controller):
        try:
            label = tk.Label(self, text="Admin Dashboard", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            self.button_view_appointments = tk.Button(self, text="View Appointment",
                                                      command=lambda: controller.show_frame(ViewAppointmentsPage))
            self.button_view_appointments.pack(side=LEFT, expand=TRUE)

            self.button_doctor = tk.Button(self, text="Doctor Management",
                                           command=lambda: self.navigate_doctor_management(controller))
            self.button_doctor.pack(side=LEFT, expand=TRUE)

            self.button_patient = tk.Button(self, text="Patient Management",
                                            command=lambda: controller.show_frame(PatientManagementPage))
            self.button_patient.pack(side=LEFT, expand=TRUE)

            self.button_reoprt = tk.Button(self, text="Management Reports",
                                           command=lambda: controller.show_frame(mrf.DashboardPage))
            self.button_reoprt.pack(side=LEFT, expand=TRUE)

            self.button_admin = tk.Button(self, text="Manage Admin",
                                          command=lambda: controller.show_frame(ViewAdminsPage))
            self.button_admin.pack(side=LEFT, expand=TRUE)

            self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
                controller))
            self.logout.pack(side=TOP, anchor='center')

            self.button_discharged_patients = tk.Button(self, text="View Discharged Patients",
                                                        command=lambda: controller.show_frame(ViewDischargedPatients))
            self.button_discharged_patients.pack(side=LEFT, expand=TRUE)

        except:
            showinfo('Error', 'Unexpected Error')

    def logout_clear(self, controller):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.admin_page_config(controller)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def navigate_doctor_management(self, controller):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.admin_page_config(controller)
            controller.show_frame(DoctorManagementPage)
        except ValueError:
            showinfo(
                'Login', 'Error in navigating to Doctor Management. Please re-try')

# Page providing options to handle Doctor use cases by admin

class DoctorManagementPage (AdminLoginPage):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        super().__init__(parent, controller, admins, doctors, patients, appointments)

        self.load_buttons(controller)

    # To override the method in super class. Doing nothing.
    def login_check(self, controller, admins):
        pass

    def load_buttons(self, controller):

        self.label = tk.Label(self, text="Doctor Management", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)

        self.button_register_doctor = tk.Button(self, text="Register Doctor",
                                                command=lambda: controller.show_frame(DoctorRegistrationPage))
        self.button_register_doctor.pack(side=LEFT, expand=TRUE)

        self.button_view_doctor = tk.Button(self, text="View / Update / Delete Doctor",
                                            command=lambda: controller.show_frame(view_doctor_page))
        self.button_view_doctor.pack(side=LEFT, expand=TRUE)

        self.button_home = tk.Button(self, text="Admin Home",
                                     command=lambda: controller.show_frame(AdminPage)).pack(side=TOP, anchor='nw')

        self.button_logout = tk.Button(self, text="Logout",
                                       command=lambda: controller.show_frame(nf.LandingPage)).pack(side=TOP, anchor='ne')


# Inherits from parent class
class DoctorRegistrationPage(AdminLoginPage):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        super().__init__(parent, controller, admins, doctors, patients, appointments)
        self.clear_widgets()
        self.register_doctor_form(controller, admins, doctors)

    # #Overriding the parent class function
    # def login_check(self, controller, admins):
    #     pass

    def load_buttons(self, controller):
        self.label = tk.Label(
            self, text="Doctor Registration Form", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)

    # def clear_widgets(self):
    #     for widgets in self.winfo_children():
    #         widgets.destroy()

    def input_formatter(self, entries):
        entries['Doctor ID'] = ''
        entries['Patients'] = ''
        # Converting user input entries into dictionary which can be read by Classes Patient and Appointment
        doctor_data_dic = {}
        for key in entries:
            try:
                if type(entries[key]) == str:
                    doctor_data_dic[(key)] = entries[key]
                elif type(entries[key]) == list:
                    doctor_data_dic[[key]] = ', '.join(entries[key])
                else:
                    doctor_data_dic[(key)] = entries[key].get()
            except AttributeError:
                showinfo(
                    'Error', 'Error occured in processing Doctor registration. Please re-try')
        return doctor_data_dic

    # Clearing appointment booking form
    def form_clear(self, controller, admins, doctors):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.register_doctor_form(controller, admins, doctors)

    def func(self, value):

        self.clicked.set(value)
        self.entries['Speciality'] = self.clicked.get()

    # Function to create a booking request

    def register_doctor(self, entries, controller, admins, doctors):

        try:
            self.data_refresh()
            # Converting user input entries into dictionary which can be read by Classes Patient and Appointment
            doctor_data_dic = self.input_formatter(entries)

            # Calling the validator function. Retirns status. If error, return the field causing error
            is_valid, message = vf.validate_appointment_data(doctor_data_dic)

            # If input is valid, continue to register
            if (is_valid):
                # To perform the backend operation for Doctor registration
                self.admin_login = admins[0]
                # Returns 3 values. If doctor already exist, doctor registration status, doctor ID
                doc_exist, doctor_status, doctor_id = self.admin_login.register_doctor(
                    doctor_data_dic, self.doctors)
                # If doctor not exist - display the message specifc to file operation
                if not doc_exist:
                    # If file operation successful
                    if doctor_status:
                        showinfo('Doctor', str(doctor_id) +
                                 ' - Doctor Registered Successfully')
                        self.form_clear(controller, admins, doctors)
                    # Failed to add doctor to the system
                    else:
                        showinfo(
                            'Error', 'Error in Registering Doctor. Please re-try')
                # Doctor already exist in the system
                else:
                    showinfo('Error', 'Doctor Already exist in the System')
            else:
                showinfo('Error', message)
        except:
            showinfo(
                'Error', 'Error occured in processing Doctor Regidtration. Please re-try')

    def navigate_home(self, controller, admins, doctors):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.register_doctor_form(controller, admins, doctors)
        controller.show_frame(DoctorManagementPage)

    def register_doctor_form(self, controller, admins, doctors):
        try:
            self.entries = {}

            key = 'First Name'
            self.first_name = Label(self, text=key, width=20)
            self.first_name.place(x=20, y=120)
            self.first_name_entry = Entry(self)
            self.first_name_entry.place(x=200, y=120)
            self.entries[key] = self.first_name_entry

            key = 'Last Name'
            self.last_name = Label(self, text=key, width=20)
            self.last_name.place(x=420, y=120)
            self.last_name_entry = Entry(self)
            self.last_name_entry.place(x=600, y=120)
            self.entries[key] = self.last_name_entry

            key = 'Email'
            self.email = Label(self, text=key, width=20)
            self.email.place(x=20, y=160)
            self.email_entry = Entry(self)
            self.email_entry.place(x=200, y=160)
            self.entries[key] = self.email_entry

            key = 'Age'
            self.age = Label(self, text=key, width=20)
            self.age.place(x=420, y=160)
            self.age_entry = Entry(self)
            self.age_entry.place(x=600, y=160)
            self.entries[key] = self.age_entry

            key = 'Address Line 1'
            self.address_line1 = Label(self, text=key, width=20)
            self.address_line1.place(x=20, y=200)
            self.address_line1_entry = Entry(self)
            self.address_line1_entry.place(x=200, y=200)
            self.entries[key] = self.address_line1_entry

            key = 'Address Line 2'
            self.address_line2 = Label(self, text=key, width=20)
            self.address_line2.place(x=420, y=200)
            self.address_line2_entry = Entry(self)
            self.address_line2_entry.place(x=600, y=200)
            self.entries[key] = self.address_line2_entry

            key = 'Post Code'
            self.post_code = Label(self, text=key, width=20)
            self.post_code.place(x=20, y=240)
            self.post_code_entry = Entry(self)
            self.post_code_entry.place(x=200, y=240)
            self.entries[key] = self.post_code_entry

            key = 'Speciality'
            speciality_options = ['General - Fever, Flu etc', 'Dental',
                                  'ENT - Ear, Nose, Throat', 'Cardiology', 'Respiratory', 'Digestive', 'Other']
            self.clicked = StringVar()
            self.clicked.set("")
            self.speciality = Label(self, text=key, width=20)
            self.speciality.place(x=420, y=240)
            self.drop = OptionMenu(
                self, self.clicked, *speciality_options, command=self.func)
            self.drop.place(x=600, y=240)
            # self.symptoms_entry = Entry ( self )
            # self.symptoms_entry.place ( x=600 , y=240 )

            key = 'Contact Number'
            self.contact_number = Label(self, text=key, width=20)
            self.contact_number.place(x=20, y=280)
            self.contact_number_entry = Entry(self)
            self.contact_number_entry.place(x=200, y=280)
            self.entries[key] = self.contact_number_entry

            print(self.clicked.get())

            self.button_register = tk.Button(self, text="Register",
                                             command=lambda: self.register_doctor(self.entries, controller, admins, doctors), width=10).place(x=200, y=400)

            self.button_home = tk.Button(self, text="Clear", command=lambda: self.form_clear(
                controller, admins, doctors)).place(x=400, y=400)

            self.button_register = tk.Button(self, text="Back",
                                             command=lambda: self.navigate_home(controller, admins, doctors), width=10).place(x=600, y=400)

        except:
            showinfo('Doctor', 'Error in Doctor Registration')


# Inherits from AdminLoginPage
class view_doctor_page (AdminLoginPage):
    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        super().__init__(parent, controller, admins, doctors, patients, appointments)

        self.clear_widgets()

        self.label = tk.Label(self, text="List of Doctors", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)

        self.data_refresh()

        self.view_doctors(controller, admins, self.doctors,
                          self.patients, self.appointments)

    def logout_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_doctors(controller, admins, doctors,
                              patients, appointments)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'System Error. Please re-try')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_doctors(controller, admins, self.doctors,
                              self.patients, self.appointments)
            controller.show_frame(AdminPage)
        except:
            showinfo('Logout', 'System Error. Please re-try')

    def input_formatter(self, entries):
        # Converting user input entries into dictionary which can be read by Classes Patient and Appointment
        doctor_data_dic = {}
        for key in entries:
            try:
                if type(entries[key]) == str:
                    doctor_data_dic[(key)] = entries[key]
                elif type(entries[key]) == list:
                    patient_list = ', '.join(entries[key])
                    doctor_data_dic[(key)] = patient_list
                else:
                    doctor_data_dic[(key)] = entries[key].get()
            except AttributeError:
                showinfo(
                    'Error', 'Error occured in processing Doctor registration. Please re-try')
        return doctor_data_dic

    def func(self, value):
        self.clicked.set(value)
        self.search_result['Doctor'] = self.clicked.get()

    # Function to update doctor details
    def update_doctor(self, entries, controller, admins, doctors, patients, appointments):
        try:
            self.data_refresh()
            # Formatting the input
            doctor_data_dic = self.input_formatter(entries)
            # Validating filled values
            is_valid, message = vf.validate_appointment_data(doctor_data_dic)
            if is_valid:
                # Initialisinf Patient class with user input data    and then do the backend operation for appointment booking
                # Need to handle this portion gracefully
                self.admin_login = admins[0]
                # Only existing doctors can be updated. Retrieving update operation status along with Doctor ID
                doctor_update_status, doctor_id = self.admin_login.update_doctor(
                    doctor_data_dic, self.doctors, patients, appointments)
                if(doctor_update_status):
                    showinfo('Doctor', str(doctor_id) +
                             ' - Doctor Updated Successfully')
                    # Destroying the widgets in Ciew Doctoers page
                    for widgets in self.winfo_children():
                        widgets.destroy()
                    self.popup.destroy()

                    self.view_doctors(
                        controller, self.admins, self.doctors, self.patients, self.appointments)
                else:
                    showinfo(
                        'Error', 'Failed to update Doctor detailas. Please re-try')
            else:
                showinfo('Error', message)
        except:
            showinfo('Error', 'Error in updating Doctor details. Please re-try')

    # Function to detete doctor from he system
    def delete_doctor(self, entries, controller, admins, doctors, patients, appointments):
        try:
            doctor_data_dic = self.input_formatter(entries)
            self.admin_login = admins[0]
            doctor_delete_status, doctor_id = self.admin_login.delete_doctor(
                doctor_data_dic, doctors, patients, appointments)
            if(doctor_delete_status):
                showinfo('Doctor', str(doctor_id) +
                         ' Doctor Deleted Successfully')
                self.popup.destroy()
                # Destroy existing widegets and reload to refresh data
                for widgets in self.winfo_children():
                    widgets.destroy()
                self.view_doctors(controller, admins, doctors,
                                  patients, appointments)
                controller.show_frame(view_doctor_page)
            else:
                showinfo('Doctoe', 'Doctor is not present in the system')
        except:
            showinfo('Error', 'Unknown Error !')

    # Pop

    def on_row_click(self, event, controller, admins, doctors, patients, appointments):
        # Get the row that was clicked on
        self.search_result = {}
        self.row_id = self.doctor_list_view.identify_row(event.y)
        self.row = self.doctor_list_view.item(self.row_id)
        cols = ['Doctor ID', 'First Name', 'Last Name', 'Email',
                'Age', 'Contact Number', 'Speciality']
        col_values = self.row['values']
        print(col_values)
        self.search_data_dic = {}
        for i in range(0, len(cols)):
            self.search_data_dic[cols[i]] = col_values[i]

        # semd the dctionary for search

        file_name = "doctor.txt"
        # Need to handle this portion gracefully
        self.admin_login = admins[0]
        self.search_result = self.admin_login.view_doctor(
            self.search_data_dic, doctors)

        self.popup = tk.Toplevel()
        self.popup.geometry('900x600')
        # self.popup.geometry ("450*300")
        if len(self.search_result) != 0:
            # Appointment booking form widget definition

            # Defining another dictionary to handle edits.

            key = 'First Name'
            self.first_name = Label(self.popup, text=key, width=20)
            self.first_name.place(x=20, y=120)
            self.first_name_entry = Entry(self.popup)
            self.first_name_entry.place(x=200, y=120)
            self.first_name_entry.insert(0, self.search_result['First Name'])
            self.search_result[key] = self.first_name_entry

            key = 'Last Name'
            self.last_name = Label(self.popup, text=key, width=20)
            self.last_name.place(x=420, y=120)
            self.last_name_entry = Entry(self.popup)
            self.last_name_entry.place(x=600, y=120)
            self.last_name_entry.insert(0, self.search_result['Last Name'])
            self.search_result[key] = self.last_name_entry

            key = 'Email'
            self.email = Label(self.popup, text=key, width=20)
            self.email.place(x=20, y=160)
            self.email_entry = Entry(self.popup)
            self.email_entry.place(x=200, y=160)
            self.email_entry.insert(0, self.search_result['Email'])
            self.search_result[key] = self.email_entry

            key = 'Age'
            self.age = Label(self.popup, text=key, width=20)
            self.age.place(x=420, y=160)
            self.age_entry = Entry(self.popup)
            self.age_entry.place(x=600, y=160)
            self.age_entry.insert(0, self.search_result['Age'])
            self.search_result[key] = self.age_entry

            key = 'Address Line 1'
            self.address_line1 = Label(self.popup, text=key, width=20)
            self.address_line1.place(x=20, y=200)
            self.address_line1_entry = Entry(self.popup)
            self.address_line1_entry.place(x=200, y=200)
            self.address_line1_entry.insert(
                0, self.search_result['Address Line 1'])
            self.search_result[key] = self.address_line1_entry

            key = 'Address Line 2'
            self.address_line2 = Label(self.popup, text=key, width=20)
            self.address_line2.place(x=420, y=200)
            self.address_line2_entry = Entry(self.popup)
            self.address_line2_entry.place(x=600, y=200)
            self.address_line2_entry.insert(
                0, self.search_result['Address Line 2'])
            self.search_result[key] = self.address_line2_entry

            key = 'Post Code'
            self.post_code = Label(self.popup, text=key, width=20)
            self.post_code.place(x=20, y=240)
            self.post_code_entry = Entry(self.popup)
            self.post_code_entry.place(x=200, y=240)
            self.post_code_entry.insert(0, self.search_result['Post Code'])
            self.search_result[key] = self.post_code_entry

            key = 'Speciality'
            speciality_options = ['General - Fever, Flu etc', 'Dental',
                                  'ENT - Ear, Nose, Throat', 'Cardiology', 'Respiratory', 'Digestive', 'Other']
            self.clicked = StringVar()
            self.clicked.set(self.search_result['Speciality'])
            self.speciality = Label(self.popup, text=key, width=20)
            self.speciality.place(x=420, y=240)
            self.drop = OptionMenu(
                self.popup, self.clicked, *speciality_options, command=self.func)
            self.drop.config(state='disabled')
            self.drop.place(x=600, y=240)

            key = 'Contact Number'
            self.contact_number = Label(self.popup, text=key, width=20)
            self.contact_number.place(x=20, y=280)
            self.contact_number_entry = Entry(self.popup)
            self.contact_number_entry.place(x=200, y=280)
            self.contact_number_entry.insert(
                0, self.search_result['Contact Number'])
            self.search_result[key] = self.contact_number_entry

            self.button_update_doctor = tk.Button(self.popup, text="Update",
                                                  command=lambda: self.update_doctor(self.search_result, controller, admins, self.doctors, patients, appointments)).place(x=200, y=400)

            self.button_update_doctor = tk.Button(self.popup, text="Delete",
                                                  command=lambda: self.delete_doctor(self.search_result, controller, admins, self.doctors, patients, appointments)).place(x=400, y=400)

    def view_doctors(self, controller, admins, doctors, patients, appointments):
        self.data_refresh()
        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, admins, doctors, patients, appointments)).place(x=300, y=500)
        self.button_back_home = tk.Button(self, text="Back Home",
                                          command=lambda: controller.show_frame(DoctorManagementPage)).place(x=500, y=500)
        # hacky way need to implement gracefully
        self.admin_login = admins[0]
        doctor_list = self.admin_login.view_doctors(self.doctors)
        if len(doctor_list) == 0:
            showinfo(
                'No Data', "No Doctors present in the system. Please add Doctors")

        else:

            cols = ['Doctor ID', "First Name", "Last Name", 'Email',
                    'Age', 'Contact Number', 'Speciality', 'Patients']

            self.doctor_list_view = ttk.Treeview(
                self, column=cols, show='headings')

            self.doctor_list_view.column(
                "# 1", anchor=CENTER, minwidth=0, width=100)
            self.doctor_list_view.heading("# 1", text="Doctor ID")
            self.doctor_list_view.column(
                "# 2", anchor=CENTER, minwidth=0, width=100)
            self.doctor_list_view.heading("# 2", text="First Name")
            self.doctor_list_view.column(
                "# 3", anchor=CENTER, minwidth=0, width=100)
            self.doctor_list_view.heading("# 3", text="Last Name")
            self.doctor_list_view.column(
                "# 4", anchor=CENTER, minwidth=0, width=100)
            self.doctor_list_view.heading("# 4", text="Email")
            self.doctor_list_view.column(
                "# 5", anchor=CENTER, minwidth=0, width=100)
            self.doctor_list_view.heading("# 5", text="Age")
            self.doctor_list_view.column(
                "# 6", anchor=CENTER, minwidth=0, width=100)
            self.doctor_list_view.heading("# 6", text="Contact Number")
            self.doctor_list_view.column(
                "# 7", anchor=CENTER, minwidth=0, width=100)
            self.doctor_list_view.heading("# 7", text="Speciality")
            self.doctor_list_view.column(
                "# 8", anchor=CENTER, minwidth=0, width=100)
            self.doctor_list_view.heading("# 8", text="Patient IDs")

            # Iterating through the doctor list to format the data for display
            for dic in doctor_list:
                doc_list = []
                for key in cols:
                    if key in dic:
                        doc_list.append(dic[key])
                self.doctor_list_view.insert(
                    '', 'end', text="1", values=doc_list)
            self.doctor_list_view.place(width=1200, height=800)
            self.doctor_list_view.bind(
                '<Button-1>', lambda event: self.on_row_click(event, controller, admins, doctors, patients, appointments))
            self.doctor_list_view.pack()


# For Patient Management functions by Admin
class PatientManagementPage (AdminLoginPage):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        super().__init__(parent, controller, admins, doctors, patients, appointments)

        self.admins = admins
        self.doctors = doctors
        self.patients = patients
        self.appointments = appointments
        self.load_buttons(controller)

    # To override the method in super class. Doing nothing.

    def login_check(self, controller, admins):
        pass

    def load_buttons(self, controller):

        self.button_view_appointments = tk.Button(self, text="View Patients",
                                                  command=lambda: controller.show_frame(view_patients_page))
        self.button_view_appointments.pack(side=LEFT, expand=TRUE)

        self.button_doctor = tk.Button(self, text="Group patients by Family",
                                       command=lambda: controller.show_frame(GroupPatientsByFamily))
        self.button_doctor.pack(side=LEFT, expand=TRUE)

        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, admins, doctors, patients, appointments)).place(x=300, y=500)
        self.button_back_home = tk.Button(self, text="Back Home",
                                          command=lambda: self.back_home_clear(controller, self.admins, self.doctors, self.patients, self.appointments)).place(x=500, y=500)

    def logout_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors,
                               patients, appointments)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors,
                               patients, appointments)
            controller.show_frame(AdminPage)
        except:
            showinfo('Logout', 'Unexpected Error')


class view_patients_page (AdminLoginPage):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        super().__init__(parent, controller, admins, doctors, patients, appointments)

        self.admins = admins
        self.doctors = doctors
        self.patients = patients
        self.appointments = appointments

        self.view_patients(controller, self.admins,
                           self.doctors, self.patients, self.appointments)

    # To override the method in super class. Doing nothing.

    def login_check(self, controller, admins):
        pass

    def logout_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors,
                               patients, appointments)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors,
                               patients, appointments)
            controller.show_frame(AdminPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def func(self, value):
        self.clicked.set(value)
        self.search_result['Doctor'] = self.clicked.get()

    def on_row_click(self, event, controller, admins, doctors, patients, appointments):
        # Get the row that was clicked on
        self.search_result = {}
        self.row_id = self.patient_list_view.identify_row(event.y)
        self.row = self.patient_list_view.item(self.row_id)
        cols = ['Patient ID', "First Name", "Last Name", 'Email',
                'Age', 'Contact Number', 'Symptoms']

        col_values = self.row['values']
        self.search_data_dic = {}
        for i in range(0, len(cols)):
            self.search_data_dic[cols[i]] = col_values[i]

        # Need to handle this portion gracefully
        admin_login = admins[0]
        self.search_result = admin_login.view_patient(
            self.search_data_dic, patients)
        print(self.search_result)

        self.popup = tk.Toplevel()
        self.popup.geometry("900x600")
        if len(self.search_result) != 0:
            # Appointment booking form widget definition

            key = 'First Name'
            self.first_name = Label(self.popup, text=key, width=20)
            self.first_name.place(x=20, y=120)
            self.first_name_entry = Entry(self.popup)
            self.first_name_entry.place(x=200, y=120)
            self.first_name_entry.insert(0, self.search_result['First Name'])

            key = 'Last Name'
            self.last_name = Label(self.popup, text=key, width=20)
            self.last_name.place(x=420, y=120)
            self.last_name_entry = Entry(self.popup)
            self.last_name_entry.place(x=600, y=120)
            self.last_name_entry.insert(0, self.search_result['Last Name'])

            key = 'Email'
            self.email = Label(self.popup, text=key, width=20)
            self.email.place(x=20, y=160)
            self.email_entry = Entry(self.popup)
            self.email_entry.place(x=200, y=160)
            self.email_entry.insert(0, self.search_result['Email'])

            key = 'Age'
            self.age = Label(self.popup, text=key, width=20)
            self.age.place(x=420, y=160)
            self.age_entry = Entry(self.popup)
            self.age_entry.place(x=600, y=160)
            self.age_entry.insert(0, self.search_result['Age'])

            key = 'Address Line 1'
            self.address_line1 = Label(self.popup, text=key, width=20)
            self.address_line1.place(x=20, y=200)
            self.address_line1_entry = Entry(self.popup)
            self.address_line1_entry.place(x=200, y=200)
            self.address_line1_entry.insert(
                0, self.search_result['Address Line 1'])

            key = 'Address Line 2'
            self.address_line2 = Label(self.popup, text=key, width=20)
            self.address_line2.place(x=420, y=200)
            self.address_line2_entry = Entry(self.popup)
            self.address_line2_entry.place(x=600, y=200)
            self.address_line2_entry.insert(
                0, self.search_result['Address Line 2'])

            key = 'Post Code'
            self.post_code = Label(self.popup, text=key, width=20)
            self.post_code.place(x=20, y=240)
            self.post_code_entry = Entry(self.popup)
            self.post_code_entry.place(x=200, y=240)
            self.post_code_entry.insert(0, self.search_result['Post Code'])

            key = 'Symptoms'
            self.symptoms = Label(self.popup, text=key, width=20)
            self.symptoms.place(x=420, y=240)
            self.symptoms_entry = Entry(self.popup)
            self.symptoms_entry.place(x=600, y=240)
            self.symptoms_entry.insert(0, self.search_result['Symptoms'])

            key = 'Contact Number'
            self.contact_number = Label(self.popup, text=key, width=20)
            self.contact_number.place(x=20, y=280)
            self.contact_number_entry = Entry(self.popup)
            self.contact_number_entry.place(x=200, y=280)
            self.contact_number_entry.insert(
                0, self.search_result['Contact Number'])

    def view_patients(self, controller, admins, doctors, patients, appointments):
        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, admins, doctors, patients, appointments)).place(x=300, y=400)
        self.button_back_home = tk.Button(self, text="Back",
                                          command=lambda: self.back_home_clear(controller, admins, doctors, patients, appointments)).place(x=500, y=400)
        # hacky way need to implement gracefully
        self.admin_login = self.admins[0]
        patient_list = self.admin_login.view_patients(self.patients)
        if len(patient_list) == 0:
            print("No appointments to Display")

        else:

            cols = ['Patient ID', "First Name", "Last Name", 'Email',
                    'Age', 'Contact Number', 'Symptoms']

            self.patient_list_view = ttk.Treeview(
                self, column=cols, show='headings')
            self.patient_list_view.column(
                "# 1", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 1", text="Patient ID")
            self.patient_list_view.column(
                "# 2", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 2", text="First Name")
            self.patient_list_view.column(
                "# 3", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 3", text="Last Name")
            self.patient_list_view.column(
                "# 4", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 4", text="Email")
            self.patient_list_view.column(
                "# 5", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 5", text="Age")
            self.patient_list_view.column(
                "# 6", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 6", text="Contact Number")
            self.patient_list_view.column(
                "# 7", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 7", text="Symptoms")

            # Iterating through the doctor list to foramt the data for display
            for dic in patient_list:
                print()
                pat_list = []
                for key in cols:
                    if key in dic:
                        pat_list.append(dic[key])
                self.patient_list_view.insert(
                    '', 'end', text="1", values=pat_list)
            self.patient_list_view.place(width=600, height=800)
            self.patient_list_view.bind(
                '<Button-1>', lambda event: self.on_row_click(event, controller, admins, doctors, patients, appointments))
            self.patient_list_view.pack()


# Admin can group patients based on Familty. The family criteria is determined by Post Code
class GroupPatientsByFamily (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        self.admins = admins
        self.doctors = doctors
        self.patients = patients
        self.appointments = appointments

        self.group_patients(controller)

    def logout_clear(self, controller):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.group_patients(controller)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def back_home_clear(self, controller):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.group_patients(controller)
            controller.show_frame(AdminPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def group_patients(self, controller):
        try:

            self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
                controller, admins, doctors, patients, appointments)).place(x=300, y=400)
            self.button_back_home = tk.Button(self, text="Back Home",
                                              command=lambda: self.back_home_clear(controller)).place(x=500, y=400)
            self.add_button = tk.Button(
                self, text="Group Patients", command=lambda: self.group_patient_form(controller))
            self.add_button.pack()

            self.generate_patient_groups()

            self.display_groups()

        except:
            showinfo('Error', 'Error in loading groping patients of same family')

    # Generate a file for the default grouping - by default patients grouped based on post code. This is modifiable by admin
    def generate_patient_groups(self):
        try:
            file_name = 'patient_group.txt'
            if os.path.exists(file_name):
                pass
            else:
                self.patient_groups = {}
                for patient in self.patients:
                    postcode = patient.get_post_code()
                    if postcode not in self.patient_groups:
                        self.patient_groups[postcode] = []
                    full_name = patient.full_name()
                    self.patient_groups[postcode].append(full_name)
                write_status = fo.store_patient_groups(
                    file_name, self.patient_groups)
                if write_status:
                    pass
                else:
                    showinfo(
                        'Error', 'Failed to default group patients by postcode')
        except:
            pass

    # Method to display groups
    def display_groups(self):
        try:

            label = tk.Label(
                self, text="Double Click on the group to delete a group. To create a new group Click on the Group patients buton. Enter Post Code as the grouping criteria")
            label.pack(side='top', pady=10)

            # creating a list-box to display the groups of patients
            self.listbox_patient = tk.Listbox(self)
            self.listbox_patient.place(x=50, y=100, width=600, height=300)
            file_name = 'patient_group.txt'
            self.patient_groups = fo.parse_patient_groups(file_name)
            for postcode, names in self.patient_groups.items():
                group_string = f"{postcode}: "
                for name in names:
                    group_string += name + ", "
                self.listbox_patient.insert(tk.END, group_string)

            # Bind a function to the list box's <Button-1> event
            def open_window(event):
                if self.listbox_patient.curselection():
                    # Get the index of the selected item
                    index = self.listbox_patient.curselection()[0]
                    # Get the value of the selected item
                    value = self.listbox_patient.get(index)
                    # Open a new window and display the value
                    new_window = Toplevel()
                    Label(new_window, text=value).pack()
                    # Add a button to delete the item

                    def delete_item():
                        self.listbox_patient.delete(index)
                        fo.update_patient_group(self.listbox_patient)
                        new_window.destroy()
                    Button(new_window, text="Delete",
                           command=delete_item).pack()
            self.listbox_patient.bind("<Button-1>", open_window)
        except:
            pass

    def add_patient(self, name, postcode):
        try:
            # Add the patient to the appropriate group in the dictionary
            if postcode not in self.patient_groups:
                self.patient_groups[postcode] = []
            self.patient_groups[postcode].append(name)

            # writing the changes to file
            file_name = 'patient_group.txt'
            write_status = fo.store_patient_groups(
                file_name, self.patient_groups)
            if write_status:
                pass
            else:
                showinfo(
                    'Error', 'Failed to group patients by postcode. Please re-try')
            # Update the listbox to display the new patient group
            self.listbox_patient.insert(tk.END, f"{postcode}: {patient.name}")
        except:
            pass

    def group_patient_form(self, controller):
        # Create a form to collect patient information
        self.form = tk.Toplevel(self)
        self.form.title("Add Patient")
        self.form.resizable(False, False)

        # Create widgets for the form
        name_label = tk.Label(self.form, text="Name:")
        self.name_entry = tk.Entry(self.form)
        postcode_label = tk.Label(self.form, text="Postcode:")
        self.postcode_entry = tk.Entry(self.form)
        submit_button = tk.Button(
            self.form, text="Submit", command=lambda: self.add_patient_submit(controller))

        # Add the widgets to the form
        name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        postcode_label.grid(row=1, column=0)
        self.postcode_entry.grid(row=1, column=1)
        submit_button.grid(row=2, column=1, pady=10)

    def add_patient_submit(self, controller):
        # Get the patient information from the form
        name = self.name_entry.get()
        postcode = self.postcode_entry.get()
        # Add the patient to the patient groups
        self.add_patient(name, postcode)
        # Close the form
        self.form.destroy()
        self.add_button.destroy()
        self.listbox_patient.destroy()
        for widgets in self.winfo_children():
            widgets.destroy()
        self.group_patients(controller)


# Manage Admin Data
class ViewAdminsPage (tk.Frame):
    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller
        self.admins = admins
        self.appointments = appointments

        self.view_admin_data(controller, self.admins)

    def input_formatter(self, entries):
        # Converting user input entries into dictionary which can be read by Classes Patient and Appointment
        admin_data_dic = {}
        for key in entries:
            try:
                if type(entries[key]) == str:
                    admin_data_dic[(key)] = entries[key]
                elif type(entries[key]) == list:
                    admin_data_dic[[key]] = ', '.join(entries[key])
                else:
                    admin_data_dic[(key)] = entries[key].get()
            except AttributeError:
                showinfo(
                    'Error', 'Error occured in processing Admin Update request. Please re-try')
        return admin_data_dic

    # Function to confirm appointment by Admin
    def update_admin(self, controller, entries, admins):
        try:
            valid = False
            admin_data_dic = self.input_formatter(entries)
            # Calling the validator function. Retirns status. If error, return the field causing error
            is_valid, message = vf.validate_appointment_data(admin_data_dic)

            if (is_valid):
                # Initialisinf Patient class with user input data    and then do the backend operation for appointment booking
                # Need to handle this portion gracefully
                admin_login = self.admins[0]
                admin_update_status = admin_login.update_details(
                    admin_data_dic, self.admins)
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
            self.admin_ID_entry = Entry(self, textvariable=default_value)
            self.admin_ID_entry.place(x=600, y=160)
            self.admin_ID_entry.config(state='readonly')
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
            self.contact_number_entry.insert(
                0, admin_login.get_contact_number())
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
                                                        command=lambda: self.update_admin(controller, self.entries, self.admins)).place(x=400, y=400)

            self.logout = tk.Button(self, text="Logout", command=lambda: controller.show_frame(
                nf.LandingPage)).place(x=200, y=400)

            self.button_book_appointment = tk.Button(self, text="Back Home",
                                                     command=lambda: controller.show_frame(AdminPage)).place(x=600, y=400)
        except:
            showinfo('Admin', 'Error in retrieving Admin data')

     # Refreshoing data

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


# Appointment Management Frame
class ViewAppointmentsPage (tk.Frame):
    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        self.data_refresh()

        self.admins = admins
        self.doctors = doctors
        self.patients = patients
        self.appointments = appointments
        self.controller = controller

        self.view_appointments(controller, self.appointments)

    def logout_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_appointments(controller, self.appointments)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_appointments(controller, self.appointments)
            controller.show_frame(AdminPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def checkbox_clicked_admit(self):
        if self.admit_request_var.get() == 1:
            self.search_result['Admit'] = 'Admit'

    def checkbox_clicked_discharge(self):
        if self.admit_request_var.get() == 1:
            self.search_result['Admit'] = 'Discharged'

    def complete_appointment_clicked(self):
        if self.close_appointment_var.get() == 1:
            self.search_result['Status'] = 'Completed'
        else:
            self.search_result['Status'] = 'Confirmed'

    # Function to confirm appointment by Admin
    def confirm_appointment(self, entries, controller, admins, doctors, patients, appointments):

        try:
            # Changing the Appointment Status - To handle corner case if Status key is not changes after assigning a doctor. Post fixing that bug can remove this
            if entries['Status'] == 'Pending':
                entries['Status'] = 'Confirmed'
            is_valid, message = vf.validate_appointment_data(entries)

            if (entries['Appointment Date'] == ''):
                is_valid = False
                message = 'Please select appointment date'
            if (is_valid):
                # Initialisinf Patient class with user input data    and then do the backend operation for appointment booking
                # Need to handle this portion gracefully
                admin_login = self.admins[0]
                appointment_status = admin_login.confirm_appointment(
                    entries, doctors, patients, appointments)
                if(appointment_status):
                    showinfo(
                        'Appointment', entries['Appointment ID'] + ' - Appointment is processed')
                    self.popup.destroy()
                    for widgets in self.winfo_children():
                        widgets.destroy()
                    self.view_appointments(controller, self.appointments)
            else:
                showinfo('Error', message)
        except:
            showinfo(
                'Error', 'System error in confirming the request. Please re-try')

    # Pop
    def on_row_click(self, event, controller, admins, doctors, patients, appointments):
        # Get the row that was clicked on
        self.search_result = {}
        self.row_id = self.appointment_list_view.identify_row(event.y)
        self.row = self.appointment_list_view.item(self.row_id)
        cols = ['Appointment ID', 'First Name', 'Last Name', 'Email',
                'Age', 'Contact Number', 'Symptoms', 'Status']
        col_values = self.row['values']

        self.search_data_dic = {}

        # This handles index out of range exception as it is possible that col_values may have few elements than cols
        for i in range(min(len(cols), len(col_values))):
            self.search_data_dic[cols[i]] = col_values[i]

        # semd the dctionary for search

        file_name = "appointment.txt"
        # Need to handle this portion gracefully
        admin_login = self.admins[0]
        self.search_result = admin_login.view_appointment(
            self.search_data_dic, self.appointments)

        self.popup = tk.Toplevel()
        self.popup.geometry("900x600")
        if len(self.search_result) != 0:
            # Appointment booking form widget definition

            key = 'First Name'
            self.first_name = Label(self.popup, text=key, width=20)
            self.first_name.place(x=20, y=120)
            self.first_name_entry = Entry(self.popup)
            self.first_name_entry.place(x=200, y=120)
            self.first_name_entry.insert(0, self.search_result['First Name'])

            key = 'Last Name'
            self.last_name = Label(self.popup, text=key, width=20)
            self.last_name.place(x=420, y=120)
            self.last_name_entry = Entry(self.popup)
            self.last_name_entry.place(x=600, y=120)
            self.last_name_entry.insert(0, self.search_result['Last Name'])

            key = 'Email'
            self.email = Label(self.popup, text=key, width=20)
            self.email.place(x=20, y=160)
            self.email_entry = Entry(self.popup)
            self.email_entry.place(x=200, y=160)
            self.email_entry.insert(0, self.search_result['Email'])

            key = 'Age'
            self.age = Label(self.popup, text=key, width=20)
            self.age.place(x=420, y=160)
            self.age_entry = Entry(self.popup)
            self.age_entry.place(x=600, y=160)
            self.age_entry.insert(0, self.search_result['Age'])

            key = 'Address Line 1'
            self.address_line1 = Label(self.popup, text=key, width=20)
            self.address_line1.place(x=20, y=200)
            self.address_line1_entry = Entry(self.popup)
            self.address_line1_entry.place(x=200, y=200)
            self.address_line1_entry.insert(
                0, self.search_result['Address Line 1'])

            key = 'Address Line 2'
            self.address_line2 = Label(self.popup, text=key, width=20)
            self.address_line2.place(x=420, y=200)
            self.address_line2_entry = Entry(self.popup)
            self.address_line2_entry.place(x=600, y=200)
            self.address_line2_entry.insert(
                0, self.search_result['Address Line 2'])

            key = 'Post Code'
            self.post_code = Label(self.popup, text=key, width=20)
            self.post_code.place(x=20, y=240)
            self.post_code_entry = Entry(self.popup)
            self.post_code_entry.place(x=200, y=240)
            self.post_code_entry.insert(0, self.search_result['Post Code'])

            key = 'Symptoms'
            self.symptoms = Label(self.popup, text=key, width=20)
            self.symptoms.place(x=420, y=240)
            self.symptoms_entry = Entry(self.popup)
            self.symptoms_entry.place(x=600, y=240)
            self.symptoms_entry.insert(0, self.search_result['Symptoms'])

            key = 'Contact Number'
            self.contact_number = Label(self.popup, text=key, width=20)
            self.contact_number.place(x=20, y=280)
            self.contact_number_entry = Entry(self.popup)
            self.contact_number_entry.place(x=200, y=280)
            self.contact_number_entry.insert(
                0, self.search_result['Contact Number'])

            key = 'Assign Doctor'
            # This list should be based on the speciality and symptom match of doctors
            symptom = self.search_result['Symptoms']
            matching_doctors = list(
                filter(lambda doctor: self.match_symptom(doctor, symptom), self.doctors))

            # Creating matching doctor dictionary with ID and name. Name will be displayed in drop-down and ID will be stored upon selection
            self.selected_doctor_id = StringVar()
            doctor_dict = {str(doctor.full_name()) + ' (' + str(doctor.get_doctor_id()) +
                           ')': doctor.get_doctor_id() for doctor in matching_doctors}

            # If no doctor with matching symptom, rerieve all doctors
            if len(doctor_dict) == 0:
                matching_doctors = list(
                    filter(lambda doctor: self.all_doctor(doctor), self.doctors))
                doctor_dict = {str(doctor.full_name()) + '' + str(doctor.get_doctor_id())                               : doctor.get_doctor_id() for doctor in matching_doctors}

            if len(doctor_dict) != 0:
                self.doc_drop = OptionMenu(
                    self.popup, self.selected_doctor_id, *list(doctor_dict.keys()))
                self.doc_drop.place(x=600, y=280)
                self.doctor_assign = Label(
                    self.popup, text='Assign Doctor', width=20)
                self.doctor_assign.place(x=420, y=280)

                # If a value for self.search_result['Doctor ID'] exists, set the value of the OptionMenu widget to that value
                if 'Doctor ID' in self.search_result and self.search_result['Doctor ID'] in doctor_dict.values():
                    doctor_name = next(name for name, id in doctor_dict.items(
                    ) if id == self.search_result['Doctor ID'])
                    self.selected_doctor_id.set(doctor_name)

                def update_selected_doctor(*args):
                    self.search_result['Doctor ID'] = doctor_dict[self.selected_doctor_id.get(
                    )]

                self.selected_doctor_id.trace('w', update_selected_doctor)
            else:
                showinfo(
                    'Error', 'No Doctor Exist with matching Symptom. Add Doctors to the system')

            # date selection available only if status is pending
            if self.search_result['Status'] == 'Pending':

                key = 'Appointment Date'
                # Create a StringVar object to store the selected date
                self.selected_date = StringVar()

                # # Set the initial value of the StringVar object
                # self.selected_date.set(datetime.now().strftime("%Y-%m-%d"))

                self.appointment_date_label = Label(
                    self.popup, text=key, width=20)
                self.appointment_date_label.place(x=20, y=360)

                # Create a button to display the calendar when clicked
                button_date = tk.Button(
                    self.popup, text="Pick a date", command=self.pick_date)
                button_date.place(x=200, y=360)

                label = Label(
                    self.popup, textvariable=self.selected_date.get())
                label.place(x=400, y=360)

            # self.appointment_date_entry.insert(0, self.search_result['Appointment Date'])

            if self.search_result['Status'] == 'Confirmed':
                self.close_appointment = tk.Checkbutton(self.popup)
                self.close_appointment_var = IntVar()
                self.close_appointment.deselect()
                self.close_appointment.config(
                    command=self.complete_appointment_clicked, text="Close Appointment", variable=self.close_appointment_var)
                self.close_appointment.place(x=600, y=320)

            # Discharge or Process Admit request
            if self.search_result['Admit'] == 'Requested' or self.search_result['Admit'] == 'Rejected':
                self.admit_approve = tk.Checkbutton(self.popup)
                self.admit_request_var = IntVar()
                self.admit_approve.deselect()
                self.admit_approve.config(command=self.checkbox_clicked_admit,
                                          text="Approve Admit Request", variable=self.admit_request_var)
                self.admit_approve.place(x=200, y=320)

            elif self.search_result['Admit'] == 'Discharged' or self.search_result['Admit'] == '':
                pass

            else:
                self.admit_approve = tk.Checkbutton(self.popup)
                self.admit_request_var = IntVar()
                self.admit_approve.deselect()
                self.admit_approve.config(
                    command=self.checkbox_clicked_discharge, text="Discharge", variable=self.admit_request_var)
                self.admit_approve.place(x=200, y=320)

            if self.search_result['Status'] != 'Completed':

                self.button_confirm_appointment = tk.Button(self.popup, text="Confirm",
                                                            command=lambda: self.confirm_appointment(self.search_result, controller, admins, doctors, patients, appointments)).place(x=400, y=400)

    # Updating selected doctor

    def update_selected_doctor(selected_doctor_name):
        self.search_result['Doctor ID'] = self.doctor_dict[selected_doctor_name]

    # Create a function to display the calendar and allow the user to select a date
    def pick_date(self):
        # Create a frame for the date picker

        # Create a frame for the date picker
        date_picker_frame = tk.Toplevel(self.popup)

        # Create labels for the day, month, and year
        day_label = ttk.Label(date_picker_frame, text="Day:")
        day_label.grid(row=0, column=0)
        month_label = ttk.Label(date_picker_frame, text="Month:")
        month_label.grid(row=0, column=1)
        year_label = ttk.Label(date_picker_frame, text="Year:")
        year_label.grid(row=0, column=2)

        # Create comboboxes for the day, month, and year
        day_var = tk.StringVar()
        day_combobox = ttk.Combobox(date_picker_frame, textvariable=day_var)
        day_combobox['values'] = list(range(1, 32))
        day_combobox.grid(row=1, column=0)
        month_var = tk.StringVar()
        month_combobox = ttk.Combobox(
            date_picker_frame, textvariable=month_var)
        month_combobox['values'] = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        month_combobox.grid(row=1, column=1)
        year_var = tk.StringVar()
        year_combobox = ttk.Combobox(date_picker_frame, textvariable=year_var)
        year_combobox['values'] = list(range(2023, 2025))
        year_combobox.grid(row=1, column=2)

        # Create a button to submit the date
        submit_button = ttk.Button(date_picker_frame, text="Submit", command=lambda: submit_date(
            day_var.get(), month_var.get(), year_var.get()))
        submit_button.grid(row=2, column=0, columnspan=3)

        def submit_date(day, month, year):
            # Convert the selected day, month, and year to a date
            month_list = ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]
            month_int = month_list.index(month) + 1
            date = datetime(int(year), month_int, int(day)).date()
            self.selected_date = date
            self.search_result['Appointment Date'] = self.selected_date
            date_picker_frame.destroy()

    def match_symptom(self, doctor, symptom):
        return symptom in doctor.get_speciality()

    def all_doctor(self, doctor):
        return doctor

    def view_appointments(self, controller, appointments):

        self.data_refresh()
        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, self.admins, self.doctors, self.patients, self.appointments))
        self.logout.pack(side="left", padx=5, pady=5)

        self.button_book_appointment = tk.Button(self, text="Back Home",
                                                 command=lambda: self.back_home_clear(controller, self.admins, self.doctors, self.patients, self.appointments))
        self.button_book_appointment.pack(side="right", padx=5, pady=5)
        # hacky way need to implement gracefully
        admin_login = self.admins[0]
        appointment_list = admin_login.view_appointments(self.appointments)
        if len(appointment_list) == 0:
            print("No appointments to Display")

        else:

            cols = ['Appointment ID', "First Name", "Last Name", 'Email',
                    'Age', 'Contact Number', 'Symptoms', 'Status', 'Admit']

            self.appointment_list_view = ttk.Treeview(
                self, column=cols, show='headings')

            self.appointment_list_view.column(
                "# 1", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 1", text="Appointment ID")
            self.appointment_list_view.column(
                "# 2", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 2", text="First Name")
            self.appointment_list_view.column(
                "# 3", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 3", text="Last Name")
            self.appointment_list_view.column(
                "# 4", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 4", text="Email")
            self.appointment_list_view.column(
                "# 5", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 5", text="Age")
            self.appointment_list_view.column(
                "# 6", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 6", text="Contact Number")
            self.appointment_list_view.column(
                "# 7", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 7", text="Symptoms")
            self.appointment_list_view.column(
                "# 8", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading(
                "# 8", text="Appointment Status")
            self.appointment_list_view.column(
                "# 9", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 9", text="Admit Status")

            # Iterating through the appointment list to foramt the data for display
            for dic in appointment_list:
                app_list = []
                for key in cols:
                    if key in dic:
                        app_list.append(dic[key])
                self.appointment_list_view.insert(
                    '', 'end', text="1", values=app_list)
            self.appointment_list_view.place(width=900, height=800)
            self.appointment_list_view.bind(
                '<Button-1>', lambda event: self.on_row_click(event, controller, self.admins, self.doctors, self.patients, self.appointments))
            self.appointment_list_view.pack()

    # Refresh the data
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

# Discharged Patients


class ViewDischargedPatients (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Discharged Patients", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.admins = admins
        self.doctors = doctors
        self.patients = patients
        self.appointments = appointments

        self.discharged_patients(
            controller, admins, doctors, patients, appointments)

    def logout_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors,
                               patients, appointments)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error in the applicaiton')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            # Initialising Patients - Reading from file and defined as a list of Patient Objects
            file_name = 'patient.txt'
            patient_list = fo.parse_data_file(file_name)
            self.patients = []
            # For every dictionary on the appointment_list, initialise Appointment class and store in a list as list of objects

            for pat in patient_list:
                patient = Patient(pat)
                self.patients.append(patient)
            self.discharged_patients(
                controller, admins, doctors, self.patients, appointments)
            controller.show_frame(AdminPage)
        except:
            showinfo('Logout', 'Unexpected Error in loading')

    def func(self, value):
        self.clicked.set(value)
        self.search_result['Doctor'] = self.clicked.get()

    def discharged_patients(self, controller, admins, doctors, patients, appointments):

        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, admins, doctors, patients, appointments)).place(x=200, y=500)
        self.button_back_home = tk.Button(self, text="Back Home",
                                          command=lambda: self.back_home_clear(controller, admins, doctors, patients, appointments)).place(x=400, y=500)

        # Initialising Doctors - Reading from file and defined as a list of Doctor Objects
        file_name = 'doctor.txt'
        doctor_list = fo.parse_data_file(file_name)
        self.doctors = []
        # For every dictionary on the doctor_list, initialise Doctor class and store in a list as list of objects

        for doc in doctor_list:
            doctor = Doctor(doc)
            self.doctors.append(doctor)

        # hacky way need to implement gracefully
        admin_login = self.admins[0]
        patient_list = admin_login.view_patients(patients)

        if len(patient_list) == 0:
            print("No appointments to Display")

        else:

            cols = ["First Name", "Last Name", 'Email',
                    'Age', 'Contact Number', 'Symptoms', 'Admit']

            self.patient_list_view = ttk.Treeview(
                self, column=cols, show='headings')

            self.patient_list_view.column(
                "# 1", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 1", text="First Name")
            self.patient_list_view.column(
                "# 2", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 2", text="Last Name")
            self.patient_list_view.column(
                "# 3", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 3", text="Email")
            self.patient_list_view.column(
                "# 4", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 4", text="Age")
            self.patient_list_view.column(
                "# 5", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 5", text="Contact Number")
            self.patient_list_view.column(
                "# 6", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 6", text="Symptoms")
            self.patient_list_view.column(
                "# 7", anchor=CENTER, minwidth=0, width=100)
            self.patient_list_view.heading("# 7", text="Admit")

            # Iterating through the doctor list to foramt the data for display
            pat_list = []
            for dic in patient_list:
                if 'Admit' in dic and dic['Admit'] == 'Discharged':
                    values = [dic[key] for key in cols if key in dic]
                    pat_list.append(values)
            for val in pat_list:
                self.patient_list_view.insert('', 'end', text="1", values=val)

            self.patient_list_view.place(width=600, height=800)
            self.patient_list_view.pack()
