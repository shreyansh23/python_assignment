def correction_string(string):
    
    string=string.replace('.','. ')
    while '  ' in string:
        string=string.replace('  ',' ')
    string=string.lstrip()    
        
    print ( string) 

x=input("enter any string \n")
correction_string(x)

