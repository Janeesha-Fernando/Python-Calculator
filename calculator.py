# Python Calculator 
def welcome():
    print("                                                                       Welcome to Calculator ")
    print("__________________________________________________________________________________________________________________________________________________________________")
    print("\n")
def calculate():
    try:
        num1=int(input("Enter your first number: "))
        print("\n")
        print('''Please type in the math operation you would like to complete: 
        + for addition
        - for substraction
        * for multiplication
        / for division
        ''')
        print("\n")
        operation = input("Please enter the operator: ")
        print("\n")
        num2=int(input("Enter your second number: "))
    except:
        print("Invalid input") 
        print("\n")  
        num1=int(input("Enter your first number: "))
        print("\n")
        print('''Please type in the math operation you would like to complete: 
        + for addition
        - for substraction
        * for multiplication
        / for division
        ''')
        print("\n")
        operation = input("Please enter the operator: ")
        print("\n")
        num2=int(input("Enter your second number: "))

    #Addition
    if operation == "+":
        print('{} + {} = ' .format(num1,num2),end=" ")
        print(num1+num2)

    #Substraction
    elif operation == "-":
        print('{} - {} = ' .format(num1,num2),end=" ")
        print(num1-num2)

    #Multiplication
    elif operation == "*":
        print('{} * {} = ' .format(num1,num2), end=" ")
        print(num1*num2)

    #Division
    elif operation == "/":
        print('{} / {} = ' .format(num1,num2),end=" ")
        print(num1/num2)
    else:
        print("\n")
        print("ERROR.Please enter a valid operator.")
             
  
    again()

def again():
    print("\n")
    calculate_again=input("Do you want to calculate again (Y/N) ?  ")

    if calculate_again == "Y":
        calculate()
    elif calculate_again == "N":
        print("\n")
        print("Calculator is turning off.")    
        quit()
    else:
        again()    

welcome()
calculate()
