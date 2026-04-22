weeksalary = 0 #while loop
dayofweek = 1
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
while(True):
  if(week[dayofweek] == "Sunday"):
    print("Week Over, Its Holiday!!")
    break
  weeksalary += 2000
  dayofweek += 1
print(weeksalary)

#for loop
names = ["Alexis", "Angel", "Amber"]
print(names)
#ex
for a in range(10,20):
    print(a)
#ex
fruit= ["Apple", "Banana", "Cherry"]
for index in range(len(fruit)):
   print('current fruit:', fruit[index])
#ex
string = "Hello World"
for x in string:
   print(x)
#ex
lis_of_list = [[1,2,3], [4,5,6], [7,8,9]]
for list in lis_of_list:
    for x in list:
        print(x,end="")
#range start, stop, step
for i in range(5):
    print(i)
for t in range(1,10):
    print(t)
for s in range(1,10,2):
    print(s)
    #else statement in for loop
for p in range(6):
    print(p)
else:
    print("Finally finished!")
    #continue statement in for loop
for m in range(6):
    if m == 3:
        continue
    print(m)
    #break statement in for loop
for n in range(6):
    if n == 3:
        break
    print(n)
    #pass statement in for loop
for k in range(6):
    if k == 3:
        pass
    print(k) 
  #ex
strval = "Alexis Cartagena"
for i in strval:
    if i=="g":
        pass
    else: 
        print(i, end="") 
#ex
formula = "860+390-89=1161"
for val in formula:
    if val not in '89':
        print(val,end= " ")