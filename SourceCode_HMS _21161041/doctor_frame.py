# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:00:26 2022

@author: aathira
"""
#**************DOCTOR FUNCTIONALITIES NOT FULLY FUNCTIONAL YET************


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from appointment import Appointment
from doctor import Doctor
import os
import file_operations as fo
import navigator_frame as nf


LARGE_FONT = ("Verdana", 12)

# Class defines the doctor page


class doctor_login_page (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Doctor Login Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.__login_form(controller, admins, doctors, patients, appointments)

    def __login_form(self, controller, admins, doctors, patients, appointments):
        try:
            user_name = Label(self, text="User Name",
                              width=20, font=LARGE_FONT)
            user_name.place(x=20, y=120)
            self.user_name_entry = Entry(self)
            self.user_name_entry.place(x=200, y=120)

            password = Label(self, text="Password", width=20, font=LARGE_FONT)
            password.place(x=20, y=160)
            self.password_entry = Entry(self, show='*')
            self.password_entry.place(x=200, y=160)

            self.login = tk.Button(self, text="Login", command=lambda: self.login_validator(
                controller, admins, doctors, patients, appointments)).place(x=300, y=400)

            self.login = tk.Button(self, text="Back Home", command=lambda: controller.show_frame(
                nf.LandingPage)).place(x=500, y=400)
        except:
            showinfo('Login', 'Unexpected Error in Login')

    # Clears the login credential in the form
    def login_form_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.__login_form(controller, admins, doctors,
                              patients, appointments)
        except ValueError:
            showinfo('Login', 'Unexpected Error in clearing logout')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.__login_form(controller, admins, doctors,
                              patients, appointments)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    # Admin login validator. Initialises the class Admin to trigger login method of the class Admin
    def login_validator(self, controller, admins, doctors, patients, appointments):
        try:
            user_name = self.user_name_entry.get()
            password = self.password_entry.get()

            # To begin with Login - First Name and Last Name is considered

            # Doctor Login is different from Admin. Doctors will have to input First Name, Last Name, username and password. Username and Password is not added to doctor data
            doctor_login = ''

            for doc in doctors:
                # if user_name == doc.get_first_name() and password == doc.set_last_name():
                if user_name == 'doctor' and password == 'password':
                    self.login_form_clear(
                        controller, admins, doctors, patients, appointments)
                    doctor_login = doc
                    break
            if doctor_login == '':
                showinfo('Login', 'Invalid Credentials')

            else:
                for widgets in self.winfo_children():
                    widgets.destroy()

                else:

                    # Identify the list patiens linked to a doctor first. Then retrieve appointments present for those patients
                    appointment_list = doctor_login.retrieve_patient()
                    if len(appointment_list) == 0:
                        print("No appointments to Display")

                    cols = ["First Name", "Last Name", 'Email',
                            'Age', 'Contact Number', 'Symptoms', 'Status', 'Admit']

                    self.appointment_list_view = ttk.Treeview(
                        self, column=cols, show='headings')

                    self.appointment_list_view.column(
                        "# 1", anchor=CENTER, minwidth=0, width=100)
                    self.appointment_list_view.heading(
                        "# 1", text="First Name")
                    self.appointment_list_view.column(
                        "# 2", anchor=CENTER, minwidth=0, width=100)
                    self.appointment_list_view.heading("# 2", text="Last Name")
                    self.appointment_list_view.column(
                        "# 3", anchor=CENTER, minwidth=0, width=100)
                    self.appointment_list_view.heading("# 3", text="Email")
                    self.appointment_list_view.column(
                        "# 4", anchor=CENTER, minwidth=0, width=100)
                    self.appointment_list_view.heading("# 4", text="Age")
                    self.appointment_list_view.column(
                        "# 5", anchor=CENTER, minwidth=0, width=100)
                    self.appointment_list_view.heading(
                        "# 5", text="Contact Number")
                    self.appointment_list_view.column(
                        "# 6", anchor=CENTER, minwidth=0, width=100)
                    self.appointment_list_view.heading("# 6", text="Symptoms")
                    self.appointment_list_view.column(
                        "# 7", anchor=CENTER, minwidth=0, width=100)
                    self.appointment_list_view.heading("# 7", text="Status")
                    self.appointment_list_view.column(
                        "# 8", anchor=CENTER, minwidth=0, width=100)
                    self.appointment_list_view.heading("# 8", text="Admit")

                    # Iterating through the appointment list to foramt the data for display
                    for dic in appointment_list:
                        print()
                        app_list = []
                        for key in cols:
                            if key in dic:
                                app_list.append(dic[key])
                        self.appointment_list_view.insert(
                            '', 'end', text="1", values=app_list)
                    self.appointment_list_view.place(width=600, height=800)
                    # self.appointment_list_view.bind(
                    #     '<Button-1>', lambda event: self.on_row_click(event, controller, admins, doctors, patients, appointments))
                    # self.appointment_list_view.pack()

                    self.button_book_appointment = tk.Button(self, text="Back Home",
                                                             command=lambda: self.back_home_clear(controller, admins, doctors, patients, appointments)).place(x=400, y=500)

        except:
            showinfo('Login', 'Unexpected Error in Login')

    def data_refresh():
        file_name = 'admin.txt'
        admin_list = fo.parse_data_file(file_name)
        admins = []
        
        # For every dictionary on the admin_list, initialise Admin class and store in a list as list of objects
        # username is 'admin', password is 'password'
        for adm in admin_list:
            admin = Admin(adm)
            admins.append(admin)

        # Initialising Doctors - Reading from file and defined as a list of Doctor Objects
        file_name = 'doctor.txt'
        doctor_list = fo.parse_data_file(file_name)
        doctors = []
        
        # For every dictionary on the doctor_list, initialise Doctor class and store in a list as list of objects
        for doc in doctor_list:
            doctor = Doctor(doc)
            doctors.append(doctor)

        # Initialising Appointments - Reading from file and defined as a list of Appointment Objects
        file_name = 'appointment.txt'
        appointment_list = fo.parse_data_file(file_name)
        appointments = []
        
        # For every dictionary on the appointment_list, initialise Appointment class and store in a list as list of objects
        for app in appointment_list:
            appointment = Appointment(app)
            appointments.append(appointment)

        # Initialising Patients - Reading from file and defined as a list of Patient Objects
        file_name = 'patient.txt'
        patient_list = fo.parse_data_file(file_name)
        patients = []
        
        # For every dictionary on the appointment_list, initialise Appointment class and store in a list as list of objects
        for pat in patient_list:
            patient = Patient(pat)
            patients.append(patient)


# Definition of landing page of admin. Imherited from doctor_login_page
class doctor_page (doctor_login_page):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        self.doctor_page_config(
            controller, admins, doctors, patients, appointments)
        super().__init__(parent, controller, admins, doctors, patients, appointments)

        super().data_refresh()

    def doctor_page_config(self, controller, admins, doctors, patients, appointments):
        try:
            label = tk.Label(self, text="Admin Page", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            self.button_view_appointments = tk.Button(self, text="View Appointments",
                                                      command=lambda: controller.show_frame(apf.ViewAppointmentsPage))
            self.button_view_appointments.pack()

            self.button_doctor = tk.Button(self, text="Doctor Management",
                                           command=lambda: controller.show_frame(dmf.DoctorManagementPage))
        except:
            showinfo('Error', 'Unexpected Error')

    def logout_clear(self, controller):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.doctor_page_config(
                controller, admins, doctors, patients, appointments)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error')
