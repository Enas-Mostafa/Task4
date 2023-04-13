list=[1,2,3,4,5,6]
m=len(list)
dict={}
def hash_func(l,m):
    for v in list:  
        f=v%m
        dict[v]=f 
    return dict
print(hash_func(list,m))