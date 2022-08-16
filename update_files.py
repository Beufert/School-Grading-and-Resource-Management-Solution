# This file will be used to take inputs from the user and add it to the specific file

student_filename = "Active_Students.txt"

def writestudentstofile(fname, lname, grade, sID, errorbool):
    with open(student_filename, "a") as students:
        student = "{}G{}: {} {}\n".format(sID, grade, fname, lname)
        students.write(student)
        fname, lname = '', ''
        grade = 0
        errorbool = True
        students.close()
        return fname, lname, grade, errorbool
