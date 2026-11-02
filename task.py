while True:  

    print("========= voting age =========")    

    a=input("enter age :")

    if a.isdigit():
        age=int(a)
        break
    else:
        print("invalid...")

if age>=18:
    print("eligible for voting...")

else:
    print("not eligible for voting...")