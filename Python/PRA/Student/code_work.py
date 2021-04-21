class Student:
    def __init__(self,roll_no,name,mark1,mark2,total_marks):
        self.roll_no = roll_no
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.total_marks = total_marks
    
    def updateStudentMarks(self,per_change):
        self.mark1 = self.mark1+((per_change/100)*self.mark1)
        self.mark2 = self.mark2-((per_change/100)*self.mark2)
        self.total_marks = self.mark1 + self.mark2
         
class School:
    def __init__(self,school_name,students_list):
        self.school_name = school_name
        self.students_list=students_list
        
    def calculateStudentMarksUpdation(self,percent,stu_roll):
        for i in self.students_list:
            if(i.roll_no==stu_roll):
                i.updateStudentMarks(percent)
                if percent==0:
                    print(i.name,i.mark1,i.mark2,i.total_marks)
                    return
                print(i.name,i.mark1,i.mark2,i.total_marks)
                return

#main
count = int(input())
pass_list=[]

for i in range(count):
    roll_no = int(input())
    name = input()
    mark1 = float(input())
    mark2 = float(input())
    total_marks = mark1+mark2
    pass_list.append(Student(roll_no,name,mark1,mark2,total_marks))

school_name="ABC"
obj_school=School(school_name,pass_list)

reqd_roll=int(input())
reqd_percent = float(input())

obj_school.calculateStudentMarksUpdation(reqd_percent,reqd_roll)
