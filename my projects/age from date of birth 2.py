from datetime import datetime
now=datetime.now()
year=now.strftime("%Y")
month=now.strftime("%m")

byear=int(input("enter the birth year"))
bmonth=int(input("enter the birth month in number"))
year=int(year)
month=int(month)
if(byear<year):
    if(bmonth<month):
        x = year - byear
        y = month -bmonth
        print(f"your age is{x} and {y}month")
    else:
        x = (year-byear)-1
        y = 12-(bmonth-month)
        print(f"your age is{x} and {y} month")
    
    
     

