class MyCalculator:
    def Add(x,y):
        return x+y
    def Sub(x,y):
        return x-y
    def Mux(x,y):
        return x*y
    def Div(x,y):
        return x/y
    
    print("1.Add/2.Subtract/3.Multiply/4.Divide")
    while True:
        choice=input("Enter(1/2/3/4)")
        if choice in('1','2','3','4'):
            num1=float(input("Enter First Number:"))
            num2=float(input("Enter Second Number:"))
            if choice=='1':
                print("Addition: ",Add(num1,num2))
            elif choice=='2':
                print("Subtraction: ",Sub(num1,num2))
            elif choice=='3':
                print("Multiplication: ",Mux(num1,num2))
            elif choice=='4':
                print("Division: ",Div(num1,num2))
            nc=input("Want to continue? (0/1)")   
            if nc=="0":
                break
        else:
            print("Invalid Input")