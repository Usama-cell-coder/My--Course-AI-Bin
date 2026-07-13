# 21. Area of rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle:", area)

# 22. Power calculation
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Result:", a ** b)

# 23. Division vs floor division
print("Division:", 10 / 3)
print("Floor Division:", 10 // 3)

# 24. Modulus
print("Remainder:", 25 % 4)

# 25. Average of five numbers
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))
n4 = float(input("Enter number 4: "))
n5 = float(input("Enter number 5: "))
avg = (n1 + n2 + n3 + n4 + n5) / 5
print("Average:", avg)

# 26. Minutes to hours and minutes
minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining = minutes % 60
print("Hours:", hours, "Minutes:", remaining)

# 27. Area of circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area of circle:", area)

# 28. Cube of a number
num = int(input("Enter number: "))
print("Cube:", num ** 3)

# 29. PEMDAS demonstration
result = 10 + 5 * 2
print("Result:", result)

# 30. Simple Interest
P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
T = float(input("Enter time: "))
SI = (P * R * T) / 100
print("Simple Interest:", SI)