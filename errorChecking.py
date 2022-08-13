# Set up this file to check for errors
#
#
#
# import adminGetVariables


def errorchecking(intcheck):
        try:
            intcheck = int(intcheck)
            return int(intcheck)
        except ValueError:
            # print("{} is not a number. Value must be within range of {}".format(intcheck))
            intcheck = 999999
            return int(intcheck)
