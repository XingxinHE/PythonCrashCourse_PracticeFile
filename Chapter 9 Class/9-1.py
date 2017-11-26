class Restaurant():
    """My first class using Python!"""
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Our restaurant is "+self.restaurant_name+".")
        print("We provide "+self.cuisine_type+" for you.")
    
    def open_restaurant(self):
        print("We are opening right now!")

restaurant = Restaurant('Four Seasons Hotel','INTERNATIONAL DINING EXPERIENCE')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()