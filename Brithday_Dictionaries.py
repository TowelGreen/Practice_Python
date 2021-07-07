birthdays={'Albert':'02/04/2004',
             'Maria':'10/20/1965',
             'Benjamin ':'07/23/1943'}

print('Welcome to the birthday dictionary. We know the birthdays of:') 
for n in birthdays:
    print(n)
c=input("Who's birthday do you want to look up?")
if c in birthdays:
    name=c
    print(f'{name} brithday is {birthdays[name]}')
else:
    print("We dont have that name")