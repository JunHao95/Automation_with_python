#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"
def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer_backup(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    min_date_employees_dict = {}
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue
        min_date_employees_dict[row[0]] = row[1]
        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.
        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        # If this date is the same as the current minimum,
        # we add the employee in this row to the list of
        # employees at the minimal date.
        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))

    return min_date, min_date_employees

data = get_file_lines(FILE_URL)
def get_same_or_newer(start_date,data):
    """Returns the employees that started on the given date, or the closest one."""
    reader = csv.reader(data[1:])
    min_date = datetime.datetime.today()
    min_date_employees_dict = {}
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        if row_date < start_date:
            continue
        if row_date < min_date:
            min_date = row_date
            min_date_employees_dict = {}
        if row_date == min_date:
            min_date_employees_dict[row[0] + " " + row[1]] = row_date

    #for k,v in min_date_employees_dict.items():
    #    if v < start_date:
    #        del min_date_employees_dict[k]
    keys = list(min_date_employees_dict.keys())
    for k in keys:
        if min_date_employees_dict[k] < start_date:
            del min_date_employees_dict[k]
    #print("My function output \n")
    #print( min_date, [k for k,v in sorted(min_date_employees_dict.items(),key=lambda p : p[1])])
    #print("End of my function output \n")
    return min_date, [k for k,v in sorted(min_date_employees_dict.items(),key=lambda p : p[1])]


def list_newer(start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date,data)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    #data = get_file_lines(FILE_URL)
    list_newer(start_date)

if __name__ == "__main__":
    main()
