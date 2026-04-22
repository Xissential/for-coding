# while loop
a = 4
while a<8:
    print(a, end="\n")
    a += 1

# Example ulit
number = int(input("Enter a number: "))
total = 0
while number != 0:
    total += number
    number = int(input("Enter a number: "))
print('The sum is', total)

#break statement while loop
ans = "YES"
while ans.upper()=="YES":
    num = input("Enter a number: ")
    print("The number is: " + num)
    ans = input("Enter another? (YES/NO): ")
    if ans.upper()=="NO":
        print("End of program!")
        break

#example bro
i= 1
while i < 9:
    print(i)
    if i == 3:
        break
    i += 1
#example hehe
x = 0
courses = ["BSCS", "BSIT", "BSIS"]
while(x<len(courses)):
    print(courses[x])
    x += 1










