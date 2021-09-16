class Magazine:
    def __init__(self, Author, Viewers, Cost, Name):
        self.Author = Author
        self.Viewers = Viewers
        self.Cost = Cost
        self.Name = Name


class publishingHouse:
    def __init__(self, magazineCollection):
        self.magazineCollection = magazineCollection

    def findMinimumMagazineByViewers(self):
        miniarray = []
        if len(self.magazineCollection) == 0:
            return None
        else:
            for vi in self.magazineCollection:
                miniarray.append(vi.Viewers)

            mini = min(miniarray)

            for vi1 in self.magazineCollection:
                if mini == vi1.Viewers:
                    return vi1

    def sortMagazineByCost(self):
        costarray = []
        if len(self.magazineCollection) == 0:
            return None
        else:
            for costs in self.magazineCollection:
                costarray.append(costs.Cost)
            costarray.sort()
            return costarray

#main
number = int(input())
collection = []

for i in range(number):
    Author = input()
    Viewers = int(input())
    Cost = float(input())
    Name = input()
    collection.append(Magazine(Author, Viewers, Cost, Name))

result = publishingHouse(collection)

ans = result.findMinimumMagazineByViewers()
ans1 = result.sortMagazineByCost()

if ans == ans1 == None:
    print("No Data Found")
else:
    print(ans.Author)
    print(ans.Viewers)
    print(ans.Cost)
    print(ans.Name)

    for i in ans1:
        print(i)