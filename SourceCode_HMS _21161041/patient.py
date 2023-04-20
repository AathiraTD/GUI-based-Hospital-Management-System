# Loading Class Modules
from appointment import Appointment
from person import Person

# Loading tkinter messagebox for error display
from tkinter.messagebox import showinfo

# For generating unique ID
import uuid
import hashlib

# Loading module for file operations
import file_operations as fo


class Patient (Person):
    """Patient class"""
    # Passing patient  as a dictionary for __init__ method

    def __init__(self, pat):
        """
            Keyword arguments
        """
        self.__symptoms = pat[('Symptoms')]
        self.__patient_id = pat[('Patient ID')]
        self.__doctor_id = pat[('Doctor ID')]
        self.__admit = pat[('Admit')]
        self.__appointment_date = pat[('Appointment Date')]

        super().__init__(pat)

    def get_doctor(self):
        return self.__doctor_id

    # def get_contact_number(self) :
    #     return self.__contact_number

    def get_unique_id(self):
        return self.__patient_id

    def set_unique_id(self, value):
        self.__patient_id = value

    def get_symptoms(self):
        return self.__symptoms

    def get_admit(self):
        return self.__admit

    def set_admit(self, value):
        self.__admit = value

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        # ToDo4
        pass

    def get_appointment_date(self):
        return self.__appointment_date

    def set_appointment_date(self, value):
        self.__appointment_date = value

    def full_name(self):
        full_name = self.get_first_name() + ' ' + self.get_last_name()
        return full_name

    # Method to store patient data to file
    def store_data_to_file(self, entries, patients):
        try:
            write_status = False
            file_name = "patient.txt"
            patient_exist = self.check_patient_exist(entries, patients)
            if not patient_exist:
                # Patient is not exist in the system.
                value = entries.pop('Status', None)
                write_status = fo.store_data_to_file(entries, file_name)
        except:
            showinfo('Patient', 'Error in processing the request')
        finally:
            return write_status

    # Check if patient already exist in the system
    def check_patient_exist(self, entries, patients):
        try:
            exist = False
            if len(patients) != 0:
                for patient in patients:
                    if (entries['Patient ID'] == patient.get_unique_id()):
                        exist = True
                        return exist
            else:
                pass
        except:
            pass
        finally:
            return exist

    # Function to process the appointment request. First system checks if appointment exist for the patient. If Yes, booking new appointment is not allowed
    def book_appointment(self, entries, patients, appointments):
        try:
            appointment_status = False
            appointment_id = ''

            # Creating an appointment object. Check if appointment alredy exist for the patient. If not create a new appointment request
            app = Appointment(entries)

            # Generate Unique Id for Appointment and patient
            entries['Appointment ID'] = app.generate_unique_id(
                (entries['Contact Number']))
            entries['Patient ID'] = self.generate_unique_id(
                entries['Contact Number'])

            # If the appointment is created successfully, checks if patient exist or not. If not adds the patient to the system
            appointment_status = app.store_data_to_file(entries, appointments)
            # Proceed to patient file oprations
            if appointment_status:
                # Assigning ID to Patient
                self.set_unique_id(entries['Patient ID'])
                # Writing Patient data to file
                appointment_status = self.store_data_to_file(entries, patients)
                if appointment_status:
                    pass
                else:
                    # Revert modificaiton to appointment file. Current system ignores this. Can enhance  in the future
                    pass
            else:
                showinfo(
                    'Patient', 'Please check the existing appointment request status before raising another once.')
        except:
            showinfo('Patient', 'Error in processing the request')
        finally:
            return appointment_status, entries['Appointment ID']

    # Function to search appointment request
    def search_appointment(self, entries, patients, appointments):
        try:
            appointment_exist = False
            app_retrieve = {}

            for app in appointments:
                # Checking if appointment exist with mathcing input criteria. Haven't included Appointment ID in Ui as a criteria. Can enhance later.
                if (entries['First Name'] == app.get_patient_first_name() and entries['Last Name'] == app.get_patient_last_name() and app.get_appointment_status() != 'Closed'):
                    entries['Status'] = app.get_appointment_status()
                    entries['Admit'] = app.get_admit()
                    entries['Doctor'] = app.get_doctor()
                    entries['Appointment ID'] = app.get_appointment_id()
                    appointment_exist = True
                    break
        except:
            showinfo('Appointment', "Error in retrieving appointment")
        finally:
            return appointment_exist, entries

    # Method to update patient data in files
    def update_data_to_file(self, entries, patients):
        try:
            status = False
            file_name = "patient.txt"
            status = fo.update_data_to_file(file_name, 'Patient ID', entries)
        except:
            print("Error in processing update request")

        finally:
            return status

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
