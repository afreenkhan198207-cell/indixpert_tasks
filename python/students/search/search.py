
def search(student):
    print("============== search ===============")
    email=input("enter email for searching... :-")

    if email in student:

        student
        print("name",student[email]["name"])
        print("student_id",student[email]["student_id"])
        print("course",student[email]["course"])
        print("email",student[email]["email"])
        print("password",student[email]["password"])

    else:
        print("not found...")
