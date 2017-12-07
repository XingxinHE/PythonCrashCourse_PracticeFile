file_name = 'learning_python.txt'

with open(file_name) as file:
    lines = file.readlines()

python_zen_list =[]

for line in lines:
    line = line.replace('Python','Processing')
    python_zen_list.append(line)

print(python_zen_list)

for sen in python_zen_list:
    print(sen)