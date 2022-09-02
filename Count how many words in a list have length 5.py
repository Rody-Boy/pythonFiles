mylist =['obedient', 'fired', 'large', 'tired', 'admired']
def find(mylist):
    find= 0
    for f in mylist: 
    
        if len(f) == 5: 
            find = find + 1
    return find

print (find(mylist))
