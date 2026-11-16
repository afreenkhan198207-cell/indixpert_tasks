from indixpert_tasks.python.student_registration.signup.signup import Student
from indixpert_tasks.python.student_registration.signup.signup import Teacher


def menu():

    while True:

        print("\n===== REGISTRATION SYSTEM =====")
        print("1. Teacher Registration")
        print("2. Student Registration")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            obj = Teacher()
            obj.register()

        elif choice == 2:

            obj = Student()
            obj.register()

        elif choice == 3:

            print("Thank you!")
            break

        else:
            print("Invalid choice!")


menu()
