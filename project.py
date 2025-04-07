import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv('students.csv')

# Step 2: Show basic info
print("Student Data Overview:")
print(df)

# Step 3: Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Fill missing values with the average of the numeric columns
df.fillna(df[['Math', 'Science', 'English']].mean(), inplace=True)


# Step 5: Calculate average marks
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Step 6: Sort students by average marks
sorted_df = df.sort_values(by='Average', ascending=False)

# Step 7: Display results
print("\nFinal Student Data with Average Marks:")
print(sorted_df)

# Optional: Save the final result to a new CSV file
sorted_df.to_csv('final_result.csv', index=False)
