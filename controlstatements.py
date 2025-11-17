num=int(input("enter a number"))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

    if num%2==0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
        #if elif else statement
        marks=int(input("enter a marks:"))
        if 80 <= marks <= 100:
            print(f"{marks} is an A")
        elif 79 <= marks <=60:
            print(f"{marks} is an B")
        elif 59 <= marks <= 50:
            print(f"{marks} is an C")
        elif 49 <= marks <= 40:
            print(f"{marks} is an D")
        elif 39 >= marks <=30:
            print(f"{marks} is an E")
        else:
            print(f"{marks} is an F")




