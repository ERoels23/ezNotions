def run():
    # code written below will be traced by the program
    def myFunc():
        myVar = "hehe"
        return myVar
    print(type(myFunc))
    x = 1
    y = x
    myFunc()
    z = 3
    h = 7

if __name__ == "__main__":
    run()

