# Define the Student class with getter and setter methods for student attributes
from datetime import datetime


class Student:

    students = []  # List to store instances of students

    # Constructor to initialize student attributes
    def __init__(self, stdNumber, firstName, lastName, dateOfBirth, sex, countryOfBirth):
        self._stdNumber = stdNumber
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._sex = sex
        self._countryOfBirth = countryOfBirth

    # Getter methods for retrieving student attributes
    def get_stdNumber(self):
        return self._stdNumber

    def get_firstName(self):
        return self._firstName

    def get_lastName(self):
        return self._lastName

    def get_dateOfBirth(self):
        return self._dateOfBirth

    def get_sex(self):
        return self._sex

    def get_countryOfBirth(self):
        return self._countryOfBirth

    def get_age(self):
        # Assuming date of birth is in "DD/MM/YYYY" format
        dob = datetime.strptime(self._dateOfBirth, "%d/%m/%Y")
        today = datetime.now()
        age = today.year - dob.year - \
            ((today.month, today.day) < (dob.month, dob.day))
        return age

# Main class inherits from Student


class Main(Student):

    # Function to add a new student
    def addNewStudent():
        try:
            stdNumber = int(input("Enter Std Number: "))
            fName = str(input("Enter First Name: "))
            lName = str(input("Enter Last Name: "))
            dateOfBirth = input("Enter Date of Birth (DD/MM/YYYY): ")
            sex = str(input("Enter your gender (M/F): "))
            countryOfBirth = str(input("Enter country of birth: "))

            # Create a new Student instance
            new_student = Student(stdNumber=stdNumber, firstName=fName, lastName=lName,
                                  dateOfBirth=dateOfBirth, sex=sex, countryOfBirth=countryOfBirth)

        except ValueError:
            print("Invalid input. Please enter valid data")
            return

        with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Python Projects\student.txt", "a") as f:
            f.write(f"{new_student.get_stdNumber()} {new_student.get_firstName()} {new_student.get_lastName()} {new_student.get_dateOfBirth()} {new_student.get_sex()} {new_student.get_countryOfBirth()}\n")

        # Append the new student to the list of students
        Student.students.append(new_student)
        print("Student Added")

    # Function to find a student by student number.
    # This function also reads the data from the file and finds the students from there.
    def findStudent():
        found_students = False

        # Get the student number from the user
        stdNum = input("Enter Student Number: ")

        # Open the student data file in read mode
        with open(r"\Users\\yusuf\OneDrive\Masaüstü\Python Projects\student.txt", "r") as f:
            # Iterate through each line in the file
            for line in f:
                data = line.strip().split()

                # Check if the student number matches
                if data[0] == stdNum:
                    print("Match Found")
                    print(f"Student Number: {data[0]}")
                    print(f"First Name: {data[1]}")
                    print(f"Last Name: {data[2]}")
                    print(f"Date of Birth: {data[3]}")
                    print(f"Gender: {data[4]}")
                    print(f"Country of Birth: {data[5]}")

                    # Calculate and print the age
                    dob = datetime.strptime(data[3], "%d/%m/%Y")
                    today = datetime.now()
                    age = today.year - dob.year - \
                        ((today.month, today.day) < (dob.month, dob.day))
                    print(f"Age: {age}")

                    found_students = True
                    break

            # Print a message if no match is found
            if not found_students:
                print("Sorry, Match Not Found")

    # Function to read and display all student data from the file.
    def readStudentData():
        # Open the student data file in read mode
        with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Python Projects\student.txt", "r") as f:
            # Iterate through each line in the file
            for line in f:
                data = line.strip().split()

                # Create a new Student instance
                student = Student(stdNumber=data[0], firstName=data[1], lastName=data[2],
                                  dateOfBirth=data[3], sex=data[4], countryOfBirth=data[5])

                # Display all student information, including age
                print(f"{student.get_stdNumber()} {student.get_firstName()} {student.get_lastName()} "
                      f"{student.get_dateOfBirth()} {student.get_sex()} {student.get_countryOfBirth()} "
                      f"{student.get_age()}")

    # This function reads the data from the file.
    # Then prints the students for the given year.
    def showByYear():
        from datetime import datetime

        # Get the year from the user
        year = input("Enter Year: ")

        found_students = False  # Flag to check if any students are found for the given year
        student_count = 0  # Counter for the students found

        file_path = r"C:\Users\yusuf\OneDrive\Masaüstü\Python Projects\student.txt"

        # Open the student data file in read mode
        with open(file_path, "r") as f:
            # Iterate through each line in the file
            for line in f:
                data = line.strip().split()

                # Assuming data[3] is the date of birth in "DD/MM/YYYY" format
                try:
                    # Parse the date string to a datetime object
                    date_of_birth = datetime.strptime(data[3], "%d/%m/%Y")

                    # Check if the year matches
                    if date_of_birth.year == int(year):
                        student_count += 1
                        print(
                            f"{student_count}. {data[0]} {data[1]} {data[2]} {data[3]} {data[4]} {data[5]}")
                        found_students = True

                except ValueError:
                    # Handle invalid date format
                    print(f"Invalid date format for student: {data[3]}")

        # Print a message if no students are found for the given year
        if not found_students:
            print("Sorry, No Student Found in the records for the year", year)

    # Function to modify a student record.
    # This function modifies stdno,name, dob,gender,cob.
    def Modify():
        stdNum = input("Enter Student No: ")

        # Open the student data file in read and write mode
        with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Python Projects\student.txt", "r+") as f:
            lines = f.readlines()
            found_student = False

            # Iterate through each line in the file
            for i, line in enumerate(lines):
                data = line.strip().split()

                # Check if the student number matches
                if data[0] == stdNum:
                    print("Student found:")
                    print(
                        f"{data[0]} {data[1]} {data[2]} {data[3]} {data[4]} {data[5]}")
                    found_student = True

                    # Get user choice for modification
                    choice = input(
                        "1. StdNo, 2. First Name, 3. Last Name, 4. Date of Birth, 5. Sex, 6. Country of Birth: ")

                    # Handle different modification choices
                    if choice == "1":
                        new_stdNo = input("Enter new student number: ")
                        data[0] = new_stdNo
                        lines[i] = ' '.join(data) + '\n'
                        print("Student Number changed successfully")
                        break

                    elif choice == "2":
                        fname = input("Enter student first name: ")
                        data[1] = fname
                        lines[i] = ' '.join(data) + '\n'
                        print("First name changed successfully")
                        break

                    elif choice == "3":
                        lname = input("Enter student last name: ")
                        data[2] = lname
                        lines[i] = ' '.join(data) + '\n'
                        print("Last name changed successfully")
                        break

                    elif choice == "4":
                        Date = input(
                            "Enter student Date of Birth (DD/MM/YYYY): ")
                        data[3] = Date
                        lines[i] = ' '.join(data) + '\n'
                        print("Date of Birth changed successfully")
                        break

                    elif choice == "5":
                        sex = input("Enter student's gender (M/F): ")
                        data[4] = sex
                        lines[i] = ' '.join(data) + '\n'
                        print("Gender changed successfully")
                        break

                    elif choice == "6":
                        country = input("Enter student country of birth: ")
                        data[5] = country
                        lines[i] = ' '.join(data) + '\n'
                        print("Country of birth changed successfully")
                        break

            # Print a message if no student is found with the given student number
            if not found_student:
                print("No student found with the given student number")

            # Move the file pointer to the beginning and overwrite the content
            f.seek(0)
            f.writelines(lines)

    # Function to delete a student.
    def delete():
        stdNum_to_delete = input("Enter Student Number: ")

        # Open the student data file in read mode
        with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Python Projects\student.txt", "r") as f:
            lines = f.readlines()

        # Open the student data file in write mode
        with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Python Projects\student.txt", "w") as f:
            for line in lines:
                data = line.strip().split()

                # Check if the student number matches
                if data[0] != stdNum_to_delete:
                    f.write(line)

        print("Student deleted")

    # Function to quit the program
    def Quit():
        quit()


while True:
    # Display the menu options
    print("1: Add a new student")
    print("2: Find a student by student number")
    print("3: Show all students")
    print("4: Show all students by given year")
    print("5: Modify a student record")
    print("6: Delete a student with a specific student number")
    print("7: Quit ")

    # Get user choice
    choice = input("Enter your Choice:")

    # Perform the corresponding action based on user choice
    if choice == "1":
        Main.addNewStudent()

    elif choice == "2":
        Main.findStudent()

    elif choice == "3":
        Main.readStudentData()

    elif choice == "4":
        Main.showByYear()

    elif choice == "5":
        Main.Modify()

    elif choice == "6":
        Main.delete()

    elif choice == "7":
        Main.Quit()
        break
    else:
        print("You have to enter number between 1-7")
