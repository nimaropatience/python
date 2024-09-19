from datetime import datetime
print("This program calculates your age from your date of birth")
dd=int(input("What day were you born"))
mm=int(input("What month were you born ,enter the month number:"))
yyyy=int(input("What year were you born? Enter the full year: "))

today=datetime.today()
b1= dd,mm,yyyy
newdate1= datetime.timetuple(b1, "%d/%m/%Y")


age=today.year- b1.year-((today.month,today.day)<(b1.month,b1.day))
print(age)