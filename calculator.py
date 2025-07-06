def addition(a,b):
    print(f'{a} + {b} = {a+b}')
def subtraction(a,b):
    print(f'{a} - {b} = {a-b}')
def multiplication(a,b):
    print(f'{a} * {b} = {a*b}')
def division(a,b):
    print(f'{a} / {b} = {a/b}')


print("Choose what you want to do: ");
print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");

choice = input("Choose one from the above given options (1,2,3,4): ");
if(choice == "1" or choice=="2" or choice=="3" or choice=="4"):
   number1 = int(input(("Enter first number: ")));
   number2 = int(input(("Enter second number: ")));
else:
    print("Invalid input")

if(choice == "1"):
      addition(number1,number2);
elif(choice == "2"):
      subtraction(number1,number2);
elif(choice == "3"):
      multiplication(number1,number2);
elif(choice == "4"):
      division(number1,number2);
else:
      print("Invalid");
      

