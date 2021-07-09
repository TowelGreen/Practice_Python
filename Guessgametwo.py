import random

correct=random.randint(1,101)
choice=int(input('Quess my number its between 1 to 100:'))


tries=1
while True:
    if correct==choice:
        print('you are correct')
        results=f"It took you {tries} attemps to get that right"
        print(results)
        break
    else:
        tries += 1
        check=abs((choice - correct))
        if check > 50:
            check='You are cold'
        elif check > 25:
            check='Warmer'
        elif check < 5:
            check="HOT!HOT!HOT"
        answer= f"incorrect {check}"
        choice=int(input("Guess again: "))
        print(answer)
