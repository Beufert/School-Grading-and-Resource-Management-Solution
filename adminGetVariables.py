# Imports
import errorChecking
import update_files
import random
#
# Variables
#
# Student Variables


studentFirstName, studentLastName = '', ''
# TODO: Need to create a function to create ID values and store them
studentID = 0

# Teacher Variables
teacherFirstName, teacherLastName = '', ''
teacherID = 0

# Class Variables
classID, classGradeLevel, assignmentPoints = 0, 999, 0
assignment = ''
classType = ["Math", "English", "Science", "Social Studies", "Physical Education", "Music", "Special Education"]
classRoomNum = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
# Functional Application Variables
continueLoop = ''
action = 0
status, tempBool = True, True
errorBool = False

# These are output texts for user instructions - allows to pass values to error checking, reducing code while
# giving the users information needed to correctly use the application
gradeTitle = "0 - 12 (0 = Kindergarten)"

# intro into application

print("Welcome to Brizer Grading System!!")
print("*" * 80)
while tempBool:
    while action == 0:
        try:  # Telling user what to input, checking if the value they put is an number
            action = int(input("Please select a number from the options below: "
                               "\n 1. Add a new student "
                               "\n 2. Add a new teacher "
                               "\n 3. Give a student a grade "          
                               "\n Pick 1-3:  "))
        except ValueError:
            print("You did not input a number.")
            print("*" * 80)
            continue

    # Entering selected menu, restarts if user inputs value outside of range (1-3)

    # This section is for adding a Student
    if action == 1:
        #
        # Get Student's Names
        continueLoop = 'student'    # option later asks if you want to add more *blank*
        studentFirstName = input("What is the student's first name? ")
        studentLastName = input("What is the student's last name? ")
        classGradeLevel = input("What grade is {} in? {} ".format(studentFirstName, gradeTitle))
        classGradeLevel, gradeTitle, errorBool = errorChecking.errorcheckingintegers(classGradeLevel, gradeTitle, errorBool)
        print("We've added {} {}, Grade {}, to the school roster.".format(studentFirstName, studentLastName, classGradeLevel))
        update_files.writestudentstofile(studentFirstName, studentLastName, classGradeLevel, studentID, errorBool)
        studentFirstName, studentLastName, classGradeLevel, studentID = '', '', '', ''
        errorBool = False

    elif action == 2:
        #
        # Get Teacher's Names
        continueLoop = 'teacher'
        teacherFirstName = input("What is the teacher's first name? ")
        teacherLastName = input("What is the teacher's last name? ")
        classGradeLevel = input("What grade will Mr./Mis./Miss. {} be teaching? {} ".format(studentLastName, gradeTitle))
        classGradeLevel, gradeTitle, errorBool = errorChecking.errorcheckingintegers(classGradeLevel, gradeTitle, errorBool)
        print("We've added {} {}, Grade {}, to the school staff.".format(teacherFirstName, teacherLastName, classGradeLevel))
        update_files.writeteacherstofile(teacherFirstName, teacherLastName, classGradeLevel, teacherID, errorBool)
        teacherFirstName, teacherLastName, classGradeLevel, teacherID = '', '', '', ''
        errorBool = False

    elif action == 3:
        print("Please select the student: ")
        with open("Active_Students.txt") as students:
            studentlist = students.read()
            print(studentlist)
            students.close()
        studentID = input("Please input the student ID, located to the left of the student's name. Format: xxGx.")
        assignmentPoints = int(input("What grade did they get? "))

        print("We've added {} to {}.{}'s grade-book.".format(assignmentPoints, studentID, studentFirstName))

        # This is a substitute value for the option later to continue adding whatever value is in 'ContinueLoop'
        continueLoop = 'grade'

    # Restarts to menu as they did not input a correct number
    else:
        print("You did not pick a number from 1 - 3, try again. ")
        print("*" * 80)
        action = 0

    if action in range(1, 4):
        print("*" * 80)
        tempVal = input("Do you want to add another {}?  Yes or No? ".format(continueLoop))
        print("*" * 80)
        if tempVal not in ("Yes", "yes"):
            tempVal = input("Do you want to add something else? ")
            if tempVal not in ("Yes", "yes"):
                tempBool = False
            else:
                action = 0
