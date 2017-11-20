places_for_vacations = {}

button = True

while button:
    place = input("If you could visit one place in the world, where would you go?")
    name = input("And please tell me your name. ")
    places_for_vacations[name] = place
    
    reply = input('Would you like to let another person respond? Yes/No ')
#    onemore_time
    
    if reply == 'No':
        button = False
    
    else:
        button = True

for name,place in places_for_vacations.items():
    print(name+' wants to visit '+place+' for vacation.')