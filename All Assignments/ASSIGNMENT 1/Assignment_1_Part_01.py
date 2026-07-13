# 1. Print Hello World and name
print("Hello, World!")
print("Usama")

# 2. Favorite color
color = input("Enter your favorite color: ")
print("Your favorite color is", color)

# 3. Three words separated by hyphen
print("Python", "is", "fun", sep="-")

# 4. Birth year to age
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print("Your age is:", age)

# 5. Sum of 5 + 5
print("The sum of 5 and 5 is", 5 + 5)

# 6. Using end parameter
print("Hello", end=" ")
print("World")

# 7. Join two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Joined string:", s1 + s2)

# 8. Greeting in uppercase
name = input("Enter your name: ")
print(("Welcome, " + name + "!").upper())

# 9. City and Country format
city = input("Enter your city: ")
country = input("Enter your country: ")
print(city + ", " + country)

# 10. Fix string + integer error
num = 10
print("The number is " + str(num))