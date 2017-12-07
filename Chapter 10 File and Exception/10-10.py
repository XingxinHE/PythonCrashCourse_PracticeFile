
file1 = 'Ten Books on Architecture.txt'



with open(file1) as file:
    contents = file.read()

    words = contents.split()
#    print(words)
    num = words.count('architecture')
    newWord = []
    for word in words:
        newWord.append(word.lower())
    c_num = newWord.count('architecture')
    print("This book contains "+str(num)+"words of architecture in it.")
    print("This book contains "+str(c_num)+"words of architecture in it.")