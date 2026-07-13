
# Q1
t = tuple([1,2,3,4])
a,b,c,d = t
print("Q1:", a,b,c,d)

# Q2
t2 = (('a',1),('b',2),('c',3))
print("Q2:", [x[1] for x in t2])

# Q3
def stats(lst):
    return sum(lst), min(lst), max(lst)

print("Q3:", stats([1,2,3,4]))

# Q4
print("Q4:", list((1,2,3) + (4,5)))

# Q5
t3 = (1,2,2,3,3,3)
print("Q5:", max(set(t3), key=t3.count))

# Q6
print("Q6:", sorted((1,2,3)) == sorted((3,2,1)))

# Q7
t6 = (1,2,3,4,5,6)
print("Q7:", t6[-3:])

# Q8
print("Q8:", (1,2) * 3)

# Q9
t8 = ((1,2),(3,4))
print("Q9:", tuple(x for sub in t8 for x in sub))

# Q10
p1 = (2,3)
p2 = (5,7)
print("Q10:", abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))