# To check for input validation - make scalable by taking in any number within code

def errorcheckingintegers(intcheck, gradetitle, errorbool):
    while errorbool == False:
        try:
            intcheck = int(intcheck)
            if intcheck in range(0, 13):
                errorbool = True
                return intcheck, gradetitle, errorbool
            else:
                intcheck = input("Your input is invalid, please select a number from {}. ".format(gradetitle))
        except ValueError:
            intcheck = input("Your input is invalid, please select a number from {}. ".format(gradetitle))


