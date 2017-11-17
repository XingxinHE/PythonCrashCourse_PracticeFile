account_list = ['Eric','Morris','Steven','admin','Oscar']

for account in account_list:
    if account == 'admin':
        print('Hello '+account+', would you like to see a status report?')
    else:
        print('Hello '+account+',thank you for logging in again.')

if account_list:
    for account in account_list:
        print(account)
else:
    print('We need to find some users!')


current_users = ['Eric','Morris','steven','admin','Oscar']
new_users = ['Yolanda','Eva','Mandy','Oscar','Steven']
for account in new_users:
    if account.lower() in current_users:
        print('Sorry, '+account+' has been registered.')
    else:
        print(account+' is a valid account name!')
        

#lower() is for string, but how can I convert a list to lower case.