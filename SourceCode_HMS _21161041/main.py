# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:30:26 2022

@author: aathira

 ADMIN USERNAME : admin
 ADMIN PASSWORD : password
 
"""
# Imports
from admin import Admin
from doctor import Doctor
from patient import Patient
from appointment import Appointment
import navigator_frame as Window

#Importing file operations modules
import file_operations as fo


def main():
    """
    the main function to be ran when the program runs
    """
    # Initialising the actor Admin - - Reading from file and defined as a list of Admin Objects
    file_name = 'admin.txt'
    admin_list = fo.parse_data_file(file_name)
    admins=[]
    
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
    
        
    # Initialising the  MainWindow to create root window object.
    root = Window.MainWindow( admins , doctors , patients , appointments )
    
    #  Executing the main window
    root.mainloop ()

    # Below partial code given is not used as developing it in GUI.
    # Initialising the actors
    # admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    # doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    # discharged_patients = []

    # # keep trying to login tell the login details are correct
    # while True:
    #     if admin.login():
    #         running = True # allow the   to run
    #         break
    #     else:
    #         print('Incorrect username or password.')

    # while running:
    #     # print the menu
    #     print('Choose the operation:')
    #     print(' 1- Register/view/update/delete doctor')
    #     print(' 2- Discharge patients')
    #     print(' 3- View discharged patient')
    #     print(' 4- Assign doctor to a patient')
    #     print(' 5- Update admin detais')
    #     print(' 6- Quit')

    #     # get the option
    #     op = input('Option: ')

    #     if op == '1':
    #         # 1- Register/view/update/delete doctor
    #      #ToDo1
    #       pass

    #     elif op == '2':
    #         # 2- View or discharge patients
    #         #ToDo2
    #         pass

    #         while True:
    #             op = input('Do you want to discharge a patient(Y/N):').lower()

    #             if op == 'yes' or op == 'y':
    #                 #ToDo3
    #                 pass

    #             elif op == 'no' or op == 'n':
    #                 break

    #             # unexpected entry
    #             else:
    #                 print('Please answer by yes or no.')
        
    #     elif op == '3':
    #         # 3 - view discharged patients
    #         #ToDo4
    #         pass

    #     elif op == '4':
    #         # 4- Assign doctor to a patient
    #         admin.assign_doctor_to_patient(patients, doctors)

    #     elif op == '5':
    #         # 5- Update admin detais
    #         admin.update_details()

    #     elif op == '6':
    #         # 6 - Quit
    #         #ToDo5
    #         pass

    #     else:
    #         # the user did not enter an option that exists in the menu
    #         print('Invalid option. Try again')

if __name__ == '__main__':
    main()
    
    
