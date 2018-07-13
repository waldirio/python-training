#!/usr/bin/env python

from datetime import datetime

def questions():
    # Questions here
    name = raw_input("Your Name: ")
    address = raw_input("Your Address: ")
    dt_bday = raw_input("Your Birthday Date (dd/mm/yyyy): ")

    # Filtering just the year of my bday
    year_from_my_bday = dt_bday.split("/")[2]

    # Collecting the actual year
    actual_year = datetime.now().year

    # My age according the year
    # age = actual_year-year_from_my_bday    # we will check this one
    age = actual_year-int(year_from_my_bday)

    # new line
    print("\n\n")

    # Printing everything
    print("Your name is {}".format(name))
    print("Your Address is {}".format(address))

    # Two diff ways, we can calculate here or just print the variable
    print("Your age is near {}".format(actual_year-int(year_from_my_bday)))
    print("Your age is near {}".format(age))


questions()
