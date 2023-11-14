import pandas as pd


with open('koreaDIAMETERlist.txt', 'r') as file:
    # Read numbers from the text file
    numbers = [int(line.strip()) for line in file]

# Create a DataFrame
df = pd.DataFrame(numbers, columns=['Numbers'])

# Count occurrences and sort
result = df['Numbers'].value_counts().reset_index()
result.columns = ['Number', 'Count']
result = result.sort_values(by='Count', ascending=False)

# Select the top 200 values
top_200 = result.head(200)

# Save the top 200 values to a CSV file
top_200.to_csv('diametertop200.csv', index=False)

# Print or save the result
print(top_200)
