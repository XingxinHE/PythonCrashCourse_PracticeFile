inputInfo = input('Please type your name.')
file_name = 'guest.txt'
with open(file_name,'a') as file:
    file.write(inputInfo)