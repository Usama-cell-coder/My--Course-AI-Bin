
# Q1
squares = [x**2 for x in range(21) if x % 2 == 0]
print("Q1:", squares)

# Q2
nums = [3, 1, 4, 1, 5, 9]
sorted_nums = sorted(nums)
print("Q2:", sorted_nums)

# Q3
lst = [1,2,2,3,4,3,5]
seen = []
for x in lst:
    if x not in seen:
        seen.append(x)
print("Q3:", seen)

# Q4
nested = [[1,2],[3,4],[5]]
flat = [x for sub in nested for x in sub]
print("Q4:", flat)

# Q5
names = ['alice','Bob','charlie','DAVID']
print("Q5:", sorted(names, key=str.lower))

# Q6
a = [10,20,30,40,50,60]
a[2:5] = [100,200]
print("Q6:", a)

# Q7
lst2 = [7,1,7,3,7]
indices = [i for i,x in enumerate(lst2) if x == 7]
print("Q7:", indices)

# Q8
lst3 = [1,2,2,3,4,4,5]
unique = [x for x in lst3 if lst3.count(x) == 1]
print("Q8:", unique)

# Q9
lst4 = [1,2,3,4]
rotated = lst4[-1:] + lst4[:-1]
print("Q9:", rotated)

# Q10
lst5 = [1,2,3,4,5]
even = [x for x in lst5 if x % 2 == 0]
odd = [x for x in lst5 if x % 2 != 0]
print("Q10 Even:", even)
print("Q10 Odd:", odd)