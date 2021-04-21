class Employee:
    def __init__(self,employeeId,employeeName,status,ageInRole):
        self.employeeId=employeeId
        self.employeeName=employeeName
        self.status=status
        self.ageInRole=ageInRole

class Organization:
    def __init__(self,employeeList):
        self.employeeList=employeeList
    
    def updateEmployeeStatus(self,noOfYears):
        for i in self.employeeList:
            if(i.ageInRole>noOfYears):
                i.status="Retirement Due"
    
    def countEmployees(self):
        count = 0
        for i in self.employeeList:
            if(i.status.lower()=="retirement due"):
                count+=1
        return count
    

#main Program
count = int(input())
pass_list=[]

for i in range(count):
    Id = int(input())
    employeeName=input()
    status="Available"
    ageInRole=int(input())
    pass_list.append(Employee(Id,employeeName,status,ageInRole))
    
obj = Organization(pass_list)

no_of_yrs=int(input())
obj.updateEmployeeStatus(no_of_yrs)

update=obj.countEmployees()

if update==0:
    print("No employees updated")
else:
    print("count of employee updated {0}".format(update))
    
for i in pass_list:
    print(i.employeeId,i.employeeName,i.status)

