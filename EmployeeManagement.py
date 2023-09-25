from validations import *
def accept():
    global id,name,age,sal,g,city,add,mob,dob,doj,pan,aadhar,designation,dname
    print("Enter Employee details -> \n")

    while True:

        id = input("Enter Employee id -> ")
        if isempidvalid(id):
            flag = 1
            for i in emplist:
                if id == i.id:
                    flag = 0
                    print("Employee with the given id already exist!")
            if flag == 1:
                break
        else:
            print("Enter id in valid format!")


    while True:

        name = input("Enter Employee name -> ")
        if isnamevalid(name):
            break
        else:
            print("hint-- Firstname Middlename Lastname!")

    while True:
        mob = input("Enter Mobile Number -> ")
        if ismobvalid(mob):
            flag = 1
            for i in emplist:
                if mob == i.mob:
                    flag = 0
                    print("Employee with the given mobile number already exist!")
            if flag == 1:
                break
        else:
            print("Invalid Mobile Number!")

    while True:
        sal = input("Enter Employee Salary -> ")
        if isempsalaryvalid(sal):
            break
        else:
            print("Invalid Salary")


    while True:
        age = input("Enter Employee Age -> ")
        if isempagevalid(age):
            break
        else:
            print("Invalid Age")

    while True:
        g = input("Enter Gender -> ")
        if isempgendervalid(g):
            break
        else:
            print("Enter valid gender!")
            print("hint-- Male | Female | Other")

    add = input("Enter Employee Address -> ")
    while True:
        city = input("Enter Employee city -> ")
        if isempcityvalid(city):
            break
        else:
            print("Invalid City name!")

    while True:
        dob = input("Enter Date of Birth -> \nFormat -> dd-mm-yyyy")
        if isempdobvalid(dob):
            break
        else:
            print("Invalid Format")
    while True:
        doj = input("Enter Date of Joining -> \nFormat -> dd-mm-yyyy")
        if isempdojvalid(doj):
            break
        else:
            print("Invalid Format")

    while True:
        dname = input("Enter Department name -> ")
        if isdeptvalid(dname):
            break
        else:
            print("Invalid Department")

    while True:
        designation = input("Enter Employee Designation -> ")
        if isnamevalid(designation):
            break
        else:
            print("Invalid Format")

    while True:
        pan = input("Enter Pan Number -> ")
        if ispanvalid(pan):
            flag = 1
            for i in emplist:
                if pan == i.pan:
                    flag = 0
                    print("Employee with the given PAN number already exist!")
            if flag == 1:
                break
        else:
            print("Invalid Format!")


    while True:
        aadhar = input("Enter Aadhar Number -> ")
        if isaadharvalid(aadhar):
            flag = 1
            for i in emplist:
                if aadhar == i.aadhar:
                    flag = 0
                    print("Employee with the given Aadhar Number already exist!")
            if flag == 1:
                break
        else:
            print("Invalid Format!")


