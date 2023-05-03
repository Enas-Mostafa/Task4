list = [3, 2, 9, 11, 7]
m = len(list)
dict = {}

def hash_func(list, m):
    for v in list:
        f = v % m
        
        dict[f] = [v]
    return dict

choice = input("Choose one of the following options: \n1- to construct the hash table \n2- Add a new element to the hash table\n3- Update a value of a certain key\n4- Delete an element from the hash table\n5- Search for an element in the hash table\n6- Print all elements with their key of the hash table.\n")
if choice=="1":
    print(hash_func(list, m))

elif choice == "2":
    hash_func(list, m)
    new_element = int(input("Enter the new element: "))
    key = new_element % len(list)
    
    dict[key] = [new_element]
    print("New element added successfully!")
    print(dict)
    
    
    
elif choice == "3":
    print(hash_func(list, m))
    key_to_update = int(input("Enter the key to update: "))
    if key_to_update in dict:
        new_value = int(input("Enter the new value: "))
        dict[key_to_update] = new_value
        print("Value updated successfully!")
        print(dict)
    else:
        print("Key not found in hash table.")
        
elif choice == "4":
    print(hash_func(list, m))
    element_to_delete = int(input("Enter the element to delete: "))
    key_of_element = element_to_delete % len(list)
    if key_of_element in dict and element_to_delete in dict[key_of_element]:
        dict[key_of_element].remove(element_to_delete)
        print("Element deleted successfully!")
        print(dict)
    else:
        print("Element not found in hash table.")
        
elif choice == "5":
    print(hash_func(list, m))
    search_element = int(input("Enter the element to search for: "))
    search_key = search_element % len(list)
    if search_key in dict and search_element in dict[search_key]:
        print(f"{search_element} found at key {search_key}.")
    else:
        print(f"{search_element} not found in hash table.")
        
elif choice == "6":
    hash_func(list, m)
    print("Hash table:")
    for key, values in dict.items():
        print(f"Key {key}: {values}")
        
else:
    print("Invalid choice. Please choose a valid option.")
