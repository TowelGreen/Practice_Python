


def Remove_Duplicates():
    lst=[]
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())

        lst.append(ele) # adding the element

    print(list(set(lst)))



Remove_Duplicates()
    