n=int(input("enter no of terms: "))
fib=[]
fib.append(0)
fib.append(1)
list = [fib[k-1]+fib[k-2] for k in range(2,n)]
#fib += list
#print(fib)
#print(list(map(lambda x : x**3 , fib )))
