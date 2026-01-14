import math
import sys

# ===== Secure Login System =====
correct_password = "Admin@123"
admin_name = "IT Support Team"
max_attempts = 3
attempts = 0

print("===== Secure Login System =====")

while attempts < max_attempts:
    password = input("Enter your password: ")

    if password == correct_password:
        print(" Login successful. Welcome!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f" Wrong password. Attempts left: {remaining}")

        if attempts == max_attempts:
            print("\n WARNING: Too many failed attempts!")
            print("Your account is temporarily locked.")
            print(f"Please contact {admin_name} to recover your password.")
            sys.exit()

# ===== Smart Calculator =====

many_allowed = ['1','2','3']  # unlimited numbers
two_required = ['4','5','6','8']  # exactly 2 numbers
one_required = ['7','9','10','11','12','13']  # exactly 1 number

def perform_calculation(numbers, choice):
    if choice == "1":  # Addition
        return sum(numbers)
    elif choice == "2":  # Subtraction
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        return result
    elif choice == "3":  # Multiplication
        result = 1
        for n in numbers:
            result *= n
        return result
    elif choice == "4":  # Division
        return numbers[0] / numbers[1] if numbers[1] != 0 else "Error: Cannot divide by zero"
    elif choice == "5":  # Power
        return numbers[0] ** numbers[1]
    elif choice == "6":  # Modulus
        return numbers[0] % numbers[1]
    elif choice == "7":  # Square root
        return math.sqrt(numbers[0]) if numbers[0] >= 0 else "Error: Negative number"
    elif choice == "8":  # Floor division
        return numbers[0] // numbers[1] if numbers[1] != 0 else "Error: Cannot divide by zero"
    elif choice == "9":  # Sine
        return math.sin(math.radians(numbers[0]))
    elif choice == "10":  # Cosine
        return math.cos(math.radians(numbers[0]))
    elif choice == "11":  # Tangent
        return math.tan(math.radians(numbers[0]))
    elif choice == "12":  # Log
        return math.log(numbers[0]) if numbers[0] > 0 else "Error: log undefined"
    elif choice == "13":  # Absolute
        return abs(numbers[0])
    else:
        return "Invalid operation"

# ===== MAIN CALCULATOR LOOP =====

while True:
    print("\n===== Smart Calculator =====")
    print("1. Addition (+) [many]")
    print("2. Subtraction (-) [many]")
    print("3. Multiplication (*) [many]")
    print("4. Division (/) [2 only]")
    print("5. Power (**) [2 only]")
    print("6. Modulus (%) [2 only]")
    print("7. Square Root (√) [1 only]")
    print("8. Floor Division (//) [2 only]")
    print("9. Sine (sin) [1 only]")
    print("10. Cosine (cos) [1 only]")
    print("11. Tangent (tan) [1 only]")
    print("12. Logarithm (ln) [1 only]")
    print("13. Absolute value (abs) [1 only]")

    choice = input("Enter choice (1-13): ").strip()

    if choice not in [str(i) for i in range(1,14)]:
        print(" Invalid choice. Try again.")
        continue

    # Determine number of values required
    while True:
        user_input = input("Enter numbers separated by comma: ")
        try:
            numbers = [float(x.strip()) for x in user_input.split(",")]

            if choice in many_allowed and len(numbers) < 2:
                print("Enter at least 2 numbers.")
                continue
            elif choice in two_required and len(numbers) != 2:
                print("You must enter exactly 2 numbers.")
                continue
            elif choice in one_required and len(numbers) != 1:
                print("You must enter exactly 1 number.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter numbers only.")

    # Perform calculation
    result = perform_calculation(numbers, choice)
    print("\n Result:", result)

    # Ask user if they want to exit
    while True:
        exit_choice = input("\nDo you want to exit? (Y/N): ").strip().upper()
        if exit_choice == 'Y':
            print("Calculator closed. Thank you")
            sys.exit()
        elif exit_choice == 'N':
            print("Continuing calculator...\n")
            break
        else:
            print("Please enter Y or N only.")
