Python

# View first and last rows
print("\nFirst 2 rows:")
print(df.head(2))

print("\nLast 2 rows:")
print(df.tail(2))

# Select specific columns 

name_marks = df[["Name" , "Marks"]]
print("\nName and Marks:")
print(name_marks)

# Filter using condition
high_scores = df[df["Marks"] > 80]
print("\nStudents with Marks > 80:")
print(high_scorers)

# Mean of Marks
print("Mean Marks:", df["Marks"].mean())

# Median of Marks 
print("Median Marks:", df["Marks"].median())

# Standard Deviation
print("Standard  Deviation:", df["Marks"].std())
