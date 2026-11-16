list=[]
def calculator_add():

    a = int(input("enter first value :"))
    b = int(input("enter second value :"))

    print("addiction +")
    print("substrictuion -")
    print("multiplication *")
    print("division /")

    choice = input("enter choice :")

    if choice == "+": # calculator with conditional opretor.
        print(a+b)
    elif choice =="-":
        print(a-b)
    elif choice =="*":
        print(a*b)                
    elif choice =="/":
        print(a/b)
    else:
        print("invalid")

