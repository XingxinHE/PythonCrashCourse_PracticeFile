sandwich_orders = ['Pastrami','Reuben Sandwich','Pastrami','Club Sandwich','Croque-monsieur','Pastrami']
print('Sorry, pastrami have been sold out!')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print(sandwich_orders)