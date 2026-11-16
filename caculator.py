while True:
    print("=========== calculator ===========")

    print("1 : add")
    print("2 : sub")
    print("3 : multi")
    print("4 : div")
    print("5 : exit")

    while True:
      ch=input("enter choice :-")
      if ch.isdigit() and 1<=  int(ch)<=5:
         ch=int(ch)
         break
      else:
         print("invalid invalid choice")

    while True:
       a=input("enter first value :-")
       if a.isdigit() :
          a=int(a)
          break
       else:
          print("invalid first value")

    while True:
       b=input("enter second value :-")
       if b.isdigit():
          b=int(b)
            
          break
       else:
          print("invalid second value")

    if ch==1:
       print(a+b)

    elif ch==2:
       print(a-b)

    elif ch==3:
       print(a*b)

    elif ch==4:
       print(a/b)

    elif ch==5:
       break

    else:
       print("invalid")
