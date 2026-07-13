
# Q1
text = "hello world hello"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print("Q1:", freq)

# Q2
d = {'a':1,'b':2,'c':3}
print("Q2:", {v:k for k,v in d.items()})

# Q3
d1 = {'a':1,'b':2}
d2 = {'b':3,'c':4}
print("Q3:", {**d1, **d2})

# Q4
words = ["apple","banana","apricot"]
grouped = {}
for word in words:
    grouped.setdefault(word[0], []).append(word)
print("Q4:", grouped)

# Q5
d = {'a':10,'b':60,'c':30}
print("Q5:", {k:v for k,v in d.items() if v > 50})

# Q6
nested = {'a':{'b':{'c':10}}}
print("Q6:", nested.get('a',{}).get('b',{}).get('c'))

# Q7
print("Q7:", {x: x**3 for x in range(1,11)})

# Q8
d = {'a':10,'b':50,'c':30}
print("Q8:", max(d, key=d.get))

# Q9
keys = ['a','b','c']
values = [1,2,3]
print("Q9:", dict(zip(keys, values)))

# Q10
d = {'a':1,'b':None,'c':2}
print("Q10:", {k:v for k,v in d.items() if v is not None})