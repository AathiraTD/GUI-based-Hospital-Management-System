#For generating unique ID
import uuid
import hashlib


class Person:
    """A class that deals with the Person data which are common for Patients, Doctors and Admin"""
    
    def __init__(self, per):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = per[('First Name')]
        self.__last_name = per[('Last Name')]
        self.__email = per[('Email')]
        if 'Age' in per:
            self.__age = per[('Age')]
        self.__contact_number = per[('Contact Number')]
        self.__Address_Line_1 = per[('Address Line 1')]
        self.__Address_Line_2 = per[('Address Line 2')]
        self.__postcode = per[('Post Code')]
        

    
    def full_name(self) :
        full_name = self.get_first_name() + ' ' + self.get_last_name()
        return full_name

    def get_first_name(self) :
        return self.__first_name

    def set_first_name(self, new_first_name):
        #ToDo3
        pass

    def get_last_name(self) :
        return self.__last_name

    def set_last_name(self, last_name):
        #ToDo5
        pass
    
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
    
    def get_contact_number(self) :
        return self.__contact_number
    
    def get_unique_id (self):
        return self.__unique_id
    
    #Generate a unique ID
    def generate_unique_id(self, mobile_number):
        try:
            # Generate a UUID based on the mobile number
            mobile_uuid = uuid.uuid5(uuid.NAMESPACE_OID, mobile_number)
            # Get the hexadecimal representation of the UUID
            mobile_uuid_hex = mobile_uuid.hex
            # Generate a hash of the UUID hexadecimal representation
            unique_id = hashlib.sha256(mobile_uuid_hex.encode()).hexdigest()
            # Return the first 5 digits of the hash as the unique ID
            return unique_id[:5]
        except:
            pass
    

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