class Employee:
    dept = {}
    emp = []
    def __init__(self,id,name,mob,sal,age,g,add,city,dob,doj,dname,designation,pan,aadhar):

        self.id = id
        self.name = name
        self.sal = sal
        self.mob = mob
        self.age = age
        self.g = g
        self.add = add
        self.city = city
        self.dob = dob
        self.doj = doj
        self.dname = dname
        self.designation = designation
        self.pan = pan
        self.aadhar = aadhar

        if dname not in self.dept.keys():
            self.dept[self.dname] = [self.id]
        else:
            self.dept[self.dname].append(self.id)

        if self not in self.emp:
            self.emp.append(self)


    def DisplayDetails(self):

        print("\n\nEmployee Personal Details -> ")
        print("|   id    | Name | MobileNumber | Salary | Age | DOB | DOJ | Address | City | Gender |")
        print("| ",self.id," | ",self.name," | ",self.mob," | ",self.sal," | ",self.age," | ",self.dob," | ",self.doj," | ",self.add," | ",self.city," | ",self.g)
        print("\nEmployee Department Details -> ")
        print("|    Department-Name    |  Designation    |  ")
        print(" | ",self.dname," | ",self.designation ," | ")

    def updatesalbyid(self):
        amt = int(input("Enter percentage amount to increase salary -> "))
        s = float(self.sal)
        s = s + (s * amt / 100)
        self.sal = str(s)

    @classmethod
    def updatesalbydept(self,d):
        for k,v in self.dept.items():
            #print(v)
            if k == d:
                amt = int(input("Enter percentage amount to increase salary -> "))
                for j in emplist:
                    for i in v:
                        if j.id == i:
                            s = float(j.sal)
                            s = s + (s * amt / 100)
                            j.sal = str(s)
                print("Updated Successfully")

    def updatesalary(self,amt):
        a = amt
        s = float(self.sal)
        s = s + (s * a / 100)
        self.sal = str(s)

    def updatename(self):
        while True:
            nm = input("Enter New Employee name to update-> ")
            if isnamevalid(name):
                self.name=nm
                break
            else:
                print("hint-- Firstname Middlename Lastname!")

    def updateaddress(self):
        na = input("Enter new address to update -> ")
        self.add = na

    def updatedob(self):
        while True:
            ndob = input("Enter Date of Joining -> \nFormat -> dd-mm-yyyy")
            if isempdojvalid(ndob):
                self.dob = ndob
                break
            else:
                print("Invalid Format")
    @classmethod
    def DisplayHighestSalary(cls):
        m=0
        for i in emplist:
            n = float(i.sal)
            if n > m:
                m = n
        for i in emplist:
            n = float(i.sal)
            if n == m:
                i.DisplayDetails()
    @classmethod
    def DisplayLowestSalary(cls):
        m=99999999
        for i in emplist:
            n = float(i.sal)
            if n < m:
                m = n
        for i in emplist:
            n = float(i.sal)
            if n == m:
                i.DisplayDetails()
    def deleterecord(self,empid):
        for i in emplist:
            if i.id == self.id:
                emplist.remove(self)
                print("Record Delete Successfully!")
                break

        for k,v in self.dept.items():
            for j in v:
                if j == empid:
                    v.remove(empid)
                    break

