class Operation:
    def __init__(self):
        self.number1= 12
        self.number2= 3

    def show_number1(self):
        print("le Nombre 1 est : " , self.number1)
    
    def show_number2(self):
        print("le Nombre 1 est : " , self.number2)

    def show_addition(self):
        print("Nombre 1 + Nombre 2 = " , self.number1 + self.number2)




operation = Operation()

#print(operation)
operation.show_number1()
operation.show_number2()
operation.show_addition()
