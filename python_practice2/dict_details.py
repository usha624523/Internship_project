d={1:["Abhi",21,"Bangalore","Engineer"],2:["Anvith",30,"Mangalore","Accountant"],
   3:["Bhavan",25,"Hubli","Manager"],4:["Chetan",23,"Bangalore","Business Head"]}
while True:
    n=int(input("\nEnter the EmployeeID : "))
    if n in d:
        print("\n----------------------------\nEmployee %d details are:-"%n)
        print("\tName  : ",d[n][0])
        print("\tAge   : ",d[n][1])
        print("\tPlace : ",d[n][2])
        print("\tWork  : ",d[n][3],"\n----------------------------")
    else:
        print("\n-------\nThe EmployeeID doesnot exist\n-----------------")
