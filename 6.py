n=int(input("enter no of terms: "))
fib=[]
fib.append(0)
fib.append(1)
for k in range(2,n):
    fib.append(fib[k-1]+fib[k-2])



#fib += list
print(fib)
#print(list(map(lambda x : x**3 , fib )))
