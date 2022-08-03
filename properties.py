# Import libraries and read in dataset
import pandas as pd
properties = pd.read_csv('datasets/Sao_Paulo.csv')

# Drop duplicates from properties
properties.drop_duplicates()

# Print the total number of residential properties
print('\nTotal number of properties announced in Sao Paulo dataset = ', len(properties.index))

# Keep rows with non-null addresses
prop_with_address = properties[properties['Rua'].notna()]

# Dataset info
print(properties.info())

# Edit addresses into a consistant format
prop_with_address['Rua-limpa'] = prop_with_address['Rua'].str.replace('\d+', '').str.replace(',', '').str.strip()

# Have a look at a random sample of 10 rows
#print(prop_with_address.sample(10))
print(prop_with_address[['Rua', 'Rua-limpa']].sample(10))