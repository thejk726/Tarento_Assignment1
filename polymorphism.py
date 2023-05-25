class Car:
    def accelerate(self):
        print("The car is now at top speed")

    def nationality(self):
        print("A car's nationality is it's country of origin")


    def honk(self):
        print("The car goes beep!")

class Audi(Car):
    def accelerate(self):
        print("Audi top speed at 130 mph")

    def nationality(self):
        print("Audi is a German company")

    def honk(self):
        print("Audi goes Beep!")

class Ferrari(Car):
    def accelerate(self):
        print("Ferrari top speed at 135 mph")

    def nationality(self):
        print("Ferrari is an Italian company")

    def honk(self):
        print("Ferrari goes beep!")

class Bentley(Car):
    def accelerate(self):
        print("Bentley top speeds at 120 mph")

    def nationality(self):
        print("Bentley is a British company")

    def honk(self):
        print("Bentley goes beep!")


#Operator polymorphism example

class vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __add__(self,other): #function to perform 2-D vector addition
        a_sum=self.a+other.a
        b_sum=self.b+other.b
        sum=vector(a_sum,b_sum)
        return sum


def fun(obj):
    obj.nationality()
    obj.accelerate()
    obj.honk()


c=Car()
a=Audi()
b=Bentley()
f=Ferrari()

for obj in [c,a,b,f]:
    fun(obj)
    
#Operator polymorphism 
print(2+3)
print("Hello "+"World!")
v1=vector(1,2)
v2=vector(3,4)
v_sum=v1+v2 # '+' operator return a new vector whose attributes have values equal to the sum of respective components of the two component methods.
print(v_sum.a, v_sum.b)