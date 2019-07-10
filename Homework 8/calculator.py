# my first calculator
# published in 2019
# author: P. Ohm

print("Welcome to this simple, yet great, calculator! ""\n""I will try to help you with any math. Give it a try!")
print("Remember: Don´t try to divide by zero!")
first_number = int(input("Please enter the first number:"))
second_number = int(input("Please enter the second number:"))
operator = str(input("Choose your calculation-operator: +,-,*,/"))


if operator == "+":
    print("Your result is = "+str(first_number + second_number))
elif operator == "-":
    print("Your result is= "+str(first_number-second_number))
elif operator == "*":
    print("Your result is= "+str(first_number*second_number))
elif operator == "/" and second_number != 0:
    print("Your result is= "+str(first_number/second_number))
elif operator == "/" and second_number == 0:
    print("I did warn you! World extinction initiated.""\n""You divided by zero. Mankind is doomed.")
else:
    print("Wrong user input. Read instructions carefully.")




