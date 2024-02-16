import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()
print(phonebook)
print(len(phonebook))

#mydictionary = {}    #this will create an empty dictionary

mydictionary = dict(m=8,n=9) # m and n are the keys and 8,9 are the values.

print(mydictionary)

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    print(f"Name: {name} Phone Number: {phonebook[name]}")
else:
    print(f"{name} is not in the phone book")
    
#phone = phonebook['Chris']
#print(phone)



print()
print('*****  end section 2 ********')
print()









print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Joe'] = '555-1023'
phonebook['Chris'] = '555-4444'

print(phonebook)



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()
print(phonebook)

del phonebook['Chris']

print(phonebook)


print()
print('*****  end section 4 ********')
print()



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

 
for key in phonebook:
    print(f"The key is: {key} and the value is {phonebook[key]}")

for value in phonebook.values():
    print(value)

for key, value in phonebook.items():
    print(f"The key is {key} and the value is {value}")

#for item_tuple in phonebook.items():
#    print(item_tuple)

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get('Chris,''555-5555')
print(phone)


phonebook.clear()


print(phonebook)

print()
print('*****  end section 6 ********')
print()


print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
remove = phonebook.pop('Chris', 'not found')
print(remove)
print(phonebook)

print()
print('*****  end section 7 ********')
print()





print()
print('*****  start section 8 - using popitem ********')
print()

print(phonebook)
a = phonebook.popitem()
print(a)
print(phonebook)




print()
print('*****  end section 8 ********')
print()


print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)

random_key = random.choice(list_of_keys)
print(random_key)

print(phonebook[random_key])
random_key = (phonebook[random.choice(list(phonebook))])

print()
print('*****  end section 9 ********')
print()







