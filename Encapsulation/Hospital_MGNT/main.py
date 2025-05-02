from system import Hospital_Management

if __name__ == "__main__":

	# Create object or Hospital_Management class.
	system = Hospital_Management()

	print("*********************************************Welcome to Hospital Management System.*****************************************************")
	print("1. Add Doctor.")
	print("2. Add Patient.")
	print("3. View Doctor Detail.")
	print("4. view Patient Detail.")
	print("5. Close System.")
	print("**********************************")

	# getting user choice.
	choice = int(input("Enter your choice : "))

	if choice == 1:
		print("***************************Enter Doctor Details**************************")
		name = str(input("Enter Name : "))
		email = str(input("Enter Email : "))
		gender = str(input("Enter Gender : "))
		phone_no = (input("Enter Phone Number : "))
		qualification = str(input("Enter qualification : "))
		experience = int(input("Enter experience in number : "))
		department = str(input("Enter YOur Department : "))


		system.add_doctor_or_patient(
			name : 'name',
			email : 'email',
			gender : 'gender',
			phone_no : 'phone_no',
			qualification : 'qualification',
			experience : 'experience',
			department : 'department',
			role : 'is_doctor'
			)


	elif choice == 2:
		pass
	elif choice == 3:
		pass
	elif choice == 4:
		pass
	elif choice == 5:
		print("*******************Closing System.*****************")
		exit()
	else:
		print("Invalid choice please enter between 1 to 5.")

