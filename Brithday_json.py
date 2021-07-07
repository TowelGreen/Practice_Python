import json
birthday = {}
with open('Brithday.json','r') as loaded:

    print('Welcome to the birthday dictionary. We know the birthdays of:') 
    birthdays=json.load(loaded)
    
    for n in loaded:
        print(n)
    c=input("Who's birthday do you want to look up?")
    if c in birthdays:
        name=c
        print(f'{name} brithday is {birthdays[name]}')
    else:
        print("We dont have that name")



print('Do you want to add someone')
yes_no=input("y/n")
if yes_no=="y":
    name = input('Who do you want to add to the Birthday Dictionnary?\n').title()
    date = input('When is {} born?\n'.format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print('{} was added to my birthday list\n'.format(name))
