sandwich_orders = ['Reuben Sandwich','Club Sandwich','Croque-monsieur']
finished_sandwiches = []

while sandwich_orders:
    processing_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(processing_sandwich)
    print('I made your '+processing_sandwich+'.')

print('\nOK then, all your sandwiches are done!')

