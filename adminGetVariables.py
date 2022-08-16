# Imports
import errorChecking
import update_files
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
classRoomNum, classID, classGradeLevel, assignmentPoints = 0, 0, 999, 0
assignment, classType = '', ''

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
        try: # Telling user what to input, checking if the value they put is an number
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
        #
        # Get Student's Names
        continueLoop = 'student'
        studentFirstName = input("What is the student's first name? ")
        studentLastName = input("What is the student's last name? ")
        #
        # Get Student's Grade - Grade default set to 0, here we ask for number value for the grade
        # We will also pass the value to Error Checking.py To check if the input is an integer
        while classGradeLevel == 999:
            classGradeLevel = input("What grade is {} in? {} ".format(studentFirstName, gradeTitle))
            classGradeLevel, errorBool = errorChecking.errorcheckingintegers(classGradeLevel, gradeTitle, errorBool)


            # Check if they provided a valid grade level
            if classGradeLevel in range(0, 13) and errorBool:
                print("We've added {} {}, grade {}, to the school roster.".format(studentFirstName, studentLastName, classGradeLevel))
                update_files.writestudentstofile(studentFirstName, studentLastName, classGradeLevel, studentID)
                studentFirstName, studentLastName = '', ''
                classGradeLevel, studentID = 0, 0
                errorBool = True
                break
            else:
                print("Your input is invalid, please select a number from {}. ".format(gradeTitle))
                classGradeLevel = 0
                continue
        # This is a substitute value for the option later to continue adding whatever value is in 'ContinueLoop'



    elif action == 2:
        teacherFirstName = input("What is the teacher's first name? ")
        teacherLastName = input("What is the teacher's last name? ")
        classGradeLevel = input("What grade will Mr./Mis./Miss. {} be teaching? {} ".format(studentLastName, gradeTitle))
        classGradeLevel = errorChecking.errorcheckingintegers(classGradeLevel)

        print("We've added {} to the staff roster.".format(teacherFirstName))

        # This is a substitute value for the option later to continue adding whatever value is in 'ContinueLoop'
        continueLoop = 'teacher'

    elif action == 3:
        assignmentPoints = int(input("What grade did they get? "))

        print("We've added {} to {}.{} grade-book.".format(assignmentPoints, studentID, studentFirstName))

        # This is a substitute value for the option later to continue adding whatever value is in 'ContinueLoop'
        continueLoop = 'grade'

    else:
        print("You did not pick a number from 1 - 3, try again.")
        print("*" * 80)
        action = 0

    if action in range(1, 4):
        print("*" * 80)
        tempVal = input("Do you want to add another {}?  Yes or No?".format(continueLoop))
        print("*" * 80)
        if tempVal not in ("Yes", "yes"):
            tempVal = input("Do you want to add something else? ")
            if tempVal not in ("Yes", "yes"):
                tempBool = False
            else:
                action = 0
