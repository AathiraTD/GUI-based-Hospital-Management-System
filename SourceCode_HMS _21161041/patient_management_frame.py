#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 16:47:18 2023

@author: sgshaji
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from appointment import Appointment
from doctor import Doctor
import os
import file_operations as fo
import navigator_frame as nf
from admin import Admin
import patient_frame as pf
from uuid import uuid4
import validator_functions as vf
import admin_frame as af


LARGE_FONT = ("Verdana", 12)


global admin_login
global search_result
search_result = {}


class patient_management_page (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        
        self.admins = admins
        self.doctors = doctors
        self.patients = patients
        self.appointments = appointments
        
        
        self.button_view_appointments = tk.Button(self, text="View Patients",
                                                  command=lambda: controller.show_frame(view_patients_page))
        self.button_view_appointments.pack(side=LEFT , expand=TRUE)

        self.button_doctor = tk.Button(self, text="Group patients by Family",
                                       command=lambda: controller.show_frame(group_patients_family))
        self.button_doctor.pack(side=LEFT , expand=TRUE)

        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, admins, doctors, patients, appointments)).place(x=200, y=500)
        self.button_back_home = tk.Button(self, text="Back Home",
                                                 command=lambda: self.back_home_clear(controller, admins, doctors, patients, appointments)).place(x=400, y=500)
        
    
    
    def logout_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors, patients, appointments)
            controller.show_frame( nf.LandingPage )
        except:
            showinfo('Logout', 'Unexpected Error')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors, patients, appointments)
            controller.show_frame( af.AdminPage )
        except:
            showinfo('Logout', 'Unexpected Error')


class view_patients_page (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        
        self.admins = admins
        self.doctors = doctors
        self.patients = patients
        self.appointments = appointments
        
        self.view_patients(controller, admins, doctors, patients, appointments)
     
    def logout_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors, patients, appointments)
            controller.show_frame( nf.LandingPage )
        except:
            showinfo('Logout', 'Unexpected Error')

    def back_home_clear(self, controller, admins, doctors, patients, appointments):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.view_patients(controller, admins, doctors, patients, appointments)
            controller.show_frame( af.AdminPage )
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
        cols = ['First Name', 'Last Name', 'Email',
                'Age', 'Contact Number', 'Speciality']
        col_values = self.row['values']
        print(col_values)
        self.search_data_dic = {}
        for i in range(0, len(cols)):
            self.search_data_dic[cols[i]] = col_values[i]
        print(self.search_data_dic)


        # Need to handle this portion gracefully
        admin_login = admins[0]       
        self.search_result = admin_login.view_patient (self.search_data_dic, patients )
        print(self.search_result)

        self.popup = tk.Toplevel()
        # self.popup.geometry ("450*300")
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
            self.address_line1_entry.insert(0, self.search_result['Address Line 1'])
            

            key = 'Address Line 2'
            self.address_line2 = Label(self.popup, text=key, width=20)
            self.address_line2.place(x=420, y=200)
            self.address_line2_entry = Entry(self.popup)
            self.address_line2_entry.place(x=600, y=200)
            self.address_line2_entry.insert(0, self.search_result['Address Line 2'])

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
            self.contact_number_entry.insert(0, self.search_result['Contact Number'])


    
    def view_patients(self, controller, admins, doctors, patients, appointments):
        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, admins, doctors, patients, appointments)).place(x=200, y=500)
        self.button_back_home = tk.Button(self, text="Back Home",
                                                 command=lambda: self.back_home_clear(controller, admins, doctors, patients, appointments)).place(x=400, y=500)
        # hacky way need to implement gracefully
        admin_login = self.admins[0]
        patient_list = admin_login.view_patients(patients)
        if len(patient_list) == 0:
            print("No appointments to Display")

        else:

            cols = ["First Name", "Last Name", 'Email',
                    'Age', 'Contact Number', 'Symptoms', 'Status']

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
            self.patient_list_view.heading("# 7", text="Status")

            
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




class group_patients_family (tk.Frame):

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
            controller.show_frame( nf.LandingPage )
        except:
            showinfo('Logout', 'Unexpected Error')

    def back_home_clear(self, controller):
        try:
            for widgets in self.winfo_children():
                widgets.destroy()
            self.group_patients(controller)
            controller.show_frame( af.AdminPage )
        except:
            showinfo('Logout', 'Unexpected Error')     
            
            
    def group_patients (self, controller):
        try:
            
            self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
                controller, admins, doctors, patients, appointments)).place(x=200, y=500)
            self.button_back_home = tk.Button(self, text="Back Home",
                                                     command=lambda: self.back_home_clear(controller)).place(x=400, y=500)
            self.add_button = tk.Button(self, text="Group Patients", command=lambda: self.group_patient_form(controller))
            self.add_button.pack()
       
            
            # # Creating a dictionary with post code as the key and values are list of patients
            
            # self.patient_groups ={}
            
            # for patient in self.patients:
            #     postcode = patient.get_post_code()
            #     if postcode not in self.patient_groups:
            #         self.patient_groups[postcode] = []
                
            #     full_name = patient.full_name()
            #     self.patient_groups[postcode].append(full_name)
            
            # print(self.patient_groups)
            self.generate_patient_groups()            

            self.display_groups()
            
        except:
            print("Exception in patent")
        
    # Generate a file for the default grouping - by default patients grouped based on post code. This is modifiable by admin
    def generate_patient_groups(self):
        try:
            file_name = 'patient_group.txt'
            if os.path.exists(file_name):
                pass
            else:
                self.patient_groups ={}                
                for patient in self.patients:
                    postcode = patient.get_post_code()
                    if postcode not in self.patient_groups:
                        self.patient_groups[postcode] = []
                    full_name = patient.full_name()
                    self.patient_groups[postcode].append(full_name)
                write_status = fo.store_patient_groups(file_name, self.patient_groups)
                if write_status:
                    pass
                else:
                    print("write failed")
        except:
            pass
    
    # Method to display groups
    def display_groups(self):
        try:
            #creating a list-box to display the groups of patients
            self.listbox_patient = tk.Listbox(self)
            self.listbox_patient.place(x=50, y=50, width=600, height=300)
            file_name = 'patient_group.txt'
            self.patient_groups = fo.parse_patient_groups(file_name)
            for postcode, names in self.patient_groups.items():
                group_string = f"{postcode}: "
                for name in names:
                    group_string += name + ", "
                self.listbox_patient.insert(tk.END, group_string)
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
            write_status = fo.store_patient_groups(file_name, self.patient_groups)
            if write_status:
                pass
            else:
                print("write failed")
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
        submit_button = tk.Button(self.form, text="Submit", command=lambda: self.add_patient_submit(controller))
        
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
        self.group_patients(controller)
        
