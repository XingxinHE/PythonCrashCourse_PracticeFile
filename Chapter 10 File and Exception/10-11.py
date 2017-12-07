import json
num = input("Please type your favorite number.")

file_name = 'number_files.json'
with open(file_name,'w') as file:
    json.dump(num, file)

with open(file_name) as file:
    user_num = json.load(file)
    print("I know your favorite number! It's "+user_num+".")
    