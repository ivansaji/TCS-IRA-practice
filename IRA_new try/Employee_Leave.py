class Employee:
    def __init__(self,employee_name,designation,salary,leaveBalance):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.leaveBalance = leaveBalance

class Organization:
    def __init__(self,employee_list):
        self.employee_list = employee_list
    
    def display_leaves(self,name):
        for i in self.employee_list:
            if i.name == name:
                for a,b in i.leaveBalance.items():
                    print(a,":",b)
    
    def checkLeaveEligibility(self,emp_name,leave_type,no_days_reqd):
        #for name present in list
        for i in self.employee_list:
            if i.employee_name == emp_name:
                #Condition 1 satisfied - name present
                for a,b in i.leaveBalance.items():
                    if a==leave_type:
                        if b>=no_days_reqd:
                            i.leaveBalance[a]=b-no_days_reqd
                            return 'True'
                        else:
                            return 'False'
            else:
                return 'not found'

# main program

l=[]
count = int(input())
for i in range(count):
    leaves = {}
    employee_name = input()
    designation = input()
    salary = int(input())
    no_of_leave_type = int(input())
    for i in range(no_of_leave_type):
        key = input().upper()
        value = int(input())
        leaves[key]=value
    l.append(Employee(employee_name,designation,salary,leaves))
    
o = Organization(l)

employee_name = input()
leave_type = input().upper()
no_days_reqd = int(input())

if(o.checkLeaveEligibility(employee_name,leave_type,no_days_reqd) == 'True'):
    print("leave granted")
    o.display_leaves(employee_name)
elif(o.checkLeaveEligibility(employee_name,leave_type,no_days_reqd) == 'False'):
    print("leave not granted")
    o.display_leaves(employee_name)
elif(o.checkLeaveEligibility(employee_name,leave_type,no_days_reqd) == 'not found'):
    print("leave not granted")
    print("employee not found")