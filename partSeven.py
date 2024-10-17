q = input("type 'quit' to quit ")

if q != "quit":
    while q != "quit":
        q = input("would you like to quit ")
        def inpu():
            x = int(input("what is x? "))
            op = input("what is the opperation? ")
            y = int(input("what is y? "))

            def calculation():
                match op:
                    case "+":
                        result = x + y
                        print (f"{x} + {y} = {result}")
                    case "-":
                        result = x - y
                        print (f"{x} - {y} = {result}")
                    case "*":
                        result = x * y
                        print (f"{x} * {y} = {result}")
                    case "/":
                        if y == 0:
                            print("cannot divide by zero.")
                        else:
                            result = x / y
                            print (f"{x} / {y} = {result}")
                    case "^":
                        result = x ** y
                        print (f"{x} ^ {y} = {result}")
                    case "%":
                        if y == 0:
                            print("cannot divide by zero.")
                        else:
                            result = x % y
                            print (f"{x} % {y} = {result}")
            def main():
                if x == "" or y == "" or op == "":
                    print ("please give a calculation or type 'quit' for opperation.")
                else:
                    calculation()
            
           
            main()
        inpu()
else:
    print("ending program.")