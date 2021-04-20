class Person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

class Society:
    def __init__(self,personList):
        self.personList=personList
        
    def findAverageheight(self):
        l=[]
        for i in self.personList:
            l.append(i.height)
        
        return sum(l)/len(l)
    
    def findTallerThanAgeragePerson(self):
        more_height_list=[]
        avg = self.findAverageheight()
        
        for i in self.personList:
            if i.height > avg:
                more_height_list.append(i.name)
        
        return more_height_list

# Main program
n = int(input())
pass_list=[]

for i in range(n):
    name=input()
    height=int(input())
    weight=int(input())
    pass_list.append(Person(name,height,weight))

obj = Society(pass_list)

print("The Average height is" + str(obj.findAverageheight()))
result = obj.findTallerThanAgeragePerson()

if len(result)==0:
    print("No one with more height")
else:
    for j in result:
        print(j)
