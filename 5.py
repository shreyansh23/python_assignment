my_list=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
#my_list.sort()
list1=[]
list2=[]
list3=[]
for word in my_list:
    if word[0]=='x':
        list1.append(word)
    else:
        list2.append(word)    
list1.sort()
list2.sort()
list3=list1+list2
print (list3)

