#program_1 : test accessapilty of the employee and have a recommendation
age=int(input("Enter your age"))  
driver_license =bool(input("do you have a license ?"))
recommendation =bool(input("do you have a recommendation ?"))
if recommendation == False:
    if driver_license==True & age >21 :
        print ("You are accepted.")
    else :
        print ("You are not accepted.")
else:
    print ("You are accepted.")
