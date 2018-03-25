N=int(input("Enter N : "))

def grid(X,Y,Z):
    print([(a,b,c) for a in range(0,X+1) for b in range(0,Y+1) for c in range(0,Z+1) if a+b+c!=N]) 
print("Result : \n")    
grid(3,3,5)    
