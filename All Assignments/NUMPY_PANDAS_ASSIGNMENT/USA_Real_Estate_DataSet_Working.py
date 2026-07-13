
import numpy as np

brokered_by, status , price ,bed,bath, city = np.genfromtxt('E:\DataSets_AI_Course\RealEstate-USA.csv', delimiter=',', usecols=(0,1,2,3,4,7), unpack=True, dtype=None,skip_header=1)

print(brokered_by)
print(status)
print(price)
print(bed)
print(bath)
print(city)
price = np.nan_to_num(price, nan=1)

# USA REALESTATE price  - statistics operations
print("USA REALESTATE Price mean: " , np.mean(price))
print("USA REALESTATE Price average: " , np.average(price))
print(" USA REALESTATE Price std: " , np.std(price))
print("USA REALESTATE Price mod: " , np.median(price))
print("USA REALESTATE Price percentile - 25: " , np.percentile(price,25))
print("USA REALESTATE Price percentile  - 75: " , np.percentile(price,75))
print("USA REALESTATE Price percentile  - 3: " , np.percentile(price,3))
print("USA REALESTATE Price min : " , np.min(price))
print("USA REALESTATE Price max : " , np.max(price))

# USA REALESTATE price  - maths operations
print("USA REALESTATE Price square: " , np.square(price))
print("USA REALESTATE Price sqrt: " , np.sqrt(price))
print("USA REALESTATE Price pow: " , np.power(price.astype(float), price))
print("USA REALESTATE Price abs: " , np.abs(price))



# Perform basic arithmetic operations
addition = bed+bath 
subtraction = bed-bath
multiplication = bed*bath
division = bed/bath

print(" USA REALESTATE bed + bath - Addition:", addition)
print(" USA REALESTATE bed - bath - Subtraction:", subtraction)
print(" USA REALESTATE bed * bath  - Multiplication:", multiplication)
print(" USA REALESTATE bed / bath  - Division:", division)


#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("USA REALESTATE Price - div - pie  - Sine values:", sine_values)
print("USA REALESTATE Price - div - pie Cosine values:", cosine_values)
print("USA REALESTATE Price - div - pie Tangent values:", tangent_values)

print("USA REALESTATE Price - div - pie  - Exponential values:", np.exp(pricePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("USA REALESTATE Price - div - pie  - Natural logarithm values:", log_array)
print("USA REALESTATE Price - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("USA REALESTATE Price - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print("USA REALESTATE Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("USA REALESTATE Price - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("USA REALESTATE Price - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("USA REALESTATE Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#USA REALESTATE bed Plus bath - 2 dimentional arrary
D2bedbath = np.array([bed,
                  bath])

print ("USA REALESTATE bed Plus bath - 2 dimentional arrary - " ,D2bedbath)

# check the dimension of array1
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - dimension" , D2bedbath.ndim) 

# return total number of elements in array1
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - total number of elements" ,D2bedbath.size)

# return a tuple that gives size of array in each dimension
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - gives size of array in each dimension" ,D2bedbath.shape)

# check the data type of array1
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - data type" ,D2bedbath.dtype) 

# Splicing array
D2bedbathSlice=  D2bedbath[:1,:5]
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2bedbathSlice)
D2bedbathSlice2=  D2bedbath[:1, 4:15:4]
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - Splicing array - D2LongLat[:1, 4:15:4] " , D2bedbathSlice2)


# Indexing array
D2bedbathSliceItemOnly=  D2bedbathSlice[0,1]
print("USA REALESTATE bed Plus Lat - 2 dimentional arrary - Index array - D2bedbathSlice[1,5] " , D2bedbathSliceItemOnly)
D2bedbathSlice2ItemOnly=  D2bedbathSlice2[0, 2]
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - index array - D2bedbathSlice2[0, 2] " , D2bedbathSlice2ItemOnly)


for elem in np.nditer(D2bedbath):
    print(elem)

for index, elem in np.ndenumerate(D2bedbath):
    print(index, elem)


# 2 x 149 ========>>>>> 1  x 298 - reshape
D2bedbath1TO298 = np.reshape(D2bedbath, (1,-1))
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - np.reshape(D2bedbath, (1, 298)) : " , D2bedbath1TO298)
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - np.reshape(D2bedbath, (1, 298)) : Size " , D2bedbath1TO298.size)
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - np.reshape(D2bedbath, (1, 298)) : ndim " , D2bedbath1TO298.ndim)
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - np.reshape(D2bedbath, (1, 298)) : shape " , D2bedbath1TO298.shape)
print("USA REALESTATE bed Plus bath - 2 dimentional arrary - np.reshape(D2bedbath, (1, 298)) : ndim " , D2bedbath1TO298.ndim)

print()
