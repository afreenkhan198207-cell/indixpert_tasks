student=[]

def add_data():
       name=input("enter name :-")
       id=input("enter id :-")
       course=input("enter course :-")
       n=int(input("how many qul :-"))
       
       for i in range(n):
            
         qul=input("enter qualification :-")

       data={
              "name":name,
              "id":id,
              "course":course
       }

       student.append(qul)
       student.append(data)

def show_data():
    for i in student:
        print("name:",["name"])
        print("id:",["id"])
        print("course :",["course"])
while True:
    print("1, add data")
    print("2, show data")
    print("3, exit")

    choice = int (input("enter choice :-"))

    if choice==1:
        add_data()

    elif choice==2:
        show_data()

    elif choice==3:
        print(exit)
        break

    else:
        print("invalid")
        break
         