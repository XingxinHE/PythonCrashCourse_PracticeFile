file_name = 'reason_for_programming.txt'

while True:
    reason = input("Why do you like programming?   ")
    with open(file_name,'a') as file:
        file.write(reason+'\n')