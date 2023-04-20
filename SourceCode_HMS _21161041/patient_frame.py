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

# Modules and libraries for file operations
import os
import file_operations as fo

# Modules specifc to tkinter window
import navigator_frame as nf
import validator_functions as vf
import admin_frame as af

# For generating Unique ID. Need to change
from uuid import uuid4


LARGE_FONT = ("Verdana", 16)

# Class defines the patient landing page


class PatientPage (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        self.load_buttons(controller)

    def load_buttons(self, controller):
        self.label = tk.Label(self, text="Patient Dashboard", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        self.__button_button_book_appointment_text = 'Book An Appointment'
        self.__button_button_check_appointment_text = 'Check Appointment'
        self.__button_home_text = 'Back Home'

        self.__button_book_appointment = tk.Button(self, text=self.__button_button_book_appointment_text,
                                                   command=lambda: controller.show_frame(BookAppointmentPage))
        self.__button_book_appointment.pack(side=LEFT, expand=TRUE)
        self.__button_book_appointment.config(width=25, height=5)

        self.__button_check_appointment = tk.Button(self, text=self.__button_button_check_appointment_text,
                                                    command=lambda: controller.show_frame(CheckAppointmentPage))
        self.__button_check_appointment.pack(side=LEFT, expand=TRUE)
        self.__button_check_appointment.config(width=25, height=5)

        self.__button_home = tk.Button(self, text=self.__button_home_text,
                                       command=lambda: controller.show_frame(nf.LandingPage))
        self.__button_home.pack(side=TOP, anchor=NW)

    def input_formatter(self, entries):
        # Converting user input entries into dictionary which can be read by Classes Patient and Appointment
        patient_data_dic = {}

        # Presetting system generated values. This will be needed for Patient object initialisation and later storing values to files
        entries['Patient ID'] = ''
        entries['Appointment ID'] = ''
        entries['Doctor ID'] = ''
        entries['Status'] = ''
        entries['Appointment Date'] = ''
        for key in entries:
            try:
                if type(entries[key]) == str:
                    patient_data_dic[(key)] = entries[key]
                else:
                    patient_data_dic[(key)] = entries[key].get()
            except AttributeError:
                showinfo(
                    'Error', 'Error occured in processing request. Please re-try')
        return patient_data_dic

# Formm for appointment booking bny patient


class BookAppointmentPage (PatientPage):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        super().__init__(parent, controller, admins, doctors, patients, appointments)
        self.appointment_form(controller, doctors, patients, appointments)

    def load_buttons(self, controller):
        self.label = tk.Label(
            self, text="Book Appointment Form", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)

    def appointment_form(self, controller, doctors, patients, appointments):
        try:
            # Dictionary to store user input and then use for appointment request file operations
            self.entries = {}

            # Appointment booking form widgets
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

            # This is an OPtionMenu widget.
            key = 'Symptoms'
            # Listing possible symptoms. Can load from a file to make it dynamic.
            symptom_options = ['General - Fever, Flu etc', 'Dental',
                               'ENT - Ear, Nose, Throat', 'Cardiology', 'Respiratory', 'Digestive', 'Other']
            self.clicked = StringVar()
            self.clicked.set("")
            self.symptoms = Label(self, text=key, width=20)
            self.symptoms.place(x=420, y=240)
            self.drop = OptionMenu(
                self, self.clicked, *symptom_options, command=self.func)
            self.drop.place(x=600, y=240)
            self.entries['Symptoms'] = self.clicked.get()

            key = 'Contact Number'
            self.contact_number = Label(self, text=key, width=20)
            self.contact_number.place(x=20, y=280)
            self.contact_number_entry = Entry(self)
            self.contact_number_entry.place(x=200, y=280)
            self.entries[key] = self.contact_number_entry

            # This is a Checkbutton. Additional function needed to set the selected value
            key = 'Admit Request'
            self.entries['Admit'] = ''
            self.admit = Label(self, text=key, width=20)
            self.admit.place(x=420, y=280)
            self.admit_request_var = IntVar()
            self.admit_request = Checkbutton(
                self, text="Admit", variable=self.admit_request_var, command=self.checkbox_clicked)
            self.admit_request.deselect()
            self.admit_request.place(x=600, y=280)

            self.button_register = tk.Button(self, text="Confirm",
                                             command=lambda: self.book_appointment(
                                                 self.entries, controller, doctors, patients, appointments),
                                             width=10).place(x=300, y=400)

            self.button_home = tk.Button(self, text="Cancel",
                                         command=lambda: self.cancel_form(controller, doctors, patients, appointments)).place(x=500, y=400)
        except:
            showinfo('Appointment', 'Error in data entry. Please try again')

    # Setting value for optionmenu
    def func(self, value):
        try:
            self.clicked.set(value)
            self.entries['Symptoms'] = self.clicked.get()
        except:
            showinfo('Appointment', 'Error in selecting Symptoms value')

    # Based on the cgeckbutton selection assign Admit value. If value is selected - Admit request is raised. Otherwise patiet don't want to be admitted
    def checkbox_clicked(self):
        try:
            if self.admit_request_var.get() == 1:
                self.entries['Admit'] = 'Requested'
            else:
                self.entries['Admit'] = ''
        except:
            showinfo('Appointment', 'Error in selecting Admit request')

    # Clearing appointment booking form

    def appointment_form_clear(self, controller, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.appointment_form(controller, doctors, patients, appointments)
        except:
            showinfo('Appointment', 'Internal error. If you already submitted the request, please check the status. Otherwise raise a new request')

    # Function to perform cancel action
    def cancel_form(self, controller, doctors, patients, appointments):
        try:
            self.appointment_form_clear(
                controller, doctors, patients, appointments)
            controller.show_frame(nf.LandingPage)
        except:
            showinfo('Appointment', 'Internal error. If you already submitted the request, pease check the status. Otherwise raise a new request')

    # Function to create a booking request
    def book_appointment(self, entries, controller, doctors, patients, appointments):
        try:
            # Converting user input entries into dictionary which can be read by Classes Patient and Appointment
            patient_data_dic = self.input_formatter(entries)

            # Calling the validator function
            is_valid, message = vf.validate_appointment_data(patient_data_dic)
            if (is_valid):
                # Initialisinf Patient class with user input data and then do the backend operation for appointment booking
                patient = Patient(patient_data_dic)
                # Refresh the data
                appointment_status, appointment_id = patient.book_appointment(
                    patient_data_dic, patients, appointments)
                if(appointment_status):
                    showinfo(
                        'Appointment', str(appointment_id) + ' - Appointment request sent to admin. The status will be notified via email/phone')
                    self.appointment_form_clear(
                        controller, doctors, patients, appointments)
                    controller.show_frame(af.ViewAppointmentsPage)
                    controller.show_frame(BookAppointmentPage)
            else:
                showinfo('Error', message)
        except:
            showinfo('Error', 'Error occured in processing request. Please re-try')


class CheckAppointmentPage (PatientPage):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        super().__init__(parent, controller, admins, doctors, patients, appointments)
        self.appointment_form(controller, doctors, patients, appointments)

    # Function overriding.
    def load_buttons(self, controller):
        self.label = tk.Label(self, text="Appointment", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)

    def appointment_form(self, controller, doctors, patients, appointments):
        try:
            # Dictionary to create initialize appointment and patient classes
            self.entries = {}

            # Appointment booking form widget definition
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

            key = 'Post Code'
            self.post_code = Label(self, text=key, width=20)
            self.post_code.place(x=420, y=160)
            self.post_code_entry = Entry(self)
            self.post_code_entry.place(x=600, y=160)
            self.entries[key] = self.post_code_entry

            key = 'Contact Number'
            self.contact_number = Label(self, text=key, width=20)
            self.contact_number.place(x=20, y=200)
            self.contact_number_entry = Entry(self)
            self.contact_number_entry.place(x=200, y=200)
            self.entries[key] = self.contact_number_entry

            # This is an OPtionMenu widget.
            key = 'Symptoms'
            # Listing possible symptoms. Can load from a file to make it dynamic.
            symptom_options = ['General - Fever, Flu etc', 'Dental',
                               'ENT - Ear, Nose, Throat', 'Cardiology', 'Respiratory', 'Digestive', 'Other']
            self.clicked = StringVar()
            self.clicked.set("")
            self.symptoms = Label(self, text=key, width=20)
            self.symptoms.place(x=420, y=200)
            self.drop = OptionMenu(
                self, self.clicked, *symptom_options, command=self.func)
            self.drop.place(x=600, y=200)

            self.button_search = tk.Button(self, text="Search",
                                           command=lambda: self.search_appointment(
                                               self.entries, controller, doctors, patients, appointments),
                                           width=10).place(x=300, y=400)

            self.button_home = tk.Button(self, text="Back",
                                         command=lambda: self.back_home(controller, doctors, patients, appointments)).place(x=500, y=400)
        except:
            showinfo('Error', 'Error occured in date input. Please re-try')

    # Setting value for optionmenu

    def func(self, value):
        try:
            self.clicked.set(value)
            self.entries['Symptoms'] = self.clicked.get()
        except:
            showinfo('Appointment', 'Error in selecting Symptoms value')

     # Function to create a booking request. Need to optimize exception handling
    def search_appointment(self, entries, controller, doctors, patients, appointments):
        try:
            app_data_dic = self.input_formatter(entries)
            is_valid, message = vf.validate_appointment_data(app_data_dic)
            if is_valid:
                # To ensure all keys for Patient class initialisation passing other keys. Should handle gracefully
                app_data_dic['Address Line 1'] = ''
                app_data_dic['Address Line 2'] = ''
                app_data_dic['Age'] = ''
                app_data_dic['Symptoms'] = ''
                app_data_dic['Patient ID'] = ''
                app_data_dic['Appointment ID'] = ''
                app_data_dic['Status'] = ''
                app_data_dic['Doctor ID'] = ''
                app_data_dic['Admit'] = ''
                app_data_dic['Appointment Date'] = ''

                # Initialisinf Patient class with user input data and then do the backend operation for appointment booking
                patient = Patient(app_data_dic)
                staus, app_retrieve = patient.search_appointment(
                    app_data_dic, patients, appointments)

                if not staus:
                    showinfo('Appointment', 'No record found for the patient')
                else:
                    for doctor in doctors:
                        if len(app_retrieve['Doctor']) != 0:
                            if doctor.get_doctor_id() == app_retrieve['Doctor']:
                                app_retrieve['Doctor Name'] = doctor.full_name()
                    user_details_frame = UserDetailsFrame(app_retrieve)
            else:
                showinfo('Error', message)
        except:
            showinfo('Error', 'Error in searching appointment')

    def view_details(self):
        # Create an instance of the UserDetailsFrame class and pass the user details
        user_details_frame = UserDetailsFrame(self.user_details)

    def back_home(self, controller, doctors, patients, appointments):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.appointment_form(controller, doctors, patients, appointments)
        controller.show_frame(nf.LandingPage)

# Displays appointment details


class UserDetailsFrame:
    def __init__(self, user_details):
        # Create a new frame
        self.frame = Tk()
        self.frame.title("Appointment Status")
        self.frame.geometry("400x300")

        # Display the user details using the Label widget
        first_name_label = Label(
            self.frame, text=f" First Name: {user_details['First Name']}")
        first_name_label.pack()

        last_name_label = Label(
            self.frame, text=f" Last Name: {user_details['Last Name']}")
        last_name_label.pack()

        status_label = Label(
            self.frame, text=f"Status: {user_details['Status']}")
        status_label.pack()

        if user_details['Status'] != 'Pending':
            doctor_label = Label(
                self.frame, text=f"Doctor: {user_details['Doctor Name']}")
            doctor_label.pack()
            if doctor_label:
                appointment_date_label = Label(
                    self.frame, text=f"Appointment Date: {user_details['Appointment Date']}")
                appointment_date_label.pack()
                admit_label = Label(
                    self.frame, text=f"Admit: {user_details['Admit']}")
                admit_label.pack()

        self.frame.mainloop()
