def Prime_check():     
    num=int(input('Check if number is prime: '))
    listRange = list(range(1,num+1))
    divisors=[]


    for number in listRange:
        if num % number == 0:
            divisors.append(number)

    
    
    if len(divisors)> 2:
     print('Your number is not prime')  

    else:
        print ("Your number is prime")    









Prime_check()        










        
