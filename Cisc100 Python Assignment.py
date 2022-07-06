print("Please enter the number of coins:")
while True:
    try:
        
        quarters = int(input("# of quarters:"))
        if quarters <=0:
            print("Positive numbers only")
        if quarters not in range(10000):
            print("Enter an amount between 1-9999")
        quarters = quarters*25

        dimes = int(input("# of dimes:"))
        if dimes <=0:
            print("Positive numbers only")
        if dimes not in range(10000):
            print("Enter an amount between 1-9999")    
        dimes = dimes*10

        nickels = int(input("# of nickels:"))
        if nickels <=0:
            print("Positive numbers only")
        if nickels not in range(10000):
            print("Enter an amount between 1-9999")
        nickels = nickels*5

        pennies = quarters + dimes + nickels
        
        while True:
            cont = input("Do you wish to continue? Enter 'y' or 'n'")
            
            while cont.lower() not in ("y","n"):
                print("Only enter 'y' or 'n'")
                break
            if cont == "n":
                print(f'Program Terminated')
                break
            if cont == "y":
                print(f'The total is {pennies} pennies')

            break
    except ValueError:
        print("Please input Numerical values only...") 
    break
