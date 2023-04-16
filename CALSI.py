def add(a,b):
    return a + b


def subtract(a,b):
    return a - b


def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

print("select operations.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
       # take input from the user
       choice = input("Enter choice(1/2/3/4): ")


       if choice in ('1','2','3','4'):
           num1=float(input("Enter first number: "))
           num2=float(input("Enter second number:"))

           if choice=='1':
               print(num1, "+" ,num2, "=",add(num1, num2))

           elif choice=='2':
               print(num1, "-" , num2, "=",subtract(num1, num2))

           elif choice=='3':
               print(num1, "*" , num2, "=",multiply(num1, num2))

           elif choice=='4':
               print(num1,"/" , num2, "=",divide(num1, num2))

               #check if user wants another calculation
               # break the while loop if answer is no
               next_calculation = input("Let's do next calculation? (yes/no): ")
               if next_calculation =="no":
                   break
       else:
           print("invalid Input")