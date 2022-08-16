# To check for input validation - make scalable by taking in any number within code

def errorcheckingintegers(intcheck, gradetitle, errorbool):
    try:
        intcheck = int(intcheck)
        if intcheck in range(0, 13):
            errorbool = True
            return intcheck, errorbool
        else:
            intcheck = input("Your input is invalid, please select a number from {}. ".format(gradetitle))
            errorcheckingintegers(intcheck, gradetitle)
    except ValueError:
        intcheck = 9999
        errorcheckingintegers(intcheck, gradetitle)
