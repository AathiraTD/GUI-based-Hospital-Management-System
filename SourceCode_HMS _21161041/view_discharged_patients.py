#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 16:47:18 2023

@author: aathira
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


class view_discharged_patients (tk.Frame):

    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Appointment", font=LARGE_FONT)
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
            self.view_patients(controller, admins, doctors,
                               patients, appointments)
            controller.show_frame(af.AdminPage)
        except:
            showinfo('Logout', 'Unexpected Error in loading')

    def func(self, value):
        self.clicked.set(value)
        self.search_result['Doctor'] = self.clicked.get()

    def discharged_patients(self, controller, admins, doctors, patients, appointments):

        self.logout = tk.Button(self, text="Logout", command=lambda: self.logout_clear(
            controller, admins, doctors, patients, appointments)).place(x=200, y=500)
        self.button_back_home = tk.Button(self, text="Back Home",
                                          command=lambda: controller.show_frame(admin_page)).place(x=400, y=500)
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
