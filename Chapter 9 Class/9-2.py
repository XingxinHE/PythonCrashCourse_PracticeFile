class Restaurant():
    """My first class using Python!"""
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("\nOur restaurant is "+self.restaurant_name+".")
        print("We provide "+self.cuisine_type+" for you.")
    
    def open_restaurant(self):
        print("We are opening right now!")

fourseasons = Restaurant('Four Seasons Hotel','INTERNATIONAL DINING EXPERIENCE')
genkisushi = Restaurant('Genki Sushi','delicious sushi')
ludingji = Restaurant('Luk Show','Szechuan Hotpot')

fourseasons.describe_restaurant()
genkisushi.describe_restaurant()
ludingji.describe_restaurant()