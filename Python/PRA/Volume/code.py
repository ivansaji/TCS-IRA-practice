class Container:
    def __init__(self,Id,length,breadth,height,status="Available"):
        self.Id = Id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.status = status
    
    def getVolume():
        self.volume = self.length*self.breadth*self.height
        return self.volume

class PackagingCompany:
    def __init__(self,containerList):
        self.containerList=containerList
        
    def findContainersToPack(self,obj_volume):
        for i in self.containerList:
            vol=i.getvolume()
            if(i.status.lower()=="available" && )
