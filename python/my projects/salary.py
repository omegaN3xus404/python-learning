name, income_data = input("Enter your name and income (separated by space): ").split()
expenses_name_number = []  # List to store expense details

# Open the file to check if the data exists
with open("savedfiles.txt", "r") as f:
    readed_file = f.read()  # Read the entire content of the file

# Check if the name and income already exist in the file
if f"name:{name}   income:{income_data}" in readed_file:
    print("Your income and expenses are already saved.")
    
    # Ask if the user wants to update their data
    save_again = input("If you want to make changes to your income or expenses, type 'yes' or 'no': ")
    
    if save_again.lower() == "yes":
        # Open file in append mode to add new data
        with open("savedfiles.txt", "a") as f:
            expenses_number = int(input("How many expenses do you have? "))
            
            # Collect expenses from the user
            for _ in range(expenses_number):
                expenses_name, expenses_amount = input("Enter your expense name and amount (separated by space): ").split()
                expenses_name_number.append((expenses_name, expenses_amount))
                
            # Write expenses to the file after collecting all of them
            for expense in expenses_name_number:
                f.write(f"expenses_name: {expense[0]}   expenses_amount: {expense[1]}\n")

    else:
        print("Your income and expenses are the same.")

else:
    # If the name and income don't exist, add them to the file
    with open("savedfiles.txt", "a") as f:
        f.write(f"name:{name}   income:{income_data}\n")
        
        # Collect expenses from the user
        expenses_number = int(input("How many expenses do you have? "))
        
        # Collect all expenses
        for _ in range(expenses_number):
            expenses_name, expenses_amount = input("Enter your expense name and amount (separated by space): ").split()
            expenses_name_number.append((expenses_name, expenses_amount))
        
        # Write all expenses to the file after collection
        for expense in expenses_name_number:
            f.write(f"expenses_name: {expense[0]}   expenses_amount: {expense[1]}\n")



