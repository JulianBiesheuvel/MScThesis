import pandas as pd

file_name = '.././data/files/Iceland_Stake_Data_Cleaned.csv'

df = pd.read_csv(file_name)

# Take the difference between the geopotential height and the elevation of the stake measurement
df['height_diff'] = df['altitude_climate'] - df['elevation']

df.to_csv(file_name, index=False)