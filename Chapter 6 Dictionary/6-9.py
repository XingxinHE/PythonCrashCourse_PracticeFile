favorite_places = {
        'Jiamin HUANG':['Beijing','Guangzhou','Chengdu'],
        'Yiming LIANG':['Los Angeles','San Francisco','San Diego'],
        'Xingxin HE':['Guangzhou','Shanghai','Hong Kong'],
        'Peidie LI':['Tengchong','Yangjiang','Toronto']
        }

for name,places in favorite_places.items():
    print('\n'+name+"'s favorite languages are: ")
    for place in places:
        print('\t'+place)