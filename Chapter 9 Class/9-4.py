class Restaurant():
    """make some change"""
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("Our restaurant is "+self.restaurant_name+".")
        print("We provide "+self.cuisine_type+" for you.")
    
    def open_restaurant(self):
        print("We are opening right now!")
    
    def show_customer(self):
        print("We have served "+str(self.number_served)+" customers.")
        
    def set_number_served(self,customer_num):
        self.number_served = customer_num
    
    def increment_number_served(self,increment_num):
        self.number_served += increment_num

restaurant = Restaurant('Four Seasons Hotel','INTERNATIONAL DINING EXPERIENCE')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.show_customer()

restaurant.set_number_served(200)
restaurant.show_customer()
restaurant.increment_number_served(120)
restaurant.show_customer()