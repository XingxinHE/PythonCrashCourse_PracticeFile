while True:
    age = input("Please tell me how old are you. ")
    if int(age) <3:
        print("You can watch the movie for free.")
    elif int(age) < 12:
        print("Please pay 10 dollars.")
    else:
        print("Please pay 15 dollars.")