list_of_guest = ['Peidie','Taylor','Rhiana','Emma']
print(list_of_guest)
print("Miss "+list_of_guest[1]+"can't be there")
list_of_guest[1]="Gomez"
print(list_of_guest)
list_of_guest.insert(0,'Wuhan')
list_of_guest.insert(-1,'Pink')
list_of_guest.append('Sia')
print(list_of_guest)
print("Due to the terrible restaurant, we could only invite two person.")
print("Sorry, Miss "+list_of_guest.pop(-1),"I cannot invite you.")
print("Sorry, Miss "+list_of_guest.pop(-1),"I cannot invite you.")
print("Sorry, Miss "+list_of_guest.pop(-1),"I cannot invite you.")
print("Sorry, Miss "+list_of_guest.pop(-1),"I cannot invite you.")
print("Sorry, Miss "+list_of_guest.pop(-1),"I cannot invite you.")
print("Hi, Miss "+list_of_guest[0],"you are still invited.")
print("Hi, Miss "+list_of_guest[1],"you are still invited.")
del list_of_guest[1]
del list_of_guest[0]
print(list_of_guest)
