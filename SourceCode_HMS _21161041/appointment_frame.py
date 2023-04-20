#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 16:30:11 2023

@author: aathira
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.messagebox import showinfo
from appointment import Appointment
from doctor import Doctor
from patient import Patient
import os
import file_operations as fo
import navigator_frame as nf
from admin import Admin
import patient_frame as pf
from uuid import uuid4
import validator_functions as vf
import admin_frame as af
import patient_management_frame as pmf
from tkinter import font
import calendar
import datetime
import random


LARGE_FONT = ("Verdana", 16)


class view_appointments_page (tk.Frame):
    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        self.admins = admins
        self.doctors = doctors
        self.patients = patients
        self.appointments = appointments
        self.controller = controller

        self.data_refresh()
        self.view_appointments(controller, self.appointments)

    def logout_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_appointments(controller)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_appointments(controller, self.appointments)
            controller.show_frame(af.AdminPage)
        except:
            showinfo('Logout', 'Unexpected Error')

    def func(self, value):
        self.option.set(value)
        self.search_result['Doctor'] = self.option.get()

    def checkbox_clicked_admit(self):
        if self.admit_request_var.get() == 1:
            self.search_result['Admit'] = 'Admit'

    def checkbox_clicked_discharge(self, value):
        if self.admit_request_var.get() == 1:
            self.search_result['Admit'] = 'Discharge'

    def complete_appointment_clicked(self):
        if self.close_appointment_var.get() == 1:
            self.search_result['Status'] = 'Completed'
        else:
            self.search_result['Status'] = 'Confirmed'

    # Function to confirm appointment by Admin
    def confirm_appointment(self, entries, controller, admins, doctors, patients, appointments):

        try:
            valid = False
            valid = (vf.numeric_field_validator(entries['Age'])) and (
                vf.numeric_field_validator(entries['Contact Number']))
            if (valid):
                # Initialisinf Patient class with user input data    and then do the backend operation for appointment booking
                # Need to handle this portion gracefully
                admin_login = self.admins[0]
                appointment_status = admin_login.confirm_appointment(
                    entries, patients, appointments)
                if(appointment_status):
                    showinfo(
                        'Appointment', entries['Unique Id'] + ' - Appointment is confirmed')
                    self.popup.destroy()
                    for widgets in self.winfo_children():
                        widgets.destroy()
                    self.view_appointments(controller, self.appointments)
            else:
                showinfo('Error', 'Age and Contact number must be an integer')
        except:
            showinfo('Error', 'Unknown Error !')

    # Pop
    def on_row_click(self, event, controller, admins, doctors, patients, appointments):
        # Get the row that was clicked on
        self.search_result = {}
        self.row_id = self.appointment_list_view.identify_row(event.y)
        self.row = self.appointment_list_view.item(self.row_id)
        cols = ['First Name', 'Last Name', 'Email',
                'Age', 'Contact Number', 'Symptoms', 'Status']
        col_values = self.row['values']
        print(col_values)
        self.search_data_dic = {}
        for i in range(0, len(cols)):
            self.search_data_dic[cols[i]] = col_values[i]
        print(self.search_data_dic)

        # semd the dctionary for search

        file_name = "appointment.txt"
        # Need to handle this portion gracefully
        admin_login = self.admins[0]
        self.search_result = admin_login.view_appointment(
            self.search_data_dic, self.appointments)
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

            key = 'Assign Doctor'
            # This list should be based on the speciality and symptom match of doctors
            symptom = self.search_result['Symptoms']
            matching_doctors = list(
                filter(lambda doctor: self.match_symptom(doctor, symptom), self.doctors))

            doctor_list = [doctor.full_name() for doctor in matching_doctors]
            self.option = StringVar()
            self.option.set("")
            self.doctor_assign = Label(self.popup, text=key, width=20)
            self.doc_drop = OptionMenu(
                self.popup, self.option, *doctor_list, command=self.func)
            self.doc_drop.place(x=600, y=280)
            self.doctor_assign.place(x=420, y=280)

            key = 'Appointment Date'
            now = datetime.datetime.now()
            start_date = now
            end_date = now + datetime.timedelta(days=90)
            random_date = start_date + \
                datetime.timedelta(days=random.randint(
                    0, (end_date - start_date).days))

            self.appointment_date = Label(self.popup, text=key, width=20)
            self.appointment_date.place(x=20, y=360)
            self.appointment_date_entry = Entry(self.popup)
            self.appointment_date_entry.place(x=200, y=360)
            self.search_result['Appointment Date'] = random_date.date()
            self.appointment_date_entry.insert(
                0, self.search_result['Appointment Date'])

            if self.search_result['Doctor']:
                self.option.set(self.search_result['Doctor'])
            else:
                self.search_result['Doctor'] = self.option.get()

            if self.search_result['Status'] == 'Confirmed':
                self.close_appointment = tk.Checkbutton(self.popup)
                self.close_appointment_var = IntVar()
                self.close_appointment.deselect()
                self.close_appointment.config(
                    command=self.complete_appointment_clicked, text="Close Appointment", variable=self.close_appointment_var)
                self.close_appointment.place(x=600, y=320)

            # Discharge or Process Admit request
            if self.search_result['Admit'] == 'Requested' or self.search_result['Admit'] == 'Rejected' or len(self.search_result['Admit']) == 0:
                self.admit_approve = tk.Checkbutton(self.popup)
                self.admit_request_var = IntVar()
                self.admit_approve.deselect()
                self.admit_approve.config(command=self.checkbox_clicked_admit,
                                          text="Approve Admit Request", variable=self.admit_request_var)
                self.admit_approve.place(x=200, y=320)

            else:
                self.admit_approve = tk.Checkbutton(self.popup)
                self.admit_request_var = IntVar()
                self.admit_approve.deselect()
                self.admit_approve.config(
                    command=self.checkbox_clicked_discharge, text="Discharge", variable=self.admit_request_var)
                self.admit_approve.place(x=200, y=320)

            self.button_confirm_appointment = tk.Button(self.popup, text="Confirm",
                                                        command=lambda: self.confirm_appointment(self.search_result, controller, admins, doctors, patients, appointments)).place(x=400, y=400)

    def match_symptom(self, doctor, symptom):
        return symptom in doctor.get_speciality()

    def view_appointments(self, controller, appointments):
        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, admins, doctors, patients, appointments)).place(x=200, y=500)

        self.data_refresh()
        self.button_book_appointment = tk.Button(self, text="Back Home",
                                                 command=lambda: self.back_home_clear(controller, self.admins, self.doctors, self.patients, self.appointments)).place(x=400, y=500)
        # hacky way need to implement gracefully
        admin_login = self.admins[0]
        appointment_list = admin_login.view_appointments(self.appointments)
        if len(appointment_list) == 0:
            print("No appointments to Display")

        else:

            cols = ["First Name", "Last Name", 'Email',
                    'Age', 'Contact Number', 'Symptoms', 'Status', 'Admit']

            self.appointment_list_view = ttk.Treeview(
                self, column=cols, show='headings')

            self.appointment_list_view.column(
                "# 1", anchor=CENTER, minwidth=0, width=100)
            self.appointment_list_view.heading("# 1", text="First Name")
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
            self.appointment_list_view.heading("# 5", text="Contact Number")
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
