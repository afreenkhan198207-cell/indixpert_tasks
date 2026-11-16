while True:
    n=input("enter numbeer of files :-")

    if n.isdigit():
        num=int(n)
        break
    else:
        print("invalid...")
    

for i in range(1,num + 1):
        
        with open(f"data{i}.txt","w") as file:
            file.write(f"file{i}")
