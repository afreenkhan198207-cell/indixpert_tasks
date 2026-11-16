student=[]
n=int(input("enter the number of student :"))
i=0
while i < n:
    name=input("enter name  :")
    age=int(input("enter age  :"))
    course=input("enter course  :")
    
    student.append({
        "name":name,
        "age" :age,
        "course" :[]
    })
    i += 1

    print("\n--- all student details ---")
    for student in  range(len(student)):
     print(f"\nname :{student["name"]}"),
     print(f"\nage : {student["age"]}"),
     print(f"\ncoursse: {student["course"]}")