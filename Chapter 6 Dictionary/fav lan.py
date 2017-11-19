favorite_lan = {
        'Jen' : ['Python','Ruby'],
        'Sarah':['C'],
        'Edward':['Ruby','Go'],
        'Phil':['Python','Haskell']}

for name, languages in favorite_lan.items():
    if len(languages)>1:
        print("\n"+name+"'s favorite languages are: ")
        for language in languages:
            print("\t"+language)
    else:
        print("\n"+name+"'s favorite language is: "+languages[0])