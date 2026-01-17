# Importing datetime module to get today's date
from datetime import date

# Taking user input for name
name = input("Enter your name:  ")

# Taking user input for internship role
role = input("Enter your internship role:  ")

# Getting today's date
today_date = date.today()

# Printing the output using variables
print("\n--- Internship Details ---")
print("Name:", name)
print("Internship Role:", role)
print("Today's Date:", today_date)