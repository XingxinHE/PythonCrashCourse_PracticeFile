try:
    num_1 = int(input("Please input a number."))
    num_2 = int(input("Please input another number."))
except ValueError:
    print("Sorry, you must type a number.")
else:
    num = num_1 + num_2
    print(num)

