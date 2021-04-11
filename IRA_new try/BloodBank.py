class Donor:
    def __init__(self,Id,Name,Contact,Bloodgroup,PrevDonatedMon,AwayFrom):
        self.Id=Id
        self.Name=Name
        self.Contact=Contact
        self.Bloodgroup=Bloodgroup
        self.PrevDonatedMon=PrevDonatedMon
        self.AwayFrom = AwayFrom

class BloodBank:
    def __init__(self,BankName,ListOfDonors):
        self.BankName=BankName
        self.ListOfDonors=ListOfDonors

    def getListofAvailableDonors(self):
        l=[]
        d={}
        mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        cmon='Dec'

        #creating list of blood groups
        for i in self.ListOfDonors:
            l.append(i.Bloodgroup)
        
        #creating a list of groups
        l=sorted(set(l))

        # setting 0 count for all groups
        for i in range(len(l)):
            d[l[i]]=0
        
        for i in self.ListOfDonors:
            pmon = i.PrevDonatedMon
            k1 = mon.index(pmon)
            k2 = mon.index(cmon)

            if(k2-k1>=4 and i.AwayFrom<=50):
                d[i.Bloodgroup]=d[i.Bloodgroup]+1
        return d
    
    def getAndUpdateDonor(self,reqd_grp,reqd_count):
        #Update
        res = self.getListofAvailableDonors()
        for i in res:
            if(i==reqd_grp):
                if(res[i]<reqd_count):
                    flag = False
                    mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                    cmon='Dec'
                    for j in range(res[i]):
                        for k in self.ListOfDonors:
                            if(k.Bloodgroup==reqd_grp):
                                pmon=k.PrevDonatedMon
                                k1 = mon.index(pmon)
                                k2 = mon.index(cmon)
                                if(k2-k1>=4 and k.AwayFrom<=50):
                                    k.PrevDonatedMon=cmon
                elif(res[i]>=reqd_count):
                    flag = True
                    mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                    cmon='Dec'
                    for j in range(reqd_count):
                        for k in self.ListOfDonors:
                            if(k.Bloodgroup==reqd_grp):
                                pmon=k.PrevDonatedMon
                                k1 = mon.index(pmon)
                                k2 = mon.index(cmon)
                                if(k2-k1>=4 and k.AwayFrom<=50):
                                    k.PrevDonatedMon=cmon
        return flag



#main
pass_list=[]
n=int(input())
for i in range(n):
    Id = int(input())
    Name = input()
    Contact = int(input())
    Bloodgroup = input()
    PrevDonatedMon = input()
    AwayFrom = int(input())

    pass_list.append(Donor(Id,Name,Contact,Bloodgroup,PrevDonatedMon,AwayFrom))

bankobj = BloodBank("Bank",pass_list)

#Display Sorted list
dnr_dictionary = bankobj.getListofAvailableDonors()
for grp,cnt in dnr_dictionary.items():
    print(grp," ",cnt)

#accepting reqd groups
reqd_grp = input()
reqd_count = int(input())

#passing reqd to class function
avail = bankobj.getAndUpdateDonor(reqd_grp,reqd_count)
if avail == True:
    print("Donor count available")
elif avail == False:
    print("Donor count not available")

#Display Sorted list
dnr_dictionary = bankobj.getListofAvailableDonors()
for grp,cnt in dnr_dictionary.items():
    print(grp," ",cnt)
