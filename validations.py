import re
from dateutil import parser
from datetime import datetime
def isempidvalid(i):
    if i.isdigit():
        if len(i) == 6:
            return True
        else:
            print("Length must be 6 digit!")
            return False
    else:
        print("All the elements must be digit!")
        return False


def isnamevalid(name):
    l = list(name.split())
    flag = 1
    for i in l:
        if i.isalpha():
            if i.istitle():
                flag = 1
            else:
                flag = 0
                print("Invalid Format")
                return False
        else:
            flag = 0
            print("Name should contain only letters and not digit")
            return False
    if flag == 1:
        return True

def isempagevalid(age):
    if age.isdigit():
        a = int(age)
        if a > 0:
            return True
        else:
            print("Age cannot be 0!")
            return False
    else:
        print("Age must be in digit!")
        return False

def isempsalaryvalid(sal):
    if sal.isdigit():
        s=int(sal)
        if s > 0:
            return True
        else:
            print("Salary must be greater than zero")
            return False
    else:
        print("Salary should be in digit")
        return False

def isempgendervalid(g):
    l=['Male','Female','Other']
    if g in l:
        return True
    else:
        return False

def isempcityvalid(city):
    if city.isalpha():
        return True
    else:
        print("City name can't be in digit!")
        return False

def isempdobvalid(dob):
    dv = '^[0-9]{2}[-]{1}[0-9]{2}[-]{1}[0-9]{4}$'
    if re.match(dv, dob):
        try:
            if (bool(parser.parse(dob))):
                return True
        except ValueError:
            return False
    else:
        return False

def isempdojvalid(doj):
    dv = '^[0-9]{2}[-]{1}[0-9]{2}[-]{1}[0-9]{4}$'
    day = int(doj[0:2])
    month = int(doj[3:5])
    year = int(doj[7:])
    now = datetime.now()
    if re.match(dv, doj):
        try:
            if (bool(parser.parse(doj))):
                if year <= now.year and month <= now.month or day <= now.day:
                    return True
                else:
                    print("Date must be less than systems current date!")
                    return False
        except ValueError:
            return False
    else:
        return False

def isdeptvalid(dname):
    l=['IT','HR','FINANCE','SALES','MARKETING']
    if dname in l:
        return True
    else:
        print("Department must be from the below list!")
        print("IT\tHR\tMARKETING\tFINANCE\tSALES")
        return False

def ispanvalid(pan):
    validpan = '^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(validpan,pan):
        return True
    else:
        print("Format for pan is \nhint--ABCDE1234F")
        return False

def isaadharvalid(aadhar):
    if aadhar.isdigit() and len(aadhar) == 12:
        return True
    else:
        print("Aadhar must be 12 digit number")
        return False

def ismobvalid(mob):
    if mob.isalpha():
        print("Mobile number must be in digit!")
        return False
    elif mob.isdigit():
        if len(mob) == 10:
            return True
        else:
            print("Length of mobile number must be 10 digit!")
            return False