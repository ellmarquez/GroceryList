def add_item():
    while True:
    print('Enter your item:(Done to quit)')
    item=input()
    list.append(item)
    if item=='Done':
        del list[-1]
        list[-1] = 'and '+list[-1]
        finallist=', '.join(list)
        print(finallist +' was added to your list')
        break


def remove_list():
    print ('What would you like to remove?')
    remove=input()
    for i in list:
        list.remove(i)
        print ('Your updated list is: '+ list )
    else:
        print ('That item is not on your list.')

print('Welcome type add to add an item, remove to remove an item or list to see your list:')
pick = input()
if pick.lower() == list:
 print("Your list is as follows:" + list )
#elif pick.lower()==remove:
#    remove_list
#elif pick.lower()==list:
#    print(list)
#else:
#    "You did not enter a valid option:"
#   break 