emplist = []
while True:
    print("|-----------------------MENU---------------------------|")
    print("| 1. Add record of employee ->                         |")
    print("| 2. Display Employee details ->                       |")
    print("| 3. Update Employee details ->                        |")
    print("| 4. Delete Employee details ->                        |")
    print("| 5. Search Employee details ->                        |")
    print("| 6. Display Employee details with highest salary ->   |")
    print("| 7. Display Employee details with lowest salary ->    |")
    print("| 8. Exit                                              |")
    print("|------------------------------------------------------|")
    ch = int(input("\nEnter your choice -> "))
    if ch == 1:
        accept()
        emp = Employee(id,name,mob,sal,age,g,add,city,dob,doj,dname,designation,pan,aadhar)
        emplist.append(emp)
    elif ch == 2:
        print("Details of All Employees -> ")
        for i in emplist:
            i.DisplayDetails()
    elif ch == 3:
        while True:
            print("|---------------MENU-------------|")
            print("| A -> UPDATE EMPLOYEE NAME      |")
            print("| B -> UPDATE EMPLOYEE ADDRESS   |")
            print("| C -> UPDATE EMPLOYEE DOB       |")
            print("| D -> UPDATE EMPLOYEE SALARY    |")
            print("|--------------------------------|")
            c = input("\nEnter your choice -> ")
            if c == 'D':
                while True:
                    print("|--------------------------MENU---------------------------|")
                    print("| 1. UPDATE SALARY BY EMPLOYEE ID                         |")
                    print("| 2. UPDATE SALARY OF ALL EMPLOYEE IN SPECIFIC DEPARTMENT |")
                    print("| 3. UPDATE SALARY OF ALL EMPLOYESS                       |")
                    print("|---------------------------------------------------------|")
                    choice = int(input("Enter your choice -> "))
                    if choice == 1:
                        empid = input("Enter employee id to update its salary -> ")

                        for i in emplist:
                            flag = True
                            if i.id == empid:
                                i.updatesalbyid()
                                print("Updated Successfully")
                                i.DisplayDetails()
                                break
                            else:
                                flag = False

                        if flag == False:
                            print("Employee record not found for given id")
                            break
                        else:
                            break
                    elif choice == 2:
                        d = input("Enter Department name to update salary -> ")
                        if d in Employee.dept.keys():
                            Employee.updatesalbydept(d)
                            break
                        else:
                            print("Department not found!")
                            break
                    elif choice == 3:
                        amt = int(input("Enter percentage amount to increase salary of all employees -> "))
                        for i in emplist:
                            i.updatesalary(amt)
                        print("Updated Successfully!")
                        break
                    else:
                        print("Enter Valid Choice!")

                break
            elif c == 'A':
                empid = input("Enter Employee Id to Update its name -> ")
                for i in emplist:
                    flag = True
                    if i.id == empid:
                        i.updatename()
                        print("Updated Succesfully!")
                        i.DisplayDetails()
                        break
                    else:
                        flag = False
                if flag == False:
                    print("Employee record not found for given id")
                    break
                else:
                    break
            elif c == 'B':
                empid = input("Enter Employee Id to Update its Address -> ")
                for i in emplist:
                    flag = True
                    if i.id == empid:
                        i.updateaddress()
                        print("Updated Succesfully!")
                        i.DisplayDetails()
                        break
                    else:
                        flag = False
                if flag == False:
                    print("Employee record not found for given id")
                    break
                else:
                    break
            elif c == 'C':
                empid = input("Enter Employee Id to Update its DOB -> ")
                for i in emplist:
                    flag = True
                    if i.id == empid:
                        i.updatedob()
                        print("Updated Succesfully!")
                        i.DisplayDetails()
                        break
                    else:
                        flag = False
                if flag == False:
                    print("Employee record not found for given id")
                    break
                else:
                    break
            else:
                print("Enter valid choice!")
    elif ch == 4:
        empid = input("Enter employee id to delete its record -> ")
        for i in emplist:
            flag = True
            if i.id == empid:
                i.deleterecord(empid)
            else:
                flag = False

        if flag == False:
            print("Record not found for given Employee id!")

    elif ch == 5:
        while True:
            print("|------------------MENU----------------|")
            print("| A -> SEARCH BY EMPLOYEE ID           |")
            print("| B -> SEARCH BY EMPLOYEE NAME         |")
            print("| C -> SEARCH BY DEPARTMENT NAME       |")
            print("|--------------------------------------|")
            c = input("Enter your choice -> ")
            if c == 'A':
                empid = input("Enter employee id to search -> ")
                for i in emplist:
                    flag = True
                    if i.id == empid:
                        i.DisplayDetails()
                    else:
                        flag = False
                if flag == False:
                    print("Record not found!")
                break
            elif c == 'B':
                ename = input("Enter employee name to search -> ")
                for i in emplist:
                    flag = True
                    if i.name == ename:
                        i.DisplayDetails()
                    else:
                        flag = False
                if flag == False:
                    print("Record not found")
                break
            elif c == 'C':
                d = input("Enter Department name to search -> ")
                # if d not in Employee.dept.keys():
                #     print("Department not found")
                #     break
                for k,v in Employee.dept.items():
                    flag = True
                    if d == k:
                        print("Details of Employee in Department -> ",d)
                        for i in emplist:
                            for j in v:
                                if i.id == j:
                                    i.DisplayDetails()
                    else:
                        flag = False
                if flag == False:
                    print("Department not found")
                break
            else:
                print("Enter valid choice!")

    elif ch == 6:
        Employee.DisplayHighestSalary()
    elif ch == 7:
        Employee.DisplayLowestSalary()
    elif ch == 8:
        exit(0)
    else:
        print("Enter valid choice!")
