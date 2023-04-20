# Loading Class Modules
from person import Person

# Loading tkinter messagebox for error display
from tkinter.messagebox import showinfo

#For generating unique ID
import uuid
import hashlib
import time


"""
Created on Sun Dec 25 14:00:41 2022

@author: aathira
"""

import file_operations as fo

# Definition of appointment class
class Appointment:
    """A class that deals with the Appointment"""
    #app is a dinctionary with appointment details.
    def __init__(self, app):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__patient_first_name = app[('First Name')]
        self.__patient_last_name = app[('Last Name')]
        self.__status = app[('Status')]
        self.__email = app[('Email')]
        self.__age = app[('Age')]
        self.__contact_number = app[('Contact Number')]
        self.__Address_Line_1 = app[('Address Line 1')]
        self.__Address_Line_2 = app[('Address Line 2')]
        self.__postcode = app[('Post Code')]
        self.__symptoms = app[('Symptoms')]
        self.__appointment_id = app[('Appointment ID')]
        if 'Patient ID' in app:
            self.__patient_id = app[('Patient ID')]
        self.__admit = app[('Admit')]
        self.__doctor_id = app ['Doctor ID']
        self.__appointment_date = app[('Appointment Date')]

    def get_patient_first_name(self) :
        return self.__patient_first_name

    def set_patient_first_name(self, new_first_name):
        #ToDo3
        pass

    def get_patient_last_name(self) :
        return self.__patient_last_name

    def set_patient_surname(self, new_surname):
        #ToDo5
        pass
    
    def get_doctor(self) :
        return self.__doctor_id
    
    def set_doctor(self, doctor_id) :
        self.__doctor_id = doctor_id
    
    def get_age (self):
        return self.__age
        
    def get_email (self):
        return self.__email
          
    def get_address_line1 (self):
        return self.__Address_Line_1
         
    def get_address_line2 (self):
        return self.__Address_Line_2
    
    def get_post_code (self):
        return self.__postcode
    
    def get_appointment_status (self):
        return self.__status
    
    def get_symptoms (self):
        return self.__symptoms
    
    def set_appointment_status (self, status):
        self.__status = status
    
    def get_post_code (self):
        return self.__postcode
    
    def get_admit (self):
        return self.__admit
    
    def set_admit (self, value):
        self.__admit = value
    
    def get_contact_number (self):
        return self.__contact_number
    
    def get_appointment_id (self):
        return self.__appointment_id
    
    def get_patient_id (self):
        return self.__patient_id

    def set_appointment_id (self, value):
        self.__appointment_id = value
    
    def get_appointment_date(self):
        return self.__appointment_date
    
    def set_appointment_date(self, value):
         self.__appointment_date = value
        
    # Function to check if an appointment exist for the patient for the same symptom. System only supports only one active appointment per patient for a symptom at a time
    def check_appointment_existence (self,entries, appointments):
        try:
            appointment_exist = False
            for appointment in appointments:
                if (entries['Appointment ID'] == appointment.get_appointment_id()) :
                    appointment_exist = True
                    break        
        except:
            print("Exception occured in checking appointments")
        
        finally:
            return appointment_exist, appointment.get_appointment_status()
    
    # Function writes appointment data to file
    def store_data_to_file (self, entries, appointments):
        try:        
            status = False
            id = ''
            file_name = "appointment.txt"
            # Check if appointment already exist for the paatient
            appointment_exist = False
            appointment_status = ''
            # Checks if appointment already exists, If not exists, appointment request is generated
            if len(appointments) !=0:
                appointment_exist, appointment_status = self.check_appointment_existence (entries, appointments)
            
            if appointment_exist :
                showinfo('Appointment', 'Another open appointment request exist for you. You will be notified once we process the request')
            else:
                # Setting appointment status to 'Pending'. Post Admin confirmation status will be updated
                entries['Status'] = 'Pending' 
                # File operation to write appointment request to file
                status = fo.store_data_to_file (entries, file_name)
                if status:
                    self.set_appointment_status('Pending')
                else:
                    showinfo('Appointment', 'Error in saving appointment request to system. Please re-try')
        except:
            showinfo('Appointment', 'Error in processing appointment request. Please re-try')
        
        finally:
            return status
        
    #Generate a unique ID.Since system should allow multiple appointments for a patient (at different time points) added timestamp as another criteria
    def generate_unique_id(self, mobile_number):
        try:
            # Concatenate the mobile number with the current timestamp
            input_string = f"{mobile_number}{time.time()}"
            # Generate a UUID based on the mobile number
            mobile_uuid = uuid.uuid5(uuid.NAMESPACE_OID, mobile_number)
            # Get the hexadecimal representation of the UUID
            mobile_uuid_hex = mobile_uuid.hex
            # Generate a hash of the UUID hexadecimal representation
            unique_id = hashlib.sha256(mobile_uuid_hex.encode()).hexdigest()
            # Return the last 5 digits of the hash as the unique ID
            return unique_id[:5]
        except:
            pass    
    
    # Method to update Appointmnent data in files    
    def update_data_to_file (self, entries, appointments):
        try:        
            status = False
            file_name = "appointment.txt"

            # Checks if appointment already exists, If not exists, appointment request is generated
            appointment_exist, appointment_status = self.check_appointment_existence (entries, appointments)
            if appointment_exist :
                if appointment_status !='Completed':
                    self.set_appointment_status('Confirmed')
                    self.set_appointment_date(entries['Appointment Date'])
                    # File operation to write appointment request to file
                    status = fo.update_data_to_file (file_name, 'Appointment ID', entries)
                else:
                    showinfo('Appointment', 'Appointment is already completed')
            else:
               
                  showinfo('Appointment', 'Unable to retrive appointment. Please re-try')
        except:
            showinfo('Appointment', 'Unable to process the request. Please re-try')
        
        finally:
            return status
        
    def __str__(self) :
        return f'{self.patient_first_name():^30}|{self.__patient_surname:^15}'
