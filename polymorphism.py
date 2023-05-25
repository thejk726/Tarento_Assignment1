class Car:
    def accelerate():
        print("The car is now at top speed")

    def nationality():
        print("A car's nationality is it's country of origin")


    def honk():
        print("The car goes beep!")

class Audi(Car):
    def accelerate():
        print("Audi top speed at 130 mph")

    def nationality():
        print("Audi is a German company")

    def honk():
        print("Audi goes Beep!")

class Ferrari(Car):
    def accelerate():
        print("Ferrari top speed at 135 mph")

    def nationality():
        print("Ferrari is an Italian company")

    def honk():
        print("Ferrari goes beep!")

class Bentley(Car):
    def accelerate():
        print("Bentley top speeds at 120 mph")

    def nationality():
        print("Bentley is a British company")

    def honk():
        print("Bentley goes beep!")


#Operator polymorphism example

class vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __add__(self,other):
        a_sum=self.a+other.a
        b_sum=self.b+other.b
        sum=vector(a_sum,b_sum)


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
v_sum=v1+v2
print(v_sum.a, v_sum.b)