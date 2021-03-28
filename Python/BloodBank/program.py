#class section
class Donor:
    def _init_(self,id,n,num,grp,prev_mnth_dnt,dist):
        self.id = id
        self.dnrname = n
        self.number = num
        self.group = grp
        self.PrevDonatedMon = prev_mnth_dnt[0:2]
        self.AwayFrom = dist

class BloodBank:
    def _init_(self,name,dnrlst):
        self.bank_name = name
        self.listOfDonors = dnrlst
    
    def getListofAvailableDonors(self):
        l=[]
        d={}
        mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        no_mon='Dec'

        for i in self.listOfDonors:
            l.append(i.group)
        l=sorted(list(l))

        for i in range(len(l)):
            d[l[i]]=0

        for i in self.listOfDonors:
            pmon = i.PrevDonatedMon
            k1=mon.index(pmon)
            k2=mon.index(no_mon)
            if(k2-k1>=4 and i.AwayFrom<=50):
                d[i.bloodGroup]=d[i.bloodGroup]+1
        return d
    
    def getAndUpdateDonor(self,g,c):
        res = self.getListofAvailableDonors()
        for i in res:
            if(i==g):
                if(res[i]<c):
                    z=False
                    #This shows that reguired donor is less than available(return false)
                    #now available gives blood, so their donated month is updated with present month
                    mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                    no_mon='Dec'
                    for j in range(res[i]):
                        for k in self.listOfDonors:
                            if(k.group==g):
                                pmon=k.PrevDonatedMon
                                k1=mon.index(pmon)
                                k2=mon.index(no_mon)
                                if(k2-k1>4 and k.AwayFrom<=50):
                                    k.PrevDonatedMon=no_mon

                elif(res[i]>=cbg):
					z=True
                    #This shows that reguired donor is more than available(return true)
                    #now available gives blood, so their donated month is updated with present month
					mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
					cmon='Dec'
					for j in range(cbg):
						for k in self.ListOfDoners:
							if(k.Bloodgroup==group):
								pmon=k.PrevDonatedMon
								k1=mon.index(pmon)
								k2=mon.index(cmon)
								if(k2-k1>=4 and k.AwayFrom<=50):
									k.PrevDonatedMon=cmon
	return z



#main
if "__name__" == "__main__":
    l=[]
    count = int(input())
    for i in range(count):
        iD = int(input())
        Name = input()
        Contact = int(input()[:10])
        bloodGroup = input()
        lastdonatedMonth = input().[:2]
        dist_away=int(input())
    
        l.append(Donor(iD,Name,Contact,bloodGroup,lastdonatedMonth,dist_away))
    
    B=BloodBank("Suni",l)

    group = input()
    dcount = int(input())

    res1=B.getListofAvailableDonors()

    for i in res1:
        print(i," ",res1[i])
    
    res2=B.getAndUpdateDonor(group,dcount)

    if(res2):
        print("Donor count available")
    else:
        print("Donor count not available")

    res3 = B.getListofAvailableDonors()
    for i in res3:
        print(i," ",res3[i]) 