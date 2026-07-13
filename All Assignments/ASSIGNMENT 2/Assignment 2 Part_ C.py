

# Q1
print("Q1:", {1,2,3} - {2,3,4})

# Q2
set1, set2, set3 = {1,2,3}, {2,3,4}, {3,4,5}
print("Q2:", set1 & set2 & set3)

# Q3
sentence = "Hello world hello"
print("Q3:", set(sentence.lower().split()))

# Q4
lst = [3,1,2,3,2]
print("Q4:", sorted(set(lst)))

# Q5
print("Q5:", {1,2} < {1,2,3})

# Q6
print("Q6:", {x*x for x in range(1,16) if x % 3 == 0})

# Q7
lst = [1,2,2,3,3,3]
print("Q7:", len(lst) - len(set(lst)))

# Q8
vowels = set("aeiou")
text = "hello world"
print("Q8:", ''.join([c for c in text if c not in vowels]))

# Q9
print("Q9:", {1,2,3} ^ {3,4,5})

# Q10
print("Q10:", set("listen") == set("silent"))