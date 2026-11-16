from abc import ABC, abstractmethod
import json
import os
import datetime
path=r"C:\Users\AFREEN\Desktop\indixpert.tasks\student_registration\student_data\student.json"
path1=r"C:\Users\AFREEN\Desktop\indixpert.tasks\student_registration\teacher_data\teacher.json"
path2=r"C:\Users\AFREEN\Desktop\indixpert.tasks\student_registration\error\error.json"
student=os.path.join(path)
teacher=os.path.join(path1)
error=os.path.join(path2)

class Registration(ABC):

    @abstractmethod
    def register(self):
        self.date=datetime.datetime.now()
        pass

    def save_data(self, data,filename):

        if os.path.exists(filename):
            with open(filename, "r") as file:
                records = json.load(file)
        else:
            records = []

        records.append(data)

        with open(filename, "w") as file:
            json.dump(records, file, indent=4)

        print("Registration successful!")



class Teacher(Registration):

    def register(self):

        print("\n===== TEACHER REGISTRATION =====")

        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        subject = input("Enter subject: ")
        experience = input("Enter experience: ")

        data = {
            "name": name,
            "email": email,
            "password": password,
            "subject": subject,
            "experience": experience
        }

        self.save_data(data, teacher)



class Student(Registration):

    def register(self):

        print("\n===== STUDENT REGISTRATION =====")

        while True:
            name = input("Enter name: ")
            if len(name)>2:
                break
            else:
                print("invalid name")
                with open (error,"a") as file:
                    file.write(f"[str{self.date}] [error] {name}")
        while True:
            email = input("Enter email: ")
            if "@" in email and email.endswith(".com"):
                break
            else:
                print("invalid email")
                with open (error,"a") as file:
                    file.write(f"[str{self.date}] [error] {email}")
        while True:
            password = input("Enter password: ")
            if len(password)>=6 and password.isalnum():
                break
            else:
                print("invalid password")
                with open (error,"a") as file:
                    file.write(f"[str{self.date}] [error] {password}")
        course = input("Enter course: ")
        while True:
            a = input("Enter age: ")
            if a.isdigit():
                age=int(a)
                break
            else:
                print("invalid age")
                with open (error,"a") as file:
                    file.write(f"[str{self.date}] [error] {a}")
        data = {
            "name": name,
            "email": email,
            "password": password,
            "course": course,
            "age": age
        }

        self.save_data(data, student)

