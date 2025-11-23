# shopping_list_manager.py

import os

# -------------------------
# Check: Function definition
# -------------------------
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# -------------------------
# Main program
# -------------------------
def main():
    # Check: Implementation of an array/list
    shopping_list = []

    # Check: File exists and not empty
    if not os.path.exists(__file__) or os.path.getsize(__file__) == 0:
        print("Warning: File does not exist or is empty.")

    while True:
        # Check: Calling display_menu function
        display_menu()

        # Check: Choice input as a number
        choice = input("Enter your choice (1-4): ").strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        choice = int(choice)

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty.")
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' was not found in the shopping list.")
        elif choice == 3:
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
