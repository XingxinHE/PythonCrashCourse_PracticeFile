dic = {
       'Nile' : 'Egypt',
       'Yellow River' : 'China',
       'Amazon River' : 'Brazil'
       }

for river in dic.keys():
    print(river)

print('\n')

for country in dic.values():
    print(country)

print('\n')

favorite_languages = {
        'Jen' : 'Python',
        'Sarah' : 'C',
        'Edward' : 'Ruby',
        'Phil' : 'Python'
        }

coders = ['Jen','Steven','Sarah','Morris','Edward']

for coder in coders:
    if coder in favorite_languages.keys():
        print(coder+' ,you have done the poll.')
    else:
        print(coder+' ,please finish the poll.')
        

