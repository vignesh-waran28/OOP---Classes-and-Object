from datetime import date

class cricketer:
    def __init__(self,name,jerseyno,debutYear,scores,city):
        self.name = name
        self.jerseyno = jerseyno
        self.debutYear = debutYear
        self.scores=scores
        self.city = city

    def currentScore(self):
        sco= f"Name: {self.name}\nJersey Number: {self.jerseyno}\nDebut Year: {self.debutYear}\nTotal Score: {self.scores}\nCity: {self.city}"
        return sco

    def yearsPlayed(self):
        currentYear= date.today().year
        return currentYear - self.debutYear

cric1=cricketer("Rahul",1,2012,4000,"Bangalore")
cric2=cricketer("virat",18,2000,10000,"Delhi")

print(cric1.name)
print(cric1.currentScore())
print(cric1.yearsPlayed())

print(cric2.name)
print(cric2.currentScore())
print(cric2.yearsPlayed())
