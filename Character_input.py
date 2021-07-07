from datetime import datetime

print('what is your name and age')

name=input('name: ')
age=int(input('age: '))

currentYear = datetime.now().year

year=currentYear+100-age


print(f'{name} you will be 100 years old in {year}')