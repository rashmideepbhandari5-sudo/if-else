# 1. You have a list containing mixed data types represented as strings. Write a Python
# program using a filter() and lambda function to keep only the alphabetic items
# (letters only) and remove any numeric strings from the list."
# items = ['sql', '123', 'python']

items = ['sql', '123', 'python']
filter_item=list(filter(lambda x:x.isalpha(),items))
print(filter_item)



# 2. You are managing an e-commerce inventory database. Given a list of product
# dictionaries, write a Python program using a filter() and lambda function to
# extract and display only the products that are currently in stock (instock: True)
# products = [
#  {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
#  {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':
# False}
# ]


products = [
             {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
             {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':
            False}
       ]
filter_item=list(filter(lambda x:x ['instock']==True,products ))
print(filter_item)




# 3. Given a list of course dictionaries, write a Python program using a lambda function
# to filter and display only those courses that belong to the 'history' genre.
# course = [ {'title': 'Ancient Civilizations', 'genre': 'history'}, {'title': 'Corporate
# Finance', 'genre': 'commerce'}, {'title': 'Modern World History', 'genre': 'history'} ]

course = [ {'title': 'Ancient Civilizations', 'genre': 'history'}, 
          {'title': 'Corporate Finance', 'genre': 'commerce'},
            {'title': 'Modern World History', 'genre': 'history'} ]

file_item=list(filter(lambda x:x ['genre']=='history',course))
print(file_item)

# 4. You have a list of blacklisted domains. Write a Python program using a lambda
# function to filter a list of emails and return only the ones that are considered spam
# those that match any domain in the blacklist.
# emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net',
# ‘shyam.kumar@workcorp.com’]
# blacklist = ('@hooya.com', '@malware.net')


emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net', 'shyam.kumar@workcorp.com']
blacklist = ('@hooya.com', '@malware.net')
filter_item=list(filter(lambda x:x.endswith(blacklist),emails))
print(filter_item)
for mail in filter_item:
    print(mail)





#     5. Applying a 20% discount to all items in a shopping cart:
# price = [100, 50, 200, 75] implement using lambda function

price = [100, 50, 200, 75]
discountrd_price=list(map(lambda x:x-(x*20/100),price))
print(discountrd_price)









# 6. Create a function, skip_two that takes a list as input, and returns a list that: Starts
# with the second element of the input. While skipping every two elements. Does
# not keep any element whose index is greater than 11


def skip_two(lst):
    new_list = []
    for i in range(1, len(lst)):
        if i <= 11 and (i - 1) % 3 == 0:
            new_list.append(lst[i])
    return new_list




# 7. Create a function, remove_at_idx, with the following features:
#  Takes a list as its first argument.
#  Takes a positive index as its second argument.
#  Removes the element at the given index and decreases the index of all
# subsequent elements by one.
#  Returns a new list.


def remove_at_idx(lst, idx):
    new_list = []
    for i in range(len(lst)):
        if i != idx:
            new_list.append(lst[i])
    return new_list






# 8. You are developing a data-cleaning tool for a messaging application. The
# application collects user input which may contain special characters like @, #, !,
# %, etc., which could be problematic during processing or searching. To sanitize
# this input, your task is to replace all special characters with a # symbol, while
# keeping letters and digits unchanged. Write a Python program that:
#  Accepts a string input from the user.
#  Replaces all non-alphanumeric characters (special characters) with #.

s = input("Enter a string: ")
new_str = ""

for i in s:
    if i.isalnum():
        new_str = new_str + i
    else:
        new_str = new_str + "#"

print(new_str)


# . Write a Python program that implements a simple user registration and
# login system with the following requirements: Create a global dictionary called users_db to
# store user information. Implement a register_user(username, password, email) function that:  Checks 
# if the username already exists and returns ‘Username already exists’ if it does  Stores the 
# user's password and email in the database  Returns a success message in the format: Registration'
# ' successful for {username} Implement a login_user(username, password) function that:  Returns ‘User not '
# ''
# found’ if the username doesn't exist  Returns ‘Incorrect password’ if the password is wrong  Returns ‘Welcome back, {username}’ if
# login is successful Test the program by registering three 
# users:  ram with password ‘ram123’ and email ‘ram@email.com’  shyam with password ‘shyam456’ and email ‘shyam@email.com’  hari with password ‘hari231’ and email ‘hari@email.com’



users_db = {}

def register_user(username, password, email):
    if username in users_db:
        return "Username already exists"
    users_db[username] = {"password": password, "email": email}
    return "Registration successful for " + username

def login_user(username, password):
    if username not in users_db:
        return "User not found"
    if users_db[username]["password"] != password:
        return "Incorrect password"
    return "Welcome back, " + username

print(register_user("ram", "ram123", "ram@email.com"))
print(register_user("shyam", "shyam456", "shyam@email.com"))
print(register_user("hari", "hari231", "hari@email.com"))



#   10  Develop a Python program for managing product inventory using a dictionary
# stored in a list.
# 1. Initialize inventory as a list of dictionaries: [{'name': 'Laptop', 'price': 50000,
# 'quantity': 5}]
# 2. Menu options:
#  Add new product (name, price, quantity)
#  View all products in a formatted table
#  Update product details (by product name)
#  Delete a product
#  Calculate total inventory value
#  Exit
#  3. Ensure price and quantity are positive numbers
#  4. Prevent duplicate product names
#  5. Show confirmation messages for all operations

# Inventory Management System

inventory = [
    {'name': 'Laptop', 'price': 50000, 'quantity': 5}
]

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add new product")
    print("2. View all products")
    print("3. Update product")
    print("4. Delete product")
    print("5. Calculate total inventory value")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add new product
    if choice == 1:
        name = input("Enter product name: ")

        # Check duplicate
        found = False
        for item in inventory:
            if item['name'].lower() == name.lower():
                found = True
                break

        if found:
            print("Product already exists!")
        else:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            if price > 0 and quantity > 0:
                inventory.append({'name': name, 'price': price, 'quantity': quantity})
                print("Product added successfully!")
            else:
                print("Price and quantity must be positive.")

    # View products
    elif choice == 2:
        print("\nName\tPrice\tQuantity")
        for item in inventory:
            print(item['name'], "\t", item['price'], "\t", item['quantity'])

    # Update product
    elif choice == 3:
        name = input("Enter product name to update: ")
        for item in inventory:
            if item['name'].lower() == name.lower():
                item['price'] = float(input("Enter new price: "))
                item['quantity'] = int(input("Enter new quantity: "))
                print("Product updated successfully!")
                break
        else:
            print("Product not found.")

    # Delete product
    elif choice == 4:
        name = input("Enter product name to delete: ")
        for item in inventory:
            if item['name'].lower() == name.lower():
                inventory.remove(item)
                print("Product deleted successfully!")
                break
        else:
            print("Product not found.")

    # Total inventory value
    elif choice == 5:
        total = 0
        for item in inventory:
            total += item['price'] * item['quantity']
        print("Total Inventory Value:", total)

    # Exit
    elif choice == 6:
        print("Exiting Inventory System.")
        break

    else:
        print("Invalid choice!")






# 11  11. Build a contact management system using nested data structures.
# 1. Initialize contacts as: [{'name': ’Ram kc’, 'phone': '9801234567', 'email':
# 'ram@email.com'}]
# 2. Menu features:
#  Add contact (name, phone, email)
#  Display all contacts
#  Search contact by name
#  Update contact information
#  Delete contact
#  Sort contacts alphabetically 
#  Exit
# 3. Validate phone number format (10 digits)
# 4. Validate email format (contains @ and.)
# 5. Prevent duplicate contacts


# Contact Management System

contacts = [
    {'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}
]

while True:
    print("\n--- Contact Menu ---")
    print("1. Add contact")
    print("2. Display contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Sort contacts")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Add contact
    if choice == 1:
        name = input("Enter name: ")

        # Check duplicate
        duplicate = False
        for c in contacts:
            if c['name'].lower() == name.lower():
                duplicate = True
                break

        if duplicate:
            print("Contact already exists!")
        else:
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            if len(phone) == 10 and phone.isdigit() and '@' in email and '.' in email:
                contacts.append({'name': name, 'phone': phone, 'email': email})
                print("Contact added successfully!")
            else:
                print("Invalid phone or email format.")

    # Display contacts
    elif choice == 2:
        for c in contacts:
            print(c['name'], "-", c['phone'], "-", c['email'])

    # Search contact
    elif choice == 3:
        name = input("Enter name to search: ")
        for c in contacts:
            if c['name'].lower() == name.lower():
                print(c)
                break
        else:
            print("Contact not found.")

    # Update contact
    elif choice == 4:
        name = input("Enter name to update: ")
        for c in contacts:
            if c['name'].lower() == name.lower():
                c['phone'] = input("Enter new phone: ")
                c['email'] = input("Enter new email: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")

    # Delete contact
    elif choice == 5:
        name = input("Enter name to delete: ")
        for c in contacts:
            if c['name'].lower() == name.lower():
                contacts.remove(c)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")

    # Sort contacts
    elif choice == 6:
        contacts.sort(key=lambda x: x['name'])
        print("Contacts sorted alphabetically!")

    # Exit
    elif choice == 7:
        print("Exiting Contact System.")
        break

    else:
        print("Invalid choice!")
