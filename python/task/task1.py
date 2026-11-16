# #------------ student dashboard --------------

# student=[]
# while True:

#     print("1 : signin ...")
#     print("2 : login ...")
#     print("3 : show ...")

#     choice=int(input("enter choice :-"))


#     if choice==1:

#       signin={
#       'id':input("enter id :-"),
#       'email':input("enter email :-"),
#       'password':input("enter password :-"),
#       'classs':input("enter class :-"),
#       'rank':input("enter rank :-")
#       }
#     elif choice==2:

#      login={
#       'email':input("enter email :-"),
#       'password':input("enter password :-")
#     }
#     elif signin==login:
#          print(signin)
#     elif choice==3:
#       break

#     else:
#       print("invalid")
   
def menu_add():

 student={}
 while True :

    print("-------- student data ---------")
    print("1 : signin ....")
    print("2 : login ....")
    print("3 : exit ....")

    ch=int(input("enter choice :-"))

    if ch==1:
        
        signup={
        "id":input("enter id :-"),
        "email":input("enter email :-"),
        "password":input("enter password :-"),
        "classs":input("enter class :-"),
        "rank":input("enter rank :-"),
        "con_password":input("enter password :-")
        }
        if "@" not in "email" or "." not in "email":
            print("incorrect email")
        if "password" =="con_password":
            print("try again")

        else:
            print("signup successfully")
        
        student.update(signup)
    elif ch==2:
       login={
         "email":input("enter email :-"),
         "password":input("enter password :-")
       }
       if  signup["email"] == login["email"] and signup["password"]==login["password"] :
            print("login successfully")
            print(student)
       else:
            print("try again")

    elif ch==3:
        break

    else:
        print("invalid")
        


    
