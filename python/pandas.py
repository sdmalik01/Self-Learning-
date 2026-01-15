import pandas as pd
info = {
    "Name": ["Rahul","Harshita","Shradha", "Malik"],
    "CGPA": [9.5, 7.5, 8.5, 10.0]   
}

df = pd.DataFrame(info)
print(df)

s = pd.Series([21,20,23,24], index = ["Malik","Aftab","Shahed","Swarup"])
print(s, type(s))
print(s["Malik"]) # Pointing element by labelling

labels = s.index  # .index returns all labels 
print(labels)

# Series data type in pandas

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])
s1[0] = 100     # Existing values are mutable
s3 = s1 + s2    # Vectorized operations on arrays like numpy

changed_s1 = s1.drop(0)    # Drop function drops value along with its label
print(s1)    # Original is intact as the series in pandas are immutable
print(changed_s1)   # New series is created when value is droped or added

# -------------------------------------------- DataFrame data type in pandas -----------------------------------------------

# Creating DataFrame:

# Creating from python dictionaries
info = {
    "Names": ["Adam","Eve","Bob"],
    "Age": [23, 24, 25],
    "GPA": [9.5, 8.6, 7.2]
}

df = pd.DataFrame(info, index = ["first","second","third"])
print(df, type(df))

print(df.index)  # Returns the labels (Row labels ie 0, 1, 2)
print(df.columns) # Returns the columns name

# Creating from list of list:


# [[first_row], [second_row], [third_row]....., columns_name = [should be equal to number of columns], index = [label_names which should be equal to number of rows]]
df = pd.DataFrame([["Adam", 24], ["Malik", 25], ["Rohan", 10]], columns = ["Name", "Age"], index = ["first", "second", "third"])
print(df)

# From Numpy array

import numpy as np

np_array = np.array([[1,2,3], [4,5,6]])

df = pd.DataFrame(np_array, columns = ["A","B","C"], index = ["first","second"])
print(df)

# json data

df = pd.read_json("employee_data.json")
print(df, type(df))

# csv data

df = pd.read_csv("employee_data.csv")
print(df, type(df))

# ---------------------------- DataFrame Methods: which can be used to perform different operations on the DataFrame ie EDA usescase --------------------------------

print(df.head())   #head() returns the first five values in the DataFrame
print("                -----------         ")
print(df.tail())   #tail returns the last five values of the DataFrame
print("                -----------         ")
print(df.sample())  #sample returns the sample value from the dataframe
print("                -----------         ")
print(df.sample(5))   #(value) this value in sample(), head() & tail() defines the quantity of the rows

# Info returns a summary of the data in the DataFrame
df.info()

print("                -----------         ")

# shape returns the (Rows, columns) of the DataFrame
print(df.shape)

print("                -----------         ")

# describe returns sum information about numerical data: such as count, min, max & percentile of percentage, etc.
print(df.describe())

print("                -----------         ")

# columns returns the columns
print(df.columns)

print("                -----------         ")

# nunique returns the number of unique rows in that column
print(df.nunique())

# AQI DataSet - Real DataSet from Kaggle

df = pd.read_csv("globalAirQuality.csv")
print(df.sample())
print("                -----------         ")
print(df.describe())

# ------------------------------- Selecting the data: -----------------------------------------

# Selection of columns
df["city"]    # Returns columns
df[["city","aqi"]]   # Takes [list of columns]

# Selection of rows based upon indexes and labels

# row selection Based upon indexes provided by pandas

df.iloc[0]
df.iloc[0:2]     # [start index, ending index(exclusive)]

# row selection Based upon location or label

df.loc[1]
df.loc[0:2]     # [start index, ending index(inclusive)]

# Accessing single cell element using labels 
df.loc[0, "aqi"]   # df.loc[ row value, column value]
df.loc[df["city"] == "Delhi", df.columns == "aqi"]

df.loc[0:2,["city","aqi"]]
df.iloc[0:2, 2]    # iloc takes only indexes even for columns too hence it will give ever for string,etc

# Hence loc takes strings also while iloc takes only numerical values:

df.loc[0:2, ["city","aqi","latitude"]]
df.iloc[0:3, 1:5]                           # Both give same values but inclusion of the end in [] & input values type in df.loc/iloc[value]


# ---------------------------------- Selection of individual cell or scalar value by label and indexes --------------------------------

df.at[0, "city"]      # at[row, column]
df.iat[0, 2]          # iat[row, column] but both should be numeric



# IMPORTENT: This selection methods returns jst a view rather then saving a copy so if u want to save it then store it in a variale etc.

df.at[0, "city"]    # View only - just a view window to see and observe
USA_cit = df["city"].copy()    # Copy - will not chnage in the main dataset
USA_city = df.at[0,"city"]   # Stored  - if we change this further it will get changed in the main datase
print(USA_city)              # This saves a copy

# Even if we change a value in view mode it get refeclected in the main data 
#df.at[0, "city"] = "Ahmedabad"    -    This will change the value in the main dataset too.

# --------------- Filtering of data: ----------------------------------------

df[df["aqi"] > 100]      # df[condition]
df[(df["aqi"] > 100) & (df["temperature"] > 30)]     # df[condition1 & condition2]
# & - and, | - or, ~ = not

df[0:2]["city"]  # df[rows][columns]
df[df["aqi"] > 100 ][["city", "aqi"]]  # df[condition for rows][columns]

aqi_data = df[(df["aqi"] > 100) & (df["temperature"] > 30)][["city","aqi"]]
# Still after this the labels do not get change! it will be same as in main dataset
aqi_data.loc[6]
aqi_data.iloc[0]      # both are same! this shows the difference between labels and index



