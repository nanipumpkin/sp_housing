import pandas as pd
properties = pd.read_csv('datasets/Sao_Paulo.csv')

# Drop duplicates from properties
properties.drop_duplicates()

# Print the total number of residential properties
print('\nTotal number of properties announced in Sao Paulo dataset = ', len(properties.index))

# Dataset info
print(properties.info())

# Have a look at a random sample of 10 rows
properties.sample(10)
