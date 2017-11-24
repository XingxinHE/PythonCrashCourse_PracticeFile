def make_car(manufacturer,model,**other_info):
    car_dic = {
            'Manufacturer':manufacturer,
            'Model':model
            }
    for key,value in other_info.items():
        car_dic[key] = value
    
    return car_dic
my_dream_car = make_car('Volkswagen','Tiguan',Color='Silver')
print(my_dream_car)