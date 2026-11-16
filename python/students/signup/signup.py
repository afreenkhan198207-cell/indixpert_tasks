
import datetime
def signup(student):

    print("=========== signup ============")

    name = input("enter name :-")
    student_id = input("enter id :-")
    course = input("enter course :-")
    email = input("enter email :-")
    password = input("enter password :-")
    num=int(input("how many qualification :-"))
    for i in range(num):
    
        qul=input("enter qualification :-")

    if email in student:
        print("email is already registered")

    print("====================== signup successfully ======================")
    date=datetime.datetime.now()
    print(date)
    student[email]={
        "name":name,
        "student_id":student_id,
        "qul":qul,
        "course":course,
        "email":email,
        "password":password
    }
    
def validationn():

    

    if "@" in "email" :
        print("save email ...........")

    else:
        print("email is invalid")

    if "password"<='8':
        print("save password successfully...")
    else:
        print("password is invalid")
