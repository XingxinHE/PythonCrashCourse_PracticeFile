for value in range(1,21):
    print(value)

hundred = [numbers for numbers in range(1,101)]
print (hundred)

thousands = [numbers for numbers in range(1001)]
print(min(thousands))
print(max(thousands))
print(sum(thousands))
print(thousands)

odd = [numbers for numbers in range(1,20,2)]
print(odd)

number3x = [numbers*3 for numbers in range(1,11)]
for x3 in number3x:
    print(x3)

cube = [numbers**3 for numbers in range(1,11)]
for cubenum in cube:
    print(cubenum)
    
cube2 = []
for cube2num in range(1,11):
    cube2.append(cube2num**3)
print(cube2)
