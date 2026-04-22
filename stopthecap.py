try:
    word = input("Enter a string: ").lower()
    assert word.isalpha()
except:
    print("Invalid. Please try again")
else:
    while True:
        count = 0
        for char in word:
            if char in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        print(f"Number of vowels: {count}")
        cont = input("Do you want another transaction? (yes/no): ").lower()
        if cont == "yes":
            word = input("Enter a string: ").lower()
            continue
        elif cont == "no":
            break

        
iteration = int(input("Enter number of iterations: "))
total = 0
concat = ""
for i in range(iteration):
    anything = input("Enter anything: ")
    checker = anything.replace(".", "", 1).replace(" ", "")
    if checker.isdigit():
        total += float(anything)
    elif checker.isalpha():
        concat += anything
    else:
        print("Invalid Data Type!")
print(f"""
Total: {total}
Concatenated: {concat}""")