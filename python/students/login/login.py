
def login(student):
    print("====== login ======")
    email = input("enter email :-")
    password = input("enter password :-")

    if email in student and student[email]["password"]in password:
        print("login successfully")
    else:
        print("try again")

        