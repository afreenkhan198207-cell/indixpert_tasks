# name="afreen"
# age=19
# address="tow<=n choki"


# print(f"my name is {name} my age is {}")


name=input("enter student's name :-")
roll_number=int(input("enter roll number :-"))
    # marks=float(input("enter marks :-"))

    # print (f"{name}\n{roll_number}\n" )
while True:

    bio=float(input("enter bio marks :-"))
    if bio >=1 and bio<=100:
        break
    else:
        print("invalid")
while True:

    phy=float(input("enter phy marks :-"))
    if phy >=1 and phy <=100:
        break
    else:
        print("invalid")

while True:

    chem=float(input("enter chem marks :-"))
    if chem>=1 and chem<=100:
        break
    else:
        print("invalid")

while True:

    eng=float(input("enter english marks :-"))
    if eng>=1 and eng <=100:
        break
    else:
        print("invalid")

while True:

    hindi=float(input("enter hindi marks :-"))
    if hindi>=1 and hindi<=100:
        break
    else:
        print("invalid")

total=bio+phy+chem+eng+hindi

percentage = (total/500)*100

print(percentage)


