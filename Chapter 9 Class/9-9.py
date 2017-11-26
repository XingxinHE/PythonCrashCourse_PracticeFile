class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    

class Battery():
    
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

    
    def get_range(self):
        print("Your vehicle range is "+str(self.battery_size)+" miles.")


class ElectricCar(Car):
    
    def __init__(self,make,model,year):
        
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('Tesla','Model X',2017)

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()