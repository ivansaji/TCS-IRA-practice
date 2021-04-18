class Research:
    def __init__(self,research_id,research_topic,research_author,research_cost,research_department):
        self.research_id=research_id
        self.research_topic=research_topic
        self.research_author=research_author
        self.research_cost=research_cost
        self.research_department=research_department

class University:
    def __init__(self,univ_name,res_list):
        self.univ_name = univ_name
        self.res_list = res_list
    
    def get_maxResearchDepart(self):
        d={}
        dept_list = []
        #creating List
        for i in self.res_list:
            dept_list.append(i.research_department)
        #converting list to dict with count
        for i in dept_list:
            d[i] = dept_list.count(i)
        #finding key with max value
        max_research_dept = max(d,key=d.get)
        return max_research_dept
    
    def get_researchByTopic(self,topic):
        result_list = []
        for i in self.res_list:
            if(i.research_topic == topic):
                result_list.append(Research(i.research_id,i.research_topic,i.research_author,i.research_cost,i.research_department))
        
        if len(l)==0:
            return('None')
        else:
            return(l)
    
# main program
count = int(input())
pass_list=[]
for i in range(count):
    research_id=int(input())
    research_topic = input()
    research_author = input()
    research_cost = int(input())
    research_department = input()
    pass_list.append(Research((research_id,research_topic,research_author,research_cost,research_department))
    
topic = input()
uname="suni"
univ=University(uname,pass_list)

k=univ.get_maxResearchDepart()
result = univ.get_researchByTopic(topic)
if k=='None':
    print("No researches on given topic")
else:
    for i in result:
        print(i.research_id,i.research_cost,i.research_department)