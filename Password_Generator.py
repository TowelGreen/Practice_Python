import random
import string
from typing import Counter

#

def strong_password():
    passlenth=20
    passwword=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits+string.punctuation) for _ in range(0,passlenth))
    print(passwword)



def medium_password():
    passlenth=12
    password="".join(random.choice(string.ascii_letters + string.digits) for _ in range(0,passlenth))
    print(password)

def weak_password():
    easypass=["123456",'password123','password1234','1111111','abcd123','myisbobs','cheese123','bluegreen','123123123']
    password=(random.choice(easypass))
    print(password) 



name="__main__"
c=input('Do you want a strong, medium or weak password: ')
if c=='strong':
   strong_password()
elif c=='medium':
    medium_password()
elif c=="weak":
    weak_password()
else:
    if c is not 'strong'or'medium'or 'weak':
        print('Not a option')

