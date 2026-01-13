import math
import sys

# ===== Secure Login System =====
correct_password = "Admin@123"     # set your correct password
admin_name = "IT Support Team"     # person to contact

max_attempts = 3
attempts = 0

print("===== Secure Login System =====")

while attempts < max_attempts:
    password = input("Enter your password: ")

    if password == correct_password:
        print("✅ Login successful. Welcome!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f" Wrong password. Attempts left: {remaining}")

        if remaining == 0:
            print("\n WARNING: Too many failed attempts!")
            print("Your account is temporarily locked.")
            print(f"Please contact {admin_name} to recover your password.")
            sys.exit()   # Exit program if password fails 3 times


# ===== Smart Calculator =====
print("\n===== Smart Calculator =====")

def perform_calculation(num1, num2, choice):
    """Performs calculation based on choice"""
    if choice == "1":
        return num1 + num2
    elif choice == "2":
        return num1 - num2
    elif choice == "3":
        return num1 * num2
    elif choice == "4":
        return num1 / num2 if num2 != 0 else "Error: Cannot divide by zero"
    elif choice == "5":
        return num1 ** num2
    elif choice == "6":
        return num1 % num2
    elif choice == "7":
        return math.sqrt(num1) if num1 >= 0 else "Error: Square root of negative number"
    elif choice == "8":
        return num1 // num2 if num2 != 0 else "Error: Cannot divide by zero"
    elif choice == "9":
        return math.sin(math.radians(num1))
    elif choice == "10":
        return math.cos(math.radians(num1))
    elif choice == "11":
        return math.tan(math.radians(num1))
    elif choice == "12":
        return math.log(num1) if num1 > 0 else "Error: log undefined for <=0"
    elif choice == "13":
        return abs(num1)
    else:
        return "Invalid operation"


while True:
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulus (%)")
    print("7. Square Root (√)")
    print("8. Floor Division (//)")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Logarithm (ln)")
    print("13. Absolute value (abs)")

    choice = input("Enter choice (1-13): ").strip()

    if choice not in [str(i) for i in range(1, 14)]:
        print("Invalid choice! Please select 1-13.")
        continue

    if choice in ['1','2','3','4','5','6','8']:
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
    else:
        while True:
            try:
                num1 = float(input("Enter the number: "))
                num2 = 0
                break
            except ValueError:
                print("Invalid input. Please enter numeric value.")

    result = perform_calculation(num1, num2, choice)
    print("\nResult:", result)

    while True:
        exit_choice = input("\nDo you want to exit? (Y/N): ").strip().upper()
        if exit_choice == 'Y':
            print("Calculator closed. Thank you ")
            sys.exit()
        elif exit_choice == 'N':
            break
        else:
            print("Please enter Y or N only.")
