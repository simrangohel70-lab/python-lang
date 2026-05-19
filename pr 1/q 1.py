print("welcome to personal data coollecter")

name=input("enter your name:")
age=int(input("enter your age:"))
height=float(input("enter your height:"))
favourite_number=int(input("enter your favourite number:"))

print("here is the information  we collected!")

print("name:",name)
print("type:",type(name))
print("address:",id(name))

print("age:",age)
print("type:",type(age))
print("address:",id(age))

print("height:",height)
print("type:",type(height))
print("address:",id(height))

print("favourite_number:",favourite_number)
print("type:",type(favourite_number))
print("address:",id(favourite_number))

birth_year=2026-age

print("approx_birth year:",birth_year)
print("age:",age)
print("thank_you for using our data collector ")
print("goodbye!")

