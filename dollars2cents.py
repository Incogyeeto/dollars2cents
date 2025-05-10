def main():

    def changeConverter(dollars):
        # Removes the '$' for changing type to int
        dollars = dollars.replace('$', '') 
        ''' The try/except/else is used here in the case the
          user inputs a whole number instead of a float, there
            would only be one value. The else statment catches
              cases if they input something less than 1. '''
        try: 
            # Splits the dollars and cents apart
            dollars, cents = dollars.split('.') 
        except ValueError:
            cents = 100 * int(dollars)
        else:
            if dollars != '':
                # Combines into the change value of both dollars and cents
                cents = int(cents) + (int(dollars) * 100) 
        return int(cents)

    def coinDistributor(change):
        # Initialize a count for all coin types
        quarters = 0 
        dimes = 0
        nickels = 0
        pennies = 0
        ''' A loop to check through all the coin types.
          Checks for all potential quarters first then goes 
          through the other coins. Modulo operator allows for 
          it to check through and if it isn't 0 it subtracts 
          a penny. If it is a number like 0.07 it would remove
            the pennies first then the nickel. '''
        while change > 0:
            if change / 25 >= 1:
                change -= 25
                quarters += 1
            elif change % 10 == 0:
                change -= 10
                dimes += 1
            elif change % 5 == 0:
                change -= 5
                nickels += 1
            else:
                change -= 1
                pennies += 1
            
        print(f'Quarters:{quarters} \nDimes:{dimes} \nNickels:{nickels} \nPennies:{pennies}') # Prints each coin type and their count

    money = input('Dollars: ')
    money = changeConverter(money)
    coinDistributor(money)

main()