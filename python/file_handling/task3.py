
def menu_add():
    data = {}

    while True:
        print("1 : signup")
        print("2 : login")
        print("3 : exit")
        ch = int(input("enter choice :-"))

        if ch == 1:
            name = input("enter name :-")
            student_id = int(input("enter id :-"))
            email = input("enter email :-")
            password = input("enter password :-")
            con_password = input("enter conform password :-")

            if "@" not in email or "." not in email:
                print("email is not valid")
            if con_password != password:
                print("password is not valid")
            else:
                print("invalid data")

            data["name"] = name
            data["id"] = student_id
            data["email"] = email
            data["password"] = password
            data["con_password"] = con_password

            return
        elif ch == 2:
            email = input("enter email :-")
            password = input("enter password :-")
        elif ch == 3:
            break
        else:
            print("invalid data")
