#!/bin/python3
# Problem - Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Split the string into 3 different segments by the ":"
    s = s.split(":")

    # The last item will be "00PM" so slice the last item to see if it is AM or PM
    meridian = s[-1][2:]

    # Because the problem requires writing the answer to an output path for Unit Testing, return the result instead of my usual print
    if meridian == "PM" and s[0] != "12":
        s[0] = int(s[0]) + 12
        return f"{s[0]}:{s[1]}:{s[2][:-2]}"

    elif meridian == "AM" and s[0] == "12":
        s[0] = "00"
        return f"{s[0]}:{s[1]}:{s[2][:-2]}"

    else:
        return f"{s[0]}:{s[1]}:{s[2][:-2]}"


# Provided main by HackerRank
if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
