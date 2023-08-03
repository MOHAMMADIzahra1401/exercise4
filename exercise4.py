name=input("Enter student's name :")
lastname=input("Enter student's last name:")

scor1=float(input("Enter scor1 in range 0 ta 20:"))
scor2=float(input("Enter scor2 in range 0 ta 20 :"))
scor3=float(input("Enter scor3 in range 0 ta 20 :"))

if scor1<0 or scor1>20:
     print("pleas enter a number in range 0 ta 20:") 
elif scor2<0 or scor2>20:
     print("pleas enter a number in range 0 ta 20:") 
elif scor3<0 or scor3>20:
    print("pleas enter a number in range 0 ta 20:") 
else:
    Average= (scor2+scor2+scor3)/3
    print(Average)
    if Average>=17 :
        print("Average" ,name,lastname," is  Greate")
    elif Average<17 and Average>=12 :
        print("Average" ,name,lastname, " is Normal")
    elif Average<12 :
        print("Average" ,name,lastname," is Fail")
    


