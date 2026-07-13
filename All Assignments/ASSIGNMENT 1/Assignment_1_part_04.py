# 31. Compare two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("First greater than second:", a > b)

# 32. Check even number
num = int(input("Enter number: "))
print("Is even:", num % 2 == 0)

# 33. Between 10 and 50
num = int(input("Enter number: "))
print("Between 10 and 50:", num >= 10 and num <= 50)

# 34. Check if string equals Python
text = input("Enter a word: ")
print(text == "Python")

# 35. Admin or Superuser
user = input("Enter username: ")
print(user == "Admin" or user == "Superuser")

# 36. not operator
flag = True
print("Original:", flag)
print("Reversed:", not flag)

# 37. Floating point comparison
print(0.1 + 0.2 == 0.3)
print("Due to floating point precision errors")

# 38. Age NOT under 18
age = int(input("Enter age: "))
print("Not under 18:", not(age < 18))

# 39. Positive and odd
num = int(input("Enter number: "))
print("Positive and odd:", num > 0 and num % 2 != 0)

# 40. Compare string lengths
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("First longer than second:", len(s1) > len(s2))