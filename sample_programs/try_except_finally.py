try:
    x = int(input("Enter a number: "))
    print(x)
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
finally:
    print("The 'try except' is finished")