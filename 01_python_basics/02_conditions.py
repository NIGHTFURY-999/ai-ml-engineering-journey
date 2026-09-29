# Exercise 1 - Positive / Negative / Zero
a = int(input("enter an integer: "))

if a > 0:
    print("POSITIVE")
elif a < 0:
    print("NEGATIVE")
else:
    print("Zero")

# Exercise 2 - Even / Odd
a = int(input("enter an integer: "))

if a%2 == 0:
    print("EVEN")
else:
    print("ODD")

# Exercise 3 - Largest of Two Numbers
a = int(input("enter 1st integer: "))
b = int(input("enter 2nd integer: "))

if a>b:
    print(a,"is Larger")
elif a<b:
    print(b,"is Larger")
else:
    print("Both are Equal")    

# Exercise 4 - Grade Calculator
a = int(input("Enter Marks:"))

if a >= 90:
    print("EXCELLENT")
elif a >= 75:
    print("GOOD")
elif a >= 50:
    print("PASS")
else:
    print("FAIL")

# Exercise 5 - Marks Validation
a = int(input("Enter Marks: "))

if a > 100 or a < 0:
    print("INVALID MARKS")
elif a >= 90:
    print("EXCELLENT")
elif a >= 75:
    print("GOOD")
elif a >= 50:
    print("PASS")
else:
    print("FAIL")