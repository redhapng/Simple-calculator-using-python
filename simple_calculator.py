#Simple calculator 

#Add
def add(x, y):
    return x + y
#Subtract
def subtract(x, y):
    return x - y
#Multiply 
def multiply(x, y):
    return x * y
#Divide
def divide(x, y):
    return x / y

#Selcting Operation:
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice_op = input("Enter your choice (1/2/3/4) :\n")
    if choice_op in ('1' '2' '3' '4'):
        try:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))
        except ValueError:
            print("Invalid input, try again ! ")
            continue
        if choice_op == "1":
            print (num1, "+", num2, "=" ,add(num1, num2) )
        elif choice_op == "2":
            print (num1, "-", num2, "=" ,subtract(num1, num2) )            
        elif choice_op == "3":
            print (num1, "*", num2, "=" ,multiply(num1, num2) )
        elif choice_op == "4":
            print (num1, "/", num2, "=" ,divide(num1, num2) )
        next_calculation = input("Let's do next calculation? (yes/no):\n")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")