import sys
def phonebook():
    a,b = int(input("Enter number of contacts: ")), 5
    phone_book = []
    print(phone_book)
    for i in range(a):
        print("\nEnter contact %d details :" % (i+1))
        print(" Mandatory to fill")
        temp = []
        for j in range(b):
            if j == 0:
                temp.append(str(input("Enter name: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory.") 

            if j == 1:
                temp.append(int(input("Enter number: ")))
                     
        phone_book.append(temp)
     
    print(phone_book)
    return phone_book
 
def menu():
    
    print("SMARTPHONE DIRECTORY", flush=False)
    print("You can now perform the following operations on this phonebook")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
 
    
    choice = int(input("Please enter your choice: "))
     
    return choice
 
def add_contact(ch):
    
    dip = []
    for i in range(len(ch[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        
    ch.append(dip)
    
    return ch
 
def remove_existing(ch):
    
    x = str(input("Please enter the name of the contact you want to remove: "))
    
     
    temp = 0
    
    for i in range(len(ch)):
        if x == ch[i][0]:
            temp += 1
           
             
            print(ch.pop(i))
            
             
            print("This query has now been removed")
           
             
            return ch
    if temp == 0:
        
        print("Sorry, you have entered an invalid query.\
    Please recheck and try again later.")
         
        return ch
 
def delete_all(ch):
    
    return ch.clear()
 
def search_existing(ch):
    
    choice = int(input("Enter search criteria\n\n\
    1. Name\n2. Number"))
    
     
    temp = []
    check = -1
     
    if choice == 1:
   
        x = str(input("Please enter the name of the contact you want to search: "))
        for i in range(len(ch)):
            if x == ch[i][0]:
                check = i
                temp.append(ch[i])
                 
    elif choice == 2:
    
        x = int(input("Please enter the number of the contact you want to search: "))
        for i in range(len(ch)):
            if x == ch[i][1]:
                check = i
                temp.append(ch[i])
        
    else:
    
        print("Invalid search ")
        return -1
   
     
    if check == -1:
        return -1
       
    else:
        display_all(temp)
        return check
        
 

def display_all(ch):
    if not ch:
   
        print("List is empty: []")
    else:
        for i in range(len(ch)):
            print(ch[i])
 
def thanks():
    print("THANK YOU.")
    print("PLEASE VISIT AGAIN!")
    sys.exit("GOODBYE ")
 
print("Hello dear user, welcome to our smartphone")
print("You may now proceed to explore this.....")
pk = 1
ch = phonebook()
while pk in (1, 2, 3, 4, 5):
    pk = menu()
    if pk == 1:
        ch = add_contact(ch)
    elif pk == 2:
        ch = remove_existing(ch)
    elif pk == 3:
        ch = delete_all(ch)
    elif pk == 4:
        d = search_existing(ch)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif pk == 5:
        display_all(ch) 
    else:
        thanks()
#thankyou
