# End Game: Function for inputting grade for student
# variables
import errorChecking

studentName, teacherName, continueLoop, classRoomNum, classType, assignment = '', '', '', '', '', ''

# These are output texts for user instructions - allows to pass values to error checking, reducing code
gradeTitle = "0 - 12 (0 = Kindergarten)"

schoolGrade = 0

grade, assignmentPoints = 0, 0

action = 0

# intro into application

#
# Temp value to control leaving loop
#
tempBool = True
print("Welcome to Brizer Grading System!!")
print("*" * 80)
while tempBool:
    while action == 0:
        try:
            action = int(input("Please select a number from the options below: "
                               "\n 1. Add a new student "
                               "\n 2. Add a new teacher "
                               "\n 3. Give a student a grade "          
                               "\n Pick 1-3:  "))
        except ValueError:
            print("You did not input a number.")
            print("*" * 80)
            continue
    #
    # Need to make it so when the users puts in a value other than a number for the question above, it doesn't crash
    ##
    if action == 1:
        studentName = input("What is the student's name? ")
        while schoolGrade == 0:
            schoolGrade = input("What grade is this student in? ")
            schoolGrade = errorChecking.errorchecking(schoolGrade)
            if schoolGrade in range(0, 13):
                print("We've added {}, grade {}, to the school roster.".format(studentName, schoolGrade))
                studentName = ''
                schoolGrade = 0
                break
            else:
                print("Your input is invalid, please select a number from {}. ".format(schoolGrade, gradeTitle))
                schoolGrade = 0
                continue

        continueLoop = 'student'

    elif action == 2:
        teacherName = input("What is the teacher's name? ")
        print("We've added {} to the staff roster.".format(teacherName))
        continueLoop = 'teacher'

    elif action == 3:
        grade = int(input("What is the teacher's name? "))
        print("We've added {} to the school roster.".format(grade))
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
