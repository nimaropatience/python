def MainMenu():
    print("MTN")
    print("1. Send money")
    print("2. Airtime&Bundles")
    print("3. Pay with Momo")
    print("4. Payments")
    print("5. Savings&loans")
    print("6. Financial services")
    print("7. Insurance")
    print("8. Account")
    while True:
        try:
            selection=int(input("Enter choice:"))
            if selection==1:
                a()
                break
            elif selection==2:
                b()
                break
            elif selection==3:
                c()
                break
            elif selection==4:
                d()
                break
            elif selection==5:
                e()
                break
            elif selection==6:
                f()
                break
            elif selection==7:
                g()
                break
            elif selection==8:
                h()
            else:
                print ("Invalid choice.Enter 1-8")
                MainMenu()

def a():
    print("1.Airtel number") 
    print("2.MTN number")  
    print("3.UTL number")
    print("4.International Transfer")  
    print("5.My Transaction Reversals") 
    print("6.Wendi wallet") 
    print("0.Back 00.Main Menu")  

def b():
    print("1.Airtime")   
    print("2.Voice Bundles") 
    print("3.Internet bundles")
    print("4.Freedom bundles")
    print("5.Special Bundles")
    print("6.WakaNet")
    print("7.SMS Bundles")
    print("0.Back")
    print("00.Next")








                
                        
    
    
        
    
\