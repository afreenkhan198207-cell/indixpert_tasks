
# while True:

#     num=input("enter number :-")
#     if  num.isdigit():
#         num2 = int(num)
#         for i in range(1,11):
#             print(i*num2)
#         break
#     else:
#         print("invalid")


while True:
    num=input("enter number :-")
    if num.isdigit():
        num2=int(num)
        if num2 >=1 and num2<=100:
         for i in range(1,11):
            print(i*num2)
        else:
           print("invalid number")
    else:
        print("invalid")