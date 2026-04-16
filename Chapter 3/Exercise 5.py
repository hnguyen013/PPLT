def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Division by zero error")
        return None
    return a / b

def show_menu():
    print("\n--- Pocket Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting program...")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter a: "))
                b = float(input("Enter b: "))
            except:
                print("Invalid input! Please enter numbers.")
                continue

            if choice == '1':
                print("Result:", add(a, b))
            elif choice == '2':
                print("Result:", subtract(a, b))
            elif choice == '3':
                print("Result:", multiply(a, b))
            elif choice == '4':
                result = divide(a, b)
                if result is not None:
                    print("Result:", result)
        else:
            print("Invalid choice! Please choose from 1 to 5.")

if __name__ == "__main__":
    main()