x=int(input("Enter any natuaral : "))   
print("Prime numbers between 1 and ",x," are: ")

for num in range(1,x + 1):
   
   if num > 1:
       for i in range(2,int(num**0.5)):
           if (num % i) == 0:
               break
       else:
           print(num)
