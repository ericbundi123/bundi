

def myfunton():
    print("This is my first function")
    myfunton()

    #function with parameters
    def students(name,age,gender):
        print(f"student na is {name}")
        print(f"student na is {age}")
        print(f"student na is {gender}")
        students( Eric,20,male)
        students(mercy,20,female)

        #function with return values
        def add_numbers(a,b):
            return a+b
        result=add_numbers(a=3,b=9)
        print(result)