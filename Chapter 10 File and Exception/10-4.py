
file_name = 'guest_book.txt'

while True:
    inputInfo = input('Please type your name.   ')
    print("Hello! "+inputInfo+".")
    with open(file_name,'a') as file:
        file.write(inputInfo+"\n")
