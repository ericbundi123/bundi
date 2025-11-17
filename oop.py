#define a class

class Student:

   # define a constructor/initializer
def __init__(self,name,score):
               self.name=name
                 self.score=score

# define a method
def display(self):
 print(f"Name: {self.name} Score: {self.score}")

# define a method to check if student passes
def check_pass(self):
 return self.score>=50

# create objects
s1=Student("Fraciah",85)
s2=Student("eric", 40)

# use methods

s1.display()
print(f"passed status: {s1.check_pass()}")




