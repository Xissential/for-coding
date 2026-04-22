try:
    file = open("filename.txt")
except Exception:
    print("error")
# 2
try:
    raise NameError("Hello")
except NameError:
    print("An exception is invoked")
# 3
try:
  print("This is the try block!")
except:
  print("There is an Error!")
else:
  print("No Error Found")
# 4
try:
    file = open('filename.txt2')
except Exception:
	print('Error')
else:
	print('No Error')
finally:
	print("Finally")
# 5
try:
	a = 19
	if a <=17:
		raise Exception
except Exception:
	print("Error:")
else:
	print("No Error")
finally:
	print("Finally")
# 6
x = 600
y =0
try:
    print(x/y)
except ZeroDivisionError:
      print("error division by zero")
# 7
try: 
    obj = None
    len(obj)
except TypeError:
    print("Error: Object is of NoneType, cannot calculate length.")
# 8
try :
    arr = [10, 20, 30]
    print(arr[10])
except IndexError:
     print("\nOopps! Index out of bounds for the list.")
