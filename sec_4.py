#program_1 : test accessapilty of the employee
age=int(input("Enter your age"))  
driver_license =bool(input("do you have a license ?"))

if driver_license==True & age >21 :
    print ("You are accepted.")
else :
    print ("You are not accepted.")