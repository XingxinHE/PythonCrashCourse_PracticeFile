boston_magicians = ['Larry Bird','Ray Allen','Paul Pierce','Kyrie Irving']
great_magicians = []
def show_magicians(magicians):
    """print every element in the list"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """add 'the great' in the element"""
    
#    add a temporary list
    great_magicians = []
    
#    this is too hard-coded
#    magicians_copy = magicians[:]
    
    
#    ATTENTION!! to modify each element in the list, use WHILE!!!
    while magicians:
        great_magician = "the Great "+magicians.pop()
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
        
#    add the return value
    return magicians

show_magicians(boston_magicians)

#dont need this complicate
#show_magicians(make_great(boston_magicians))

great_magicians = make_great(boston_magicians[:])
show_magicians(great_magicians)
show_magicians(boston_magicians)

