# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 02:01:38 2022

@author: aathira
"""

# Loading Class Modules
from appointment import Appointment
from person import Person
from doctor import Doctor
from patient import Patient

# Loading tkinter messagebox for error display
from tkinter.messagebox import showinfo

# For generating unique ID
import uuid
import hashlib

# Loading module for file operations
import file_operations as fo
import os

# Class is inherited from Person


class Admin (Person):
    """A class that deals with the Admin operations"""
    # adm is a dictionary

    def __init__(self, adm):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = adm[('username')]
        self.__password = adm[('password')]
        self.__admin_id = adm['Admin ID']

        super().__init__(adm)

    def full_name(self):
        """full name is first_name and surname"""
        # ToDo2
        pass

    def get_id(self):
        return self.__admin_id

    # This functon is not used. Rather developed new one in the context of GUI
    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def get_user_name(self):
        return self.__username

    def get_password(self):
        return self.__password

    def login(self, username, password, admins):
        try:
            self.refresh_data()
            for admin in self.admins:
                if (username == admin.get_user_name() and password == admin.get_password()):
                    login_status = True
                    break
                else:
                    login_status = False
        except:
            showinfo(
                'Login', ' Error in login. Please re-renter the credential and try again')

        finally:
            return login_status

    # To refresh Admin data. Re-reading from files.
    def refresh_data(self):
        try:
            file_name = 'admin.txt'
            # reading from files into a list of dictionaries
            admin_list = fo.parse_data_file(file_name)
            self.admins = []

            for adm in admin_list:
                admin = Admin(adm)
                self.admins.append(admin)
        except:
            print("Error in retrieving admin data")

    # Method not used in GUI
    def find_index(self, index, doctors):

        # check that the doctor id exists
        if index in range(0, len(doctors)):

            return True

        # if the id is not in the list of doctors
        else:
            return False

    # Method from partial code. Not used. Developed one from GUI perspective
    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        # ToDo2

        file_name = "doctor.txt"
        pass

    # Method from partial code. Not used. Developed one from GUI perspective
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        op = ''
        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        # ToDo3
        pass

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            # ToDo4
            pass

            # check if the name is already registered
            name_exists = False
            first_name = ''
            surname = ''
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    # ToDo5
                    pass  # save time and end the loop

            # ToDo6
            pass  # add the doctor ...
            # ... to the list of doctors
            print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            # ToDo7
            pass

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index != False:

                        break

                    else:
                        print("Doctor not found")

                        # doctor_index is the ID mines one (-1)

                except ValueError:  # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: '))  # make the user input lowercase

            # ToDo8
            pass

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            # ToDo9
            pass

            print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    # Retrieving all patients. Possible enhancement to combine this and view_patient
    def view_patients(self, patients):
        try:
            # A list of dictionary
            display_patients = []
            for patient in patients:
                display_patient = {}
                display_patient['First Name'] = patient.get_first_name()
                display_patient['Last Name'] = patient.get_last_name()
                display_patient['Contact Number'] = patient.get_contact_number()
                display_patient['Age'] = patient.get_age()
                display_patient['Email'] = patient.get_email()
                display_patient['Symptoms'] = patient.get_symptoms()
                display_patient['Address Line 1'] = patient.get_address_line1()
                display_patient['Address Line 2'] = patient.get_address_line2()
                display_patient['Post Code'] = patient.get_post_code()
                display_patient['Patient ID'] = patient.get_unique_id()
                display_patient['Admit'] = patient.get_admit()
                display_patient['Appointment Date'] = patient.get_appointment_date()

                display_patients.append(display_patient)

        except:
            print("Error in retrieving the data")

        finally:
            return display_patients

    # Retrieving a patient. Possible enhancement to combine this and view_patients
    def view_patient(self, data, patients):
        try:
            display_patient = {}

            for patient in patients:
                if (str(data['Patient ID']) == patient.get_unique_id()):

                    display_patient['First Name'] = patient.get_first_name()
                    display_patient['Last Name'] = patient.get_last_name()
                    display_patient['Contact Number'] = patient.get_contact_number(
                    )
                    display_patient['Age'] = patient.get_age()
                    display_patient['Email'] = patient.get_email()
                    display_patient['Symptoms'] = patient.get_symptoms()
                    display_patient['Address Line 1'] = patient.get_address_line1()
                    display_patient['Address Line 2'] = patient.get_address_line2()
                    display_patient['Post Code'] = patient.get_post_code()
                    display_patient['Patient ID'] = patient.get_unique_id()
                    display_patient['Admit'] = patient.get_admit()
                    display_patient['Appointment Date'] = patient.get_appointment_date(
                    )

                    break
            else:
                pass
        except:
            print("Error in retrieving the patient data")

        finally:
            return display_patient

    # From the GUI scope, not needed. Selected doctor Id will be passsed to Admin class method
    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return  # stop the procedures

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return  # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()  # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index, doctors) != False:

                # link the patients to the doctor and vice versa
                # ToDo11
                pass

                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError:  # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

        # ToDo12
        pass

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        # ToDo13
        pass

    def update_details(self, entries, admins):
        """
        # Allows the user to update and change username, password and address
        # """
        try:
            file_name = 'admin.txt'
            status = False
            for admin in admins:
                if (entries['Admin ID'] == admin.get_id()):
                    status = fo.update_data_to_file(
                        file_name, 'Admin ID', entries)
                    break
        except:
            pass
        finally:
            return status

    # Modified partial code to have a separate function for doctor registration
    def register_doctor(self, entries, doctors):
        try:
            doc_status = False
            # Generating Doctor ID
            entries['Doctor ID'] = self.generate_unique_id(
                entries['Contact Number'])
            file_name = "doctor.txt"
            # Receives if doctor exist and if not exist file update update ststus.
            doc_exist, doc_status = self.store_doc_data_to_file(
                file_name, entries, doctors)
        except:
            showinfo('Doctor', "Doctor Registration Failed. Please re-try")
        finally:
            # Returning registration status and ID. ID will not be used if registration fails
            return doc_exist, doc_status, entries['Doctor ID']

    # Function to save data doctor to file.

    def store_doc_data_to_file(self, file_name, entries, doctors):
        try:
            write_status = False
            doctor_exist = self.check_doctor_exist(file_name, entries, doctors)
            if not doctor_exist:
                value = entries.pop('Status', None)
                write_status = fo.store_data_to_file(entries, file_name)
        except:
            showinfo('Patient', 'Error in processing the request')
        finally:
            return doctor_exist, write_status

    # Check if doctor already exist. ID check is not possible as this is called for new doctor registration and ID will generated post this..
    def check_doctor_exist(self, file_name, entries, doctors):
        try:
            exist = False
            if len(doctors) != 0:
                for doctor in doctors:
                    if (entries['First Name'] == doctor.get_first_name() and entries['Last Name'] == doctor.get_last_name() and entries['Contact Number'] == doctor.get_contact_number() and entries['Speciality'] == doctor.get_speciality()):
                        exist = True
                        return exist
            else:
                pass
        except:
            pass
        finally:
            return exist

    # Method to delete doctor
    def delete_doctor(self, doc_data_dic):

        data_dic = {}
        new_data = {}
        file_name = "doctor.text"
        exist = False
        for key in doc_data_dic:
            try:
                data_dic[(key)] = doc_data_dic[key].get()
            except AttributeError:
                data_dic[(key)] = doc_data_dic[key]

        exist = self.check_doc_existence(data_dic)
        if (exist):
            new_data = fo.search_data_file(file_name, data_dic)

    # Retrieving all appointments
    def view_appointment(self, data, appointments):
        try:
            display_appointment = {}
            for appointment in appointments:
                # Retrieved using ID
                if (str(data['Appointment ID']) == appointment.get_appointment_id()):

                    display_appointment['First Name'] = appointment.get_patient_first_name(
                    )
                    display_appointment['Last Name'] = appointment.get_patient_last_name(
                    )
                    display_appointment['Contact Number'] = appointment.get_contact_number(
                    )
                    display_appointment['Age'] = appointment.get_age()
                    display_appointment['Email'] = appointment.get_email()
                    display_appointment['Symptoms'] = appointment.get_symptoms(
                    )
                    display_appointment['Address Line 1'] = appointment.get_address_line1(
                    )
                    display_appointment['Address Line 2'] = appointment.get_address_line2(
                    )
                    display_appointment['Status'] = appointment.get_appointment_status(
                    )
                    display_appointment['Post Code'] = appointment.get_post_code(
                    )
                    display_appointment['Appointment ID'] = appointment.get_appointment_id(
                    )
                    display_appointment['Patient ID'] = appointment.get_patient_id(
                    )
                    display_appointment['Admit'] = appointment.get_admit()
                    display_appointment['Doctor ID'] = appointment.get_doctor()
                    display_appointment['Appointment Date'] = appointment.get_appointment_date(
                    )
                    break
                else:
                    pass
        except:
            print("Error in retrieving the data")

        finally:
            return display_appointment

    def view_appointments(self, appointments):
        try:
            display_appointments = []
            for appointment in appointments:
                display_appointment = {}
                display_appointment['First Name'] = appointment.get_patient_first_name(
                )
                display_appointment['Last Name'] = appointment.get_patient_last_name(
                )
                display_appointment['Contact Number'] = appointment.get_contact_number(
                )
                display_appointment['Age'] = appointment.get_age()
                display_appointment['Email'] = appointment.get_email()
                display_appointment['Symptoms'] = appointment.get_symptoms()
                display_appointment['Address Line 1'] = appointment.get_address_line1(
                )
                display_appointment['Address Line 2'] = appointment.get_address_line2(
                )
                display_appointment['Status'] = appointment.get_appointment_status(
                )
                display_appointment['Post Code'] = appointment.get_post_code()
                display_appointment['Appointment ID'] = appointment.get_appointment_id(
                )
                display_appointment['Patient ID'] = appointment.get_patient_id(
                )
                display_appointment['Admit'] = appointment.get_admit()
                display_appointment['Doctor ID'] = appointment.get_doctor()
                display_appointment['Appointment Date'] = appointment.get_appointment_date(
                )

                display_appointments.append(display_appointment)

        except:
            print("Error in retrieving the data")

        finally:
            return display_appointments

    # Function to process the appointment request. First system checks if appointment exist for the patient. If Yes, booking new appointment is not allowed
    def confirm_appointment(self, entries, doctors, patients, appointments):
        try:
            appointment_status = False
            # Creating an appointment object
            for appointment in appointments:
                if (entries['Appointment ID'] == appointment.get_appointment_id()):
                    appointment_status = appointment.update_data_to_file(
                        entries, appointments)
                    break

            # If the appointment is updated successfully, set doctor to patient
            if appointment_status:
                for patient in patients:
                    if (entries['Patient ID'] == patient.get_unique_id()):
                        if entries['Status'] == 'Completed':
                            if entries['Admit'] == 'Admit':
                                entries['Admit'] = 'Discharged'
                            entries['Doctor ID'] = ''
                            status = patient.update_data_to_file(
                                entries, patients)
                            # Adding the doctor ID so that it can be used in Doctor file handking checks
                            entries['Doctor ID'] = patient.get_doctor().strip()

                        else:
                            patient.link(entries['Doctor ID'])
                            status = patient.update_data_to_file(
                                entries, patients)
                        if status:
                            # Linking the patient to the doctor. Entries dictionary has Doctor Id. Hence Patient is already linked to the doctor
                            for doctor in doctors:
                                doc_id = doctor.get_doctor_id()
                                if doctor.get_doctor_id() == entries['Doctor ID']:
                                    if entries['Status'] != 'Completed':

                                        doctor.add_patient(
                                            patient.get_unique_id())
                                    else:
                                        doctor.remove_patient(
                                            patient.get_unique_id())
                                    # #Retrieve the doctor data from the object to write to file with updated patient details
                                    doctor_data = {}
                                    doctor_data = self.view_doctor(
                                        entries, doctors)
                                    file_name = 'doctor.txt'
                                    status = fo.update_data_to_file(
                                        file_name, 'Doctor ID', doctor_data)
                        break  # Need to rollback appoitment if patient - update operation fails
            else:
                print("Appointment Creation Failed. Please re-try")

        except:
            print("Error in booking appointment")
        finally:
            return appointment_status

    def view_doctors(self, doctors):
        try:
            display_doctors = []

            for doctor in doctors:
                display_doctor = {}
                display_doctor['First Name'] = doctor.get_first_name()
                display_doctor['Last Name'] = doctor.get_last_name()
                display_doctor['Contact Number'] = doctor.get_contact_number()
                display_doctor['Age'] = doctor.get_age()
                display_doctor['Email'] = doctor.get_email()
                display_doctor['Speciality'] = doctor.get_speciality()
                display_doctor['Address Line 1'] = doctor.get_address_line1()
                display_doctor['Address Line 2'] = doctor.get_address_line2()
                display_doctor['Post Code'] = doctor.get_post_code()
                display_doctor['Doctor ID'] = doctor.get_doctor_id()
                display_doctor['Patients'] = doctor.retrieve_patient()

                display_doctors.append(display_doctor)
        except:
            print("Error in retrieving the doctor data")

        finally:
            return display_doctors
    
    #Retrieving doctor data
    def view_doctor(self, data, doctors):
        try:
            display_doctor = {}
            for doctor in doctors:
                if (str(data['Doctor ID']) == doctor.get_doctor_id()):

                    display_doctor['First Name'] = doctor.get_first_name()
                    display_doctor['Last Name'] = doctor.get_last_name()
                    display_doctor['Contact Number'] = doctor.get_contact_number()
                    display_doctor['Age'] = doctor.get_age()
                    display_doctor['Email'] = doctor.get_email()
                    display_doctor['Speciality'] = doctor.get_speciality()
                    display_doctor['Address Line 1'] = doctor.get_address_line1()
                    display_doctor['Address Line 2'] = doctor.get_address_line2()
                    display_doctor['Post Code'] = doctor.get_post_code()
                    display_doctor['Doctor ID'] = doctor.get_doctor_id()
                    display_doctor['Patients'] = doctor.retrieve_patient()

                    break
                else:
                    pass
        except:
            print("Error in retrieving the doctor data")

        finally:
            return display_doctor

    # Function to process the doctor data changes
    def update_doctor(self, entries, doctors, patients, appointments):
        try:
            doctor_update_status = False
            # Creating an appointment object
            for doctor in doctors:
                if (entries['Doctor ID'] == doctor.get_doctor_id()):
                    file_name = 'doctor.txt'
                    doctor_update_status = fo.update_data_to_file(
                        file_name, 'Doctor ID', entries)
                    break
        except:
            print("Error in updating doctor")
        finally:
            return doctor_update_status, entries['Doctor ID']

    # Function to delete the doctor from the system
    def delete_doctor(self, entries, doctors, patients, appointments):
        try:
            doctor_delete_status = False
            # Creating an appointment object
            for doctor in doctors:
                if (entries['Doctor ID'] == doctor.get_doctor_id()):
                    file_name = 'doctor.txt'
                    doctor_delete_status = fo.delete_data(
                        file_name, 'Doctor ID', entries)
                    break
        except:
            print("Error in deleting doctor")
        finally:
            return doctor_delete_status, entries['Doctor ID']
