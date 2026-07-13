# 11. Integer and float type
age = 22
height = 5.9
print(type(age))
print(type(height))

# 12. Complex number
c = 3 + 4j
print(c)
print(type(c))

# 13. Boolean variable
is_python_fun = True
print(is_python_fun)

# 14. Assign multiple variables in one line
a, b, c = 10, 20, 30
print(a, b, c)

# 15. Assign same value to multiple variables
x = y = z = 100
print(x, y, z)

# 16. Numeric input converted to float
num = float(input("Enter a number: "))
print("Float value:", num)

# 17. Convert string "100" to int
s = "100"
num = int(s)
print(num, type(num))

# 18. Complex number real part
c = 5 + 7j
print("Real part:", c.real)

# 19. Length of paragraph
paragraph = "Python is a powerful programming language used in AI, ML, and data science."
print("Length:", len(paragraph))

# 20. Swap without third variable
a = 5
b = 10
a, b = b, a
print("a:", a, "b:", b)