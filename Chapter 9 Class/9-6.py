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
        
class IceCreamStand(Restaurant):
    """father and son class"""
    
    def __inti__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours = []
        
    def show_icecream(self):
        print("The icecream is made of: ")
        for flavour in self.flavours:
            print("\t"+flavour)
            
my_icecream = IceCreamStand('Starbuck','sweet')
my_icecream.flavours = ['strawberry','mango','watermelon']
my_icecream.show_icecream()
    
    