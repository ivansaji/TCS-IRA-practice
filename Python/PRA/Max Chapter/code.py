class Chapter:
    def __init__(self,Subject,Name,Pages,Marks):
        self.Subject=Subject
        self.Name=Name
        self.Pages=Pages
        self.Marks=Marks
        
class Exam:
    def __init__(self,examName,chapterList):
        self.examName=examName
        self.chapterList=chapterList
    
    def findMaximumChapterByPage(self):
        max_page=0
        for i in self.chapterList:
            if(i.Pages>max_page):
                max_page=i.Pages
                max_chapter=i
        
        if (len(self.chapterList)==0):
            return None
        else:
            return max_chapter
        
    def sortChapterByMarks(self):
        l=[]
        for i in self.chapterList:
            l.append(int(i.Marks))
        
        l.sort()
            
        if(len(l)==0):
            return None
        else:
            return l

#main
count = int(input())
pass_list=[]

for i in range(count):
    sub=input()
    pages=int(input())
    marks=int(input())
    name=input()
    pass_list.append(Chapter(sub,name,pages,marks))

obj=Exam("ABC",pass_list)

res1=obj.findMaximumChapterByPage()

if(res1==None):
    print("No Data Found")
else:
    print(res1.Subject)
    print(res1.Pages)
    print(res1.Marks)
    print(res1.Name)
            
res2 = obj.sortChapterByMarks()
if(res2==None):
    print("No Data Found")
else:
    for i in res2:
        print(i)
            
