cities={
        'Tengchong':{
                'country':'China',
                'population':'65990',
                'fact':'650 km west of Kunming.'
                },
        'Toronto':{
                'country':'Canada',
                'population':'2731571',
                'fact':'a centre of business, finance, arts, and culture.'
                },
        'Basel':{
                'country':'Swizerland',
                'population':'175000',
                'fact':'is known for its many internationally renowned museums.'
                }
        }

for city,cityInfo in cities.items():
    print('\n'+'Tell me something about '+city+'!')    
    print(city+' is in '+cityInfo['country']+'.')
    print('The population of '+city+'is about '+cityInfo['population']+'.')
    print(city+' ' +cityInfo['fact'])
    
