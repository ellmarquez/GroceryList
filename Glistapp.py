
print ("""Enter A to add to your list,
Enter P to print your list,
Enter DELETE to clear your list,
Leave blank and press enter to exit""") 

userinput= input()
userinput =userinput.lower()

if userinput == 'p':
     with open("grocerylist.txt") as temp:
        list=temp.read()
        print ("--------\n" + list)
elif userinput== 'a':
   print ("What would you like to add?")
   glist=input()
   with open("grocerylist.txt", "a") as wtemp:
       wtemp.write(glist + "\n")
   with open("grocerylist.txt") as temp:
        list=temp.read()
        print ("--------\n"+ list)
elif userinput =='delete':
    print ("Your list has been deleted.")
    open('grocerylist.txt','w').close() 
else:
    print ("Goodbye ")

   
