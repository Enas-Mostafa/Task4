list = [3, 2, 9, 11,7]
m = len(list)
dict = {}

def hash_func(l, m):
    for v in list:
        f = v % m
        dict[f] = [v]
    return dict
print(hash_func(list, m))
