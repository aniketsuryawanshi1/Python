""" Project : Hospital Management System. """

"""

Create a class HospitalManagementSystem
    - That have database for that use Dictionary and list. in constructor.
    
    - After that define functions for Perform Task.
    
    - Functions in HospitalManagementSystem.
        - HospitalManagementSystem
       
            1. Add_Doctor_Patient.
            2. View_Patient_OR_Doctor_Details.
            3. Update_Patient_OR_Doctor_Details.
            4. Delete_Patient_OR_Doctor.
            5. Search_Patients_OR_Doctors.
            
        - HospitalManagement_DB
            
            1. Doctor
                - doctor_name.
                - doctor_gender.
                - doctor_email.
                - doctor_phone_number.
                - doctor_qualification.
                - doctor_experience.
                - role
                
   
"""


import re
class HospitalManagementSystem:

    def __init__(self):
        self.__hospital_db = {}

    def add_doctor_or_patient(self, **details):
        # getting role of user to store data.
        role = details.get('role') # getting doctor role is_doctor or is_patient.

        # Check is_doctor or not.
        if role == 'is_Doctor':
            email = details.get('doctor_email')
            # Check if doctor is exist with this email.
            if email in self.__hospital_db:
                print(f"Doctor {email} already exists.")
            else:
                # Save data in database.
                self.__hospital_db[email] = {
                    '_role': role,
                    "_doctor_name": details.get('doctor_name'),
                    "_doctor_gender": details.get('doctor_gender'),
                    "_doctor_phone_number": details.get('doctor_phone_number'),
                    "_doctor_qualification": details.get('doctor_qualification'),
                    "_doctor_experience": details.get('doctor_experience'),
                    "_doctor_department": details.get('doctor_department'),
                }

                print(f"Doctor {email} added successfully.")

        # Check is_patient or not.
        elif role == 'is_Patient':
            email = details.get('patient_email')
            doctor_email = details.get('doctor_email')

            # Check patient is already exist or not.
            if email in self.__hospital_db:
                print(f"Patient {doctor_email} already exists.")
            # Check doctor is exist in hospital or not.
            elif doctor_email not in self.__hospital_db:
                print(f"Doctor with email {doctor_email} does not exist.")
            else:
                # Save Patient in database.
                self.__hospital_db[email] = {
                    "_patient_name": details.get('patient_name'),
                    "_patient_gender": details.get('patient_gender'),
                    "_patient_phone_number": details.get('patient_phone_number'),
                    "_patient_age" : details.get('patient_age'),
                    "_patient_address": details.get('patient_address'),
                    "_patient_insurance": details.get('patient_insurance'),
                    "_patient_medical_history": details.get('patient_medical_history'),
                    "_patient_doctor_name": details.get('patient_doctor_name'),
                }
                print(f"Patient {doctor_email} added successfully.")

    def View_Patient_OR_Doctor_Details(self, email):
        """
        View the details of a doctor or patient by their email.
        """
        if email not in self.__hospital_db:
            print(f"No record found for email: {email}")
            return

        data = self.__hospital_db[email]
        print("**************************************************")
        print(f"Details for {email} ({data.get('_role', 'Unknown Role')})")
        print("--------------------------------------------------")
        for key, value in data.items():
            if key != '_role':
                label = key.lstrip('_').replace('_', ' ').title()
                print(f"{label}: {value}")
        print("**************************************************")

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        print("Invalid email. Please try again.")
        return False

def validate_name(name):
    if name and len(name.strip()) > 3:
        return True
    else:
        print("Name must be at least 3 characters long.")
        return False

def validate_gender(gender):
    valid_genders = ['Male', 'Female', 'Other']
    if gender.capitalize() not in valid_genders:
        print("Invalid gender. Please try again.")
        return False
    else:
        return True

def validate_phone_number(phone_number):
    if phone_number.isdigit() and len(phone_number.strip()) == 10:
        return True
    else:
        print("Invalid phone number. Please try again.")
        return False
def validate_experience(experience):
    if experience.isdigit() and int(experience) >= 0 and int(experience) >=0:
        return True
    else:
        print("Invalid experience. Please try again.")
        return False

def validate(email, name, gender, phone_number,experience):
    return (
        validate_email(email) and
        validate_name(name) and
        validate_gender(gender) and
        validate_phone_number(phone_number) and
        validate_experience(experience)
    )


while True:

    # Create class object.
    obj = HospitalManagementSystem()

    print("\nWelcome to the Hospital Management System!")
    print("1. Add Doctor.")
    print("2. Add Patient.")
    print("3. Get Patient Details.")
    print("4. Get Doctor Details.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        email = input("Enter Doctor email : ")
        name = str(input("Enter Doctor name : "))
        gender = str(input("Enter Doctor gender : "))
        phone_number = input("Enter Doctor phone number : ")
        qualification = str(input("Enter Doctor qualification : "))
        experience = str(input("Enter Doctor experience : "))
        department = str(input("Enter Doctor department : "))
        role = "is_doctor"

        # validate method call
        res = validate(email, name, gender, phone_number,experience)
        if res:
            obj.add_doctor_or_patient(
                role=role,
                doctor_email=email,
                doctor_name=name,
                doctor_gender=gender,
                doctor_phone_number=phone_number,
                doctor_qualification=qualification,
                doctor_experience=experience,
                doctor_department=department,
            )
        else:
            print("Please enter a valid details.")

    elif choice == 2:
        email = input("Enter Patient email : ")
        name = str(input("Enter Patient name : "))
        gender = str(input("Enter Patient gender : "))
        phone_number = input("Enter Patient phone number : ")
        department = str(input("Enter Patient department : "))
        age = int(input("Enter Patient age : "))
        address = str(input("Enter Patient address : "))
        insurance = str(input("Enter Patient insurance : "))
        medical_history = str(input("Enter Patient medical history : "))
        doctor_name = str(input("Enter Patient doctor name : "))
        role = "is_patient"

        res = validate(email, name, gender, phone_number,age)
        if res:
            obj.add_doctor_or_patient(
                role=role,


            )