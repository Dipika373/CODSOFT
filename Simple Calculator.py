print("                Simple Calculator        ")
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def modulous(a,b):
    return a%b
print("\nSelect Operation")
print("1.Addition")
print("2.Substraction")
print("3.Multiply")
print("4.Division")
print("5.Moduleous")
while True:
    choice=input("Enter choice(1/2/3/4/5):")
    if choice in ('1','2','3','4','5'):
        try:
            num1=float(input("Enter the first number: "))
            num2=float(input("Enter the second number: "))
        except valueError:
            print("Invail Input.Please Enter the valid number> ")
            continue
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",substract(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",divition(num1,num2))
        elif choice=='5':
            print(num1,"%",num2,"=",modulous(num1,num2))
        next_calculation=input("Let do next Calculation ? (yes/No):")
        if next_calculation==No:
            break
    else:
        print("Invaild Input")
                
                
                













