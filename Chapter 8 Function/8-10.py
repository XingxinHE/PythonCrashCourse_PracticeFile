boston_magicians = ['Larry Bird','Ray Allen','Paul Pierce','Kyrie Irving']

def show_magicians(magicians):
    """print every element in the list"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """add 'the great' in the element"""
    
#    add a temporary list
    great_magicians = []
    
#    ATTENTION!! to modify each element in the list, use WHILE!!!
    while magicians:
        great_magician = "the Great "+magicians.pop()
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)

show_magicians(boston_magicians)
make_great(boston_magicians)
show_magicians(boston_magicians)