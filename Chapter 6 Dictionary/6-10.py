favorite_numbers = {
        'Jiamin HUANG':[57,37,92,91,23],
        'Yuelin LI':[4,20,87,67,13],
        'Shuting MO':[12,78,50,52,38]}

for name,numbers in favorite_numbers.items():
    print('\n'+name+"'s favorite numbers are:")
    for num in numbers:
        print('\t'+str(num))