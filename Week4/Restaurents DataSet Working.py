import pandas as pd
df = pd.read_csv(r'C:\Users\PMLS\Documents\GitHub\My-Course-AI-Bin\FastFoodRestaurants.csv',delimiter="," )

print(df)
# we are printing data types for each column
print("Data Types are Printing", df.dtypes)
# we are printing dataset information for more clarification
print("DataSet information :", df.info())
# we are printing last three rows from our dataset
print("Printing last three rows :", df.tail(3))
# we are printing first 5 rows
print("Printing first five rows from our dataset: ", df.head(5))
# we are printing summary statistics
print("Now printing summary statistics of our dataset: ",df.describe())
# Now we are counting rows and coloumns
print("Rows and columns are: ", df.shape)
country=df['country']
print("print column name: ")
print(country)
print()
# Now we are accessing multiple columns
my_columns=df[['address','name']]
print("printing two columns: ")
print(my_columns)
print()
# Now we are printing rows using loc function
one_row= df.loc[5]
print("printing  first row from data: ")
print(one_row)
print()
#Selecting a slice of rows using .loc
slicing = df.loc[3:5]
print("#Selecting a slice of rows using .loc")
print(slicing)
print()
#Selecting a single column using .loc
columns = df.loc[:7,'name']
print("#Selecting a single column using .loc")
print(columns)
print()
# Now selecting multiple columns 
multiple_coloumns=df.loc[:8,['address','latitude']]
print("Selecting multiple coloumns: ")
print(multiple_coloumns)
print()

