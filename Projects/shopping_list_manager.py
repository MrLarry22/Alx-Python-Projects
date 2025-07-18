def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1': #Step 2:add item
            item=input("Enter the item to add:")# Prompt for and add an item
            shopping_list.append(item)
            print(f" '{item}'has been added.")

        elif choice == '2':  #Step 2:remove item
            item=input("Enter the item to remove:")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f" '{item}'has been removed.")
            else:
                print(" '{item}'not found in the shopping list.")
            
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Current Shopping list:")
                for i,item in enumerate(shopping_list, start=1):
                    print(f"{i}.{item}")
                else:
                    print("Your shopping list is empty.")
        elif choice == '4':#Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()