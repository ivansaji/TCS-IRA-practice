class Container:
    def __init__(self,Id,length,breadth,height,status):
        self.Id = Id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.status = status
    
    def getVolume(self):
        self.volume = self.length*self.breadth*self.height
        return self.volume

class PackagingCompany:
    def __init__(self,containerList):
        self.containerList=containerList
        
    def findContainersToPack(self,obj_volume):
        for i in self.containerList:
            avail_vol=i.getVolume()
            if(i.status.lower()=="available" and avail_vol>=obj_volume):
                i.status="Used"
        return self.containerList
#main func
count = int(input())
pass_list=[]

for i in range(count):
    Id = int(input())
    length=int(input())
    breadth=int(input())
    height=int(input())
    status="Available"
    pass_list.append(Container(Id,length,breadth,height,status))

obj=PackagingCompany(pass_list)

obj_vol=int(input())

result=obj.findContainersToPack(obj_vol)

for i in result:
    print(i.Id,i.length*i.breadth*i.height,i.status)
