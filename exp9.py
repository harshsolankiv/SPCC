def constant_propagation(code):
    change = code.replace('22/7', '3.14')
    print("\nAfter Optimization, the code is: ")
    print(change)  # For Program: Area of circle = 22/7*R*R


def Dead_Code_Elimination(code):
    change = code.replace('if(i==1) a= b+2;', '')
    print("\nAfter Optimization, the code is: ")
    print(change)  # For Program: i=0; if(i==1) a= b+5;


while True:
    print("\nCode Optimization")
    print("1.Constant Propagation")
    print("2.Dead Code Elimination")
    choice = int(input("\nEnter your choice of optimization : "))
    if choice == 1:
        code = (input("\nEnter the code to be optimized : "))
        constant_propagation(code)
    elif choice == 2:
        code = (input("\nEnter the code to be optimized : "))
        Dead_Code_Elimination(code)
    else:
        print("Wrong Choice")
