file_name = ['cats.txt','dogs.txt']

for f_name in file_name:
    try:
        with open(f_name, 'r') as file:
            content = file.readlines()
            

    except FileNotFoundError:
        pass
    
    else:
        print(content)

#with open(file_name2, 'r') as file:
#    content = file.readlines()
#    print(content)