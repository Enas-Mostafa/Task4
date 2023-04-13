list=[3,2,9,11,7]
m=len(list)
dict={}
def hash_func(l,m):
    for v in list:  
        f=v%m
        dict[v]=f 
    return dict
hash_func(list,m)
def adding_element():
    key=int(input("Enter the key:"))
    value=int(input("Enter the value:"))
    dict[key]=value
    return dict
def updating():    
    key=int(input('Enter the key:'))
    dict[key]=int(input("Enter the new value:"))
    return dict
def deleting():
    key=int(input("Enter the key:"))
    del dict[key]
    return dict
def searching():
    key=int(input("Enter the key:"))
    return dict[key]
def printing_elements():
    for key in dict:
        print(key,':',dict[key])

print("choose 1 for hash table\nchoose 2 for adding a new element\nchoose 3 to update a value\nchoose 4 to delete an element\nchoose 5 to search for an element\nchoose 6 to print all elements")
choice=int(input("Enter your choice:"))
if choice==1:
    print(hash_func(list,m))
elif choice==2:
    print(adding_element())
elif choice==3:
    print(updating())
elif choice==4:
    print(deleting())
elif choice==5:
    print(searching())
elif choice==6:
    printing_elements()
else:
    print("Enter a right choice")
    
