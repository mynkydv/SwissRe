
def show_help(): 
    # print instructions on how to use app
    print("What should we pick up at the store")    
    print("""
    Enter 'DONE' to stop adding items
    Enter 'SHOW' to stop adding items
    Enter 'HELP' to stop adding items
    """)

# print out the shopping list
# print(shopping_list)
def show_list():
    print("Here is your list")
    for item in shopping_list:
        print(item)

def add_item_to_list(new_item):            
       # add new items to our list
        shopping_list.append(new_item)
        print("Added {}. Now list has {} items".format(new_item, len(shopping_list)))

# Make a list to hold items
shopping_list = []


# Ask for new items
choice = 'CONT'
while True:
    new_item = input(">")

    # be able to quit the app
    if(new_item.upper() =='DONE'):
        break
    elif(new_item.upper() == 'HELP'):
        show_help()
    elif(new_item.upper() == 'SHOW'):
        show_list()
    # Add new item to list
    add_item_to_list(new_item)

show_list()
 



