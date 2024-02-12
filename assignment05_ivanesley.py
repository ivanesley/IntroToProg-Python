# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Ivan Esley, 2/12/24, Final edits/submission
# ------------------------------------------------------------------------------------------ #

import csv

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # setting student_data as dictionary
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
def load_from_csv():
    try:
         with open(FILE_NAME, "r") as file:
            column_names = ("first_name", "last_name", "course_name")
            all_rows = csv.DictReader(file, fieldnames=column_names)
            for row in all_rows:
             students.append(row) 
         print("INFO: All rows loaded from the database file!")
    except FileNotFoundError as error_message:
        print("ERROR: Database file not found")
        print(f"Error detail: {error_message}")
    except ValueError as error_message:
        print("ERROR: There was a value error exception when trying to open the file")
    finally:
        print ("Reader check")

def save_to_csv(): # Saves all information to CSV file
    print(students)
    with open(FILE_NAME,'w') as file_obj:
        for row in students:
            csv_data = f"{row["first_name"]},{row["last_name"]},{row["course_name"]}\n"
            file_obj.write(csv_data) 


def register_student(): # Adds user to database
    student_first_name = input("Enter the student's first name: ")
    if not student_first_name: # Checks if student_first_name is an empty string
        print("ERROR: Student first name cannot be empty!")
        return
    
    student_last_name = input("Enter the student's last name: ")
    if not student_last_name: # Checks if student_last_name is an empty string
        print("ERROR: Student last name cannot be empty!")
        return
    
    course_name = input("Please enter the name of the course: ")
    if not course_name: # Checks if course_name is an empty string
        print("ERROR: Course name cannot be empty!")
        return
    
    student_data = {   # Creates dictionary of the inputted student data
        "first_name": student_first_name,
        "last_name": student_last_name,
        "course_name": course_name
    }
    students.append(student_data)
    
    print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        
    
# Present and Process the data
while (True): 

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
       register_student()
        
    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["first_name"]} {student["last_name"]} is enrolled in {student["course_name"]}")
        print("-"*50)
        continue

 # Save the data to a file
    elif menu_choice == "3":
        save_to_csv()

 # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
