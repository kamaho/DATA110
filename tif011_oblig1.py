
#----------------- Task 01 -----------------------------------#
print("----------------------- Task 01 ----------------------")
#Nameprogram version one. This program assumes everyone has a middle name.
def nameOne():

    print ("This program assumes everyone has a middle name" + '\n')
    first_name = input ("Enter your first name:")
    middle_name = input ("Enter your middle name:")
    last_name = input ("Enter your last name:")
    print (first_name + '\n' + middle_name + '\n' + last_name + '\n')

#Nameprogram version two. Takes account for people without middlename.
def nameTwo():

    print ("This program takes into account that some people don't have middlename" + '\n')
    f_name = input ("Enter your first name: ")
    m_name = input ("Enter your middle name. Press enter if you do not have one: ")
    l_name = input ("Enter your last name: ")
    if m_name == "":
        print (f_name + '\n' + l_name)
    else:
        print (f_name + '\n' + m_name + '\n' + l_name) + '\n'


nameOne()
nameTwo()

#----------------- Task 02 -----------------------------------#
print("----------------------- Task 02 ----------------------")

def asteriksName():
    print('\n')
    print(' *    *      *     ******    *')
    print(' *  *       * *    *     *   *')
    print(' **        *****   *****     *')
    print(' *  *     *     *  *    *    *')
    print(' *    *  *       * *      *  *******')
    print('\n')

asteriksName()

#----------------- Task 03 ----------------------------------#
print("----------------------- Task 03 ----------------------")

def currencyConverter():
    # Currency rates
    eur_rate = 0.1075
    usd_rate = 0.1236

    # Symbols
    eur_symbol = "€"
    usd_symbol = "$"

    # Input from user
    amount = float(input("Enter amount in NOK: "))

    # Convert to eur and usd
    eur_amount = round(amount * eur_rate, 2)
    usd_amount = round(amount * usd_rate, 2)

    # Print results
    print(f"{amount} NOK = {eur_amount}{eur_symbol}")
    print(f"{amount} NOK = {usd_amount}{usd_symbol}")

currencyConverter()


