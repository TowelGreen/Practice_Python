def MaxofThree():
    print("chose 3 number to be arrange from largest to smallest")
    num1=int(input("First number:"))
    num2=int(input('second number'))
    num3=int(input('thrid number'))

    if num1 > num2 and num3 and num2>num3:
        print(num1,num2,num3)
    elif num2 > num1 and num3 and num1 >num3:
        print(num2,num1,num3)
    elif num3 > num1 and num2 and num1> num2: 
        print(num3,num1,num2) 
    elif num3> num1 and num2 and num2> num1:
        print(num3,num2,num1)
    elif num2 > num1 and num3 and num3 >num1:
        print(num2,num3,num1)

MaxofThree()


        

  