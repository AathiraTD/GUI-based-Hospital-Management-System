#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:14:00 2023

@author: aathira
"""
import admin_frame as af
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

# Importing frame modules
import doctor_frame as df
import patient_frame as pf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict
from collections import defaultdict
from datetime import datetime
import calendar


class DashboardPage (tk.Frame):
    def __init__(self, parent, controller, admins, doctors, patients, appointments):
        tk.Frame.__init__(self, parent)

        button_patient = tk.Button(self,
                                   text="Total Number of Doctors", command=lambda: self.total_doctors(doctors))
        button_patient.pack(side=LEFT, expand=TRUE)

        button_doctor = tk.Button(self,
                                  text="Patients Per Doctor", command=lambda: self.patient_per_doctor(doctors))
        button_doctor.pack(side=LEFT, expand=TRUE)

        button_illness = tk.Button(self,
                                   text="Patients by Illness Type", command=lambda: self.patient_by_illness(patients))
        button_illness.pack(side=LEFT, expand=TRUE)

        button_per_month = tk.Button(self,
                                     text="Appointments Per Doctor Per Month", command=lambda: self.patients_per_doctor_month(appointments, patients, doctors))
        button_per_month.pack(side=LEFT, expand=TRUE)

        self.button_home = tk.Button(self, text="Admin Home",
                                     command=lambda: controller.show_frame(af.AdminPage)).pack(side=TOP, anchor='nw')

    def total_doctors(self, doctors):
        # Create an instance of the UserDetailsFrame class and pass the user details
        total_doctors_frame = TotalNumberOfDoctors(doctors)

    def patient_per_doctor(self, doctors):
        # Create an instance of the UserDetailsFrame class and pass the user details
        patient_per_doctor_frame = NumberOfPatientsPerDoctor(doctors)

    def patient_by_illness(self, patients):
        # Create an instance of the UserDetailsFrame class and pass the user details
        patient_by_illness_frame = NumberOfPatientsByIllnessType(patients)

    def patients_per_doctor_month(self, appointments, patients, doctors):
        # Create an instance of the UserDetailsFrame class and pass the user details
        patients_per_doctor_month_frame = PatientsPerDoctorMonth(
            appointments, patients, doctors)


class TotalNumberOfDoctors:
    def __init__(self, doctors):
        # Create a new frame
        self.frame = Tk()
        self.frame.title("Total Number of Doctors")
        self.frame.geometry("800x600")

        fig, ax = plt.subplots()
        ax.bar([1], [len(doctors)])
        ax.set_xticks([])
        ax.set_yticks(range(0, len(doctors)+1))

        ax.set_title("Number of Doctors in Hospital")
        ax.set_xlabel("Hospital")
        ax.set_ylabel("Number of Doctors")
        canvas = FigureCanvasTkAgg(fig, self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.frame.mainloop()


class NumberOfPatientsPerDoctor:
    def __init__(self, doctors):
        # Create a new frame
        self.frame = Tk()
        self.frame.title("Total Number of Doctors")
        self.frame.geometry("800x600")
        # Dictionary to store doctor and number of patients assigned to them
        doctor_list = {}

        for doctor in doctors:
            name = doctor.full_name()
            # Stores patient ids to a string
            patient_ids_string = doctor.retrieve_patient()
            # If no patient already assigned to the Doctor
            if patient_ids_string:
                patient_ids = patient_ids_string.split(
                    ',')  # split the patient id string
                patient_count = len(patient_ids)
                if name in doctor_list:
                    doctor_list[name] += patient_count
                else:
                    doctor_list[name] = patient_count
            else:
                doctor_list[name] = 0

        names = list(doctor_list.keys())
        patient_counts = list(doctor_list.values())

        fig, ax = plt.subplots()
        ax.bar(names, patient_counts)
        # ax.set_xticks([])
        #ax.set_yticks(range(0, len(doctors)+1))

        ax.set_title("Number of Patients per Doctor")
        canvas = FigureCanvasTkAgg(fig, self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.frame.mainloop()


class NumberOfPatientsByIllnessType:
    def __init__(self, patients):
        # Create a new frame
        self.frame = Tk()
        self.frame.title("Patients based on illness type")
        self.frame.geometry("800x600")

        illness_counts = {}
        for patient in patients:
            symptom = patient.get_symptoms()
            # for symptom in symptoms:
            if symptom in illness_counts:
                illness_counts[symptom] += 1
            else:
                illness_counts[symptom] = 1

        illness_types = list(illness_counts.keys())
        patient_counts = list(illness_counts.values())
        fig, ax = plt.subplots()
        ax.bar(illness_types, patient_counts)

        ax.set_title("Number of Patients per Illness Type")
        ax.set_xlabel("Illness Type")
        ax.set_ylabel("Number of Patients")

        canvas = FigureCanvasTkAgg(fig, self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.frame.mainloop()


class PatientsPerDoctorMonth:
    def __init__(self, appointments, patients, doctors):
        # Create a new frame
        self.frame = Tk()
        self.frame.title("Patients Per Doctor Per Month")
        self.frame.geometry("800x600")

        # Create a dictionary of doctor IDs to doctor names
        doctor_names = {d.get_doctor_id(): d.full_name() for d in doctors}

        # Build the chart data structure
        chart_data = defaultdict(lambda: defaultdict(int))
        for a in appointments:
            doctor_id = a.get_doctor()
            date = a.get_appointment_date()
            if date:
                date_object = datetime.strptime(date, "%Y-%m-%d").date()
                month = date_object.month
                chart_data[doctor_names[doctor_id]][month] += 1

        # Create a Figure and a subplot
        fig, ax = plt.subplots()

        # Set the bar width
        bar_width = 0.8

        # Get the list of doctors and months
        doctor_names = list(chart_data.keys())
        months = sorted(
            list(set(month for doctor in chart_data for month in chart_data[doctor])))

        # Calculate the x-axis positions for the bars
        x_pos = [i for i in range(len(months))]

        # months = [calendar.month_name[int(month)] for month in months]

        # Iterate over the data and draw the bars on the subplot
        for i, doctor_name in enumerate(doctor_names):
            y_values = [chart_data[doctor_name][month] for month in months]
            ax.bar([x + i * bar_width for x in x_pos],
                   y_values, bar_width, label=doctor_name)

        # Set the labels for the x-axis
        ax.set_xticks(
            [x + bar_width * (len(doctor_names) - 1) / 2 for x in x_pos])
        ax.set_xticklabels(months)

        # Add a legend to the chart
        ax.legend()

        # Create a FigureCanvasTkAgg widget to display the plot
        canvas = FigureCanvasTkAgg(fig, self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.frame.mainloop()
