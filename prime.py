x=int(input("Enter any natural "))
print("Prime numbers between 1 and",x,"are:")

for num in range(1,x + 1):

    for i in range(2,num):
        if (num % i) == 0:
            break
    else:
        print(num)
