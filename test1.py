'''
Problem statement :- if you are given a nested dictonary how would you 
get a value from any part of the dictionary?
'''

d1 = {
    'name':{
        'firstname':'harsh',
        'lastname' :'valecha',
        'purvaj':{
            'jaktap':'house',
            'kamlesh':{
                'chaterjee':'done'
            }
        }
    },
    'age':23
}


def value(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        for i in dictionary:
            if type(dictionary[i])==dict:
                return value(key,dictionary[i])

print(value('chaterjee',d1))