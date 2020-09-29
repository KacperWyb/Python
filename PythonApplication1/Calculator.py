class Calculator(object):
    """description of class"""

    def calculator():
        print("Prosty kalkulator ☺")
    
        while True:
            try:
                n1 = int(input("Podaj pierwszą liczbę: "))
                char = input("Podaj operator matematyczny: ")
                n2 = int(input("Podaj drugą liczbę: "))

                if(char == "+"):
                    result = n1 + n2
                elif(char == "-"):
                    result = n1 - n2
                elif(char == "*"):
                    result = n1 * n2
                elif(char == "/"):
                    result = n1 / n2
                else:
                    print("Nie rozumiem")
                    Calculator.calculator()

                print("Twój wynik to: " + str(result))
                return

            except:
                print("Słuchaj poleceń! Jeszcze raz.")
                Calculator.calculator()
    
        
    
        


        

