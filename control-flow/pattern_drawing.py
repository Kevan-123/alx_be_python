# Ask the user for the size of the square pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use while loop for rows
while row < size:
    # Use for loop to print '*' in a row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after a row is complete
    row += 1
