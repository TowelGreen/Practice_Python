def Fibonacci_nums():
    
    nums=int(input('How many Fibonacci number do you want: '))
    Fibonacci=[]
    if nums==1:
        Fibonacci.append(1)
    elif nums>=2:
        Fibonacci.append(1)
        Fibonacci.append(1)
        
    for i in range(2,nums):
        Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])

    print(Fibonacci)
        
           
     




Fibonacci_nums()