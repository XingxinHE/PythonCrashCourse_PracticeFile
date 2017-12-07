file_name = 'learning_python.txt'

with open(file_name) as file:
    lines = file.readlines()

print(lines)

for line in lines:
    print(line)

python_zen_list = []
for line in lines:
    python_zen_list.append(line)
print(python_zen_list)


