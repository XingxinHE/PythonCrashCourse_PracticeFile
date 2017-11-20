prompt = '\nPlease select your ingredients.'
prompt += "\nType 'quit' to finish."
ingredients = ''

while ingredients != 'quit':
    ingredients = input(prompt)
    
    if ingredients != 'quit' :
        print('\nThank you.'+ ingredients+' has been added.')
