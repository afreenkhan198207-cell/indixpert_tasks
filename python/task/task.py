student1={
    "name":"afreen",
    "id":"112",
    "course":"ba",
    "email":"afreen@gmail.com",
    "password":"1234"
}
student2={
    "name":"arshil",
    "id":"113",
    "course":"btech",
    "email":"arshil@gmail.com",
    "password":"1222"
}
student3={
    "name":"priya",
    "id":"114",
    "course":"bca",
    "email":"priya@gmail.com",
    "password":"1233"
}


def login():
    email = input("enter email :-")
    password = input("enter password :-")

    if student1["password"] == password and student1["email"] == email:
        print("login successfully")
        print(student1)
    elif student2["password"] == password and student2["email"] == email:
        print("login successfully")
        print(student2)
    elif student3["password"] == password and student3["email"] == email:
        print("login successfully")
        print(student3)
    else:
        print("invalid")
