def enterProducts(): #Function 1
# Here we got the cashier to input all the products bought one by one 
# We stored all that info in a dictionary called "buyingData" and returned it back 
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Press A to add product and Q to quit: ')
        if details == 'A':
            product = input('Enter product: ')
            quantity = int(input('Enter quantity: '))
            buyingData.update({product: quantity})
        elif details =='Q':
            enterDetails = False
        else:
            print('Please select a correct option')
    return buyingData


def getPrice(product, quantity): # Function 2
# The job of this function is to give the subtotal of a single product as per its price and 
# quantity mentioned
    priceData = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3
    } 
    subtotal = priceData[product] * quantity
    print(product + ':$ ' +
    str(priceData[product]) + 'x' +str(quantity) + '=' + str(subtotal))
    return subtotal

def getDiscount(billAmount, membership): #Function 3
# Here, as per the total bill amount we decide the discount is applicable or not 
    discount = 0
    if billAmount >= 25:
        if membership == 'Gold':
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == 'Sliver':
            billAmount = billAmount*0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount*0.95
            discount = 5
        print(str(discount) + ' percent off for ' + membership + '' +' membership on total amount: $'+ str(billAmount))
    else:
        print('No discount on aamount less than $25')
    return billAmount

def makeBill(buyingData, membership): # Function 4
    billAmount = 0
    # loop start
    # Call function 2 until subtotal is added for all products with buyingData
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    #loop ends
    # Call Function 3 to calculate discounted amount
    # This is the main part of the program which is not inside any function 
    # The first line of execution of code will start from here...
    billAmount = getDiscount(billAmount, membership)
    print('The discounted amount is $' + str(billAmount))

buyingData = enterProducts() # Makes call to the Function 1
membership = input('Enter customer membership: ')
makeBill(buyingData, membership) #Makes a call to Function 4
