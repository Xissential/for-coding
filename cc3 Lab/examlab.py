while True:
    print("\n===== Display MAIN MENU =====")
    print("1. INPUT AND OUTPUT")
    print("2. STRING AND NUMBER FORMATTING")
    print("3. IF-ELSE")
    print("4. LOOPS(FOR)")
    print("5. EXCEPTION HANDLING")
    print("6. EXIT PROGRAM")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\n--- INPUT AND OUTPUT ---")

        name = input("Enter name: ")
        try:
            age = int(input("Enter age (Must be a number): "))
            if age <= 0:
                print(" ERROR! Age must be a positive number.")
                continue
        except ValueError:
            print(" ERROR! Age must be a number.")
            continue

        gender = input("Enter gender: ")
        section = input("Enter section: ")
        subject = input("Enter subject: ")

        print("\n--- COLLECTED DATA ---")
        print("Name: " + name)
        print("Age: " + str(age))
        print("Gender: " + gender)
        print("Section: " + section)
        print("Subject: " + subject)

    elif choice == "2":
        print("\n--- STRING AND NUMBER FORMATTING ---")
        user_input = input("Enter a number or a string: ")

        try:
            num = float(user_input)
            print("\nInput detected as NUMBER.")
            print("Floor:", int(num // 1))
            print("Ceil:", int(-(-num // 1)))
            print("Round:", round(num))
        except ValueError:
            print("\nInput detected as STRING.")
            print("Uppercase version:", user_input.upper())
            print("Lowercase version:", user_input.lower())
            print("Capitalize version:", user_input.capitalize())
            print("Length of the string:", len(user_input))

    elif choice == "3":
        print("\n--- IF-ELSE ---")
        user_input = input("Enter a number: ")

        try:
            num = int(user_input)

            if num == 0:
                print("The number is ZERO.")
            elif num % 2 == 0:
                print("The number is EVEN.")
            else:
                print("The number is ODD.")

        except ValueError:
            print(" ERROR! Please enter a valid number.")

    elif choice == "4":
        print("\n--- LOOPS(FOR) ---")
        user_input = input("Enter a number: ")

        try:
            num = int(user_input)
            print("\nMultiplication Table for " + str(num) + ":")
            for i in range(1, 11):
                print(str(num) + " x " + str(i) + " = " + str(num * i))
        except ValueError:
            print(" ERROR! Please enter a valid number.")

    elif choice == "5":
        print("\n--- EXCEPTION HANDLING ---")
        user_input = input("Enter a floating-point number: ")

        try:
            float_num = float(user_input)
            int_num = int(float_num)
            print("Successful conversion of the Float into an Integer! " + str(int_num))

        except ValueError:
            print(" ValueError: Input is not a valid floating-point number.")

        except Exception as e:
            print(" Unexpected error occurred: " + str(e))

    elif choice == "6":
        print("Shutdown. Congratulations!")
        break

    else:
        print("Invalid choice. Please select 1–6.")