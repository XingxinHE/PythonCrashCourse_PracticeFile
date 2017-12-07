file_name = ['cats.txt','dogs.txt']

for f_name in file_name:
    try:
        with open(f_name, 'r') as file:
            content = file.readlines()
            #好像一定要在with后面接东西，不然无法运行

    except FileNotFoundError:
        print("Sorry,"+f_name+" is not found.")
    
    else:
        print(content)

#with open(file_name2, 'r') as file:
#    content = file.readlines()
#    print(content)