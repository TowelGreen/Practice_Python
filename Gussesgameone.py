
import random

correct=random.randint(1,9)
choice=int(input('Chose a number from 1 to 9:'))

if correct==choice:
    print('you are correct')
else:
    check=abs((choice - correct))
    answer= f"incorrect the correct answer is {correct} your off by {check}"
    print(answer)