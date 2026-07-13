# Reading USA REALESTATE dataset using pandas 
import pandas as pd
df = pd.read_csv(r'E:\DataSets_AI_Course\RealEstate-USA.csv',delimiter=",")

print(df)

print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()



# access the Name column
city = df['city']
print("access the Name column: df : ")
print(city)
print()

# access multiple columns
city_zip_code = df[['city','zip_code']]
print("access multiple columns: df : ")
print(city_zip_code)
print()



# Case 1 : using .loc - default case - starts here
# Reference: https://www.datacamp.com/tutorial/loc-vs-iloc
# 
"""
Syntax               df.loc[row_indexer, column_indexer]              df.iloc[row_indexer, column_indexer]
Indexing Method      Label-based                                      Position-based indexing
Used for Reference   Row and column labels (names)                    Numerical indices of rows and columns (starting from 0)
"""
#Selecting a single row using .loc
second_row = df.loc[2]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()


#Conditional selection of rows using .loc
second_row4 = df.loc[df['city'] == 'Ponce']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:1,'city']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:1,['city','zip_code']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'bed':'city']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['city'] == 'Ponce','bed':'city']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here


print("# Case 2 : using .loc with index_col - starts here")

df_index_col = pd.read_csv(r'E:\DataSets_AI_Course\RealEstate-USA.csv'
,delimiter="," , index_col='state')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
# Second cycle - with index_col as zip-code

#Selecting a single row using .loc
second_row = df_index_col.loc['Puerto Rico']
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[['Puerto Rico', 'Puerto Rico']]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc['Puerto Rico':'Puerto Rico']
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['city'] == 'Ponce']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[:'Puerto Rico','city']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:'Puerto Rico',['city','bed']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:'Puerto Rico','bed':'city']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['city'] == 'Ponce','bed':'city']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 2 : using .loc with index_col  -  ends here
# Starting iloc function from here
#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here
#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()
# Now strating data analysis steps from here
df.loc[len(df.index)] = [15786,'for_sale',150000,4,3,0.13,1567895,'san fransisco','Puerto Rico',602,234,''] 
print("Modified DataFrame - add a new row:")
print(df)
print()
# now deleting rows with indexex
# now delete row with index 0 means first row will be removed
df.drop(0, axis=0, inplace=True)
# deleting rows with index 4 and 5 so row 5 and 6 removed
df.drop([4,5],axis=0,inplace=True)
# NOW displaying modified dataframe with removed rows
print(df) 
# Now deleting columns from dataframe
df.drop('prev_sold_date',axis=1,inplace=True)
# Now deleting two columns at a time from data set
df.drop(['zip_code','street'],axis=1,inplace=True)
# Now displaying dataframe after deleting columns
print(df)
# Now we are renaming columns 
# we are renaming columns bed and bath
df.rename(columns={'bed':'bedrooms','bath':'bathrooms'},inplace=True)
# Renaming a difficult name column
df.rename(columns={'acre_lot':'acre_spread'},inplace=True)
# Now displaying results
print(df)
df.shape
df.columns
df.head
#Now Renaming Row Labels
# rename column one index label
df.rename(index={0: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)
#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

# select the rows where the city is Ponce and Price is greater than 11000000
selected_rows = df.query('city == \'Ponce\' or price > 11000000')

print(selected_rows.to_string())
print(len(selected_rows))
# sort DataFrame by primary key 'state' in ascending order
sorted_df = df.sort_values(by='state')
print(sorted_df.to_string(index=False))
#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'price' and then by 'status' (Both in ascending order)
df1 = df.sort_values(by=['price', 'status'])

print("Sorting by 'price' (ascending) and then by 'status' (ascending):\n")
print(df1.to_string(index=False))
# Starting groupby function from here
grouped = df.groupby('price')['status'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))
#using dropna() function for droping rows
df_cleaned=df.dropna()
print("cleaned data without missing values is :",df_cleaned)
# NOW filling rows having null vales  with 0
df.fillna(0,inplace=True)
print(df)
# Creating array
data=[2,4,5,6,7,8]
myfirst_Array1=pd.array(data)
print(myfirst_Array1)
print(" USA_RealEstate Dataset Working done with Pandas")


