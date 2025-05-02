# Import Required models.
from models.doctor import Doctor
from models.patient import Patient

class Hospital_Management:
	
	def __init__(self):
		# Create hospital database.
		self.__hospital_db = {}

		"""" Adding Doctor and patient. """
	def add_doctor_or_patient(self, **details):
		# Getting user role.
		role = details.get('role')

		# check user role.
		if role == 'is_doctor':
			
			# get email id for checking user already exist or not.
			email = details.get('email')

			# check user is exist or not.
			if email in self.__hospital_db:
				return print(f"Doctor with email {email} is already exisit.")

			# Assigining data to the fields
			doctor = Doctor(**details)

			# Store in database.
			self.__hospital_db[email] = {
			'data': doctor
			}

			print(f"Doctor {email} added successfully.")

		elif role == 'is_patient':
			
			# geting email.
			email = details.get('email')

			# Check user is already exisit or not.
			if email in self.__hospital_db:
				return print(f"Patient with email {email} is already exist.")

			patient = Patient(**details)

			self.__hospital_db[email] = {
			'data' : patient
			}

			print(f"Patient {email} added successfully.")

	""" Showing Doctor and patient data. """
	def view_doctor_or_patient_details(self, email):
		# check user is exisist or not.
		if email not in self.__hospital_db:
			return print(f"No record found for {email}")

		# getting data of that user.
		user = self.__hospital_db[email]			

		# geting user role.
		role = user['role']

		# getting user data.
		details = user['data'].get_info()

		# checking user role to show user data.

		if role == "is_doctor":
			print("*************************************Doctor Details***************************************")
			for key, value in details.items():
				print(f"Doctor {key.title() : {value}}")
			print("********************************************************************************************")

		elif role == "is_patient":
			print("*************************************Patient Details***************************************")
			for key, value in details.items():
				print(f"Patient {key.title() : {value}}")
			print("********************************************************************************************")


