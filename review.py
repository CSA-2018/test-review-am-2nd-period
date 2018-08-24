class Person:
    def __init__(self, name, age, city, phone):
        self.name=name
        self.age=age
        self.city=city
        self.phone=phone

    def __str__(self):
        return str(self.name.title())+" is "+str(self.age)+" years old, lives in "+str(self.city.title())+", phone # is "+str(self.phone)+"."

def start():
    n=input("Name: ")
    a=input("Age: ")
    c=input("City: ")
    p=getphone()
    p1=Person(n,a,c,p)
    print(p1)

def getphone():
    while True:
        try:
            return int(input("Phone: "))
        except ValueError:
            print("Please enter numbers only")

start()