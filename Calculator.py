#Project Name - Basic Calculator

#Addition of two values
def add(a,b):
    return a+b

#Subtraction of two values
def subtract(a,b):
    return a-b

#Mulitplication of two values
def multiply(a,b):
    return a*b

#Division of two values
def divide(a,b):
    if b==0:
        print("Divisible by zero is not possible")
    else:
        return a/b

#Modulous of two values
def modulo(a,b):
    if b==0:
        print("Modulo by zero is not possible")
    else:
        return a%b

a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")

choice = int(input("Enter your choice:"))

if choice == 1:
    print(add(a,b))
elif choice == 2:
    print(subtract(a,b))
elif choice == 3:
    print(multiply(a,b))
elif choice == 4:
    print(divide(a,b))
elif choice == 5:
    print(modulo(a,b))
else:
    print("Invalid Choice")