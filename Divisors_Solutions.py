

num=int(input('Check Divisors of number: '))
listRange = list(range(1,num+1))
divisors=[]


for number in listRange:
    if num % number == 0:
        divisors.append(number)

print(divisors)