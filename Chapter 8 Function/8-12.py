def order_sandwich(*toppings):
    print("We are making sandwich for you, and the toppings are: ")
    for topping in toppings:
        print("\t-"+topping)

order_sandwich('Mocha','Jiangyou','Mayou')
order_sandwich('Mocha')
