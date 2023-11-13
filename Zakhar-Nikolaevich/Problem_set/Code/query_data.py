import pandas as pd

# Step 1: Import necessary libraries (Pandas)
# (Already completed above)

# Step 2: Load the dataset from 'ClimateData_Sample.csv'
data_file = 'https://raw.githubusercontent.com/Rising-Stars-by-Sunshine/Econ211-Week2.github.io/main/Zakhar-Nikolaevich/Problem_set/Data/ClimateData_Sample.csv'  # Replace with the actual file path
df = pd.read_csv(data_file)

# Step 3: Define query parameters (e.g., temperature threshold)
temperature_threshold = 25  # Example temperature threshold in degrees Celsius
humidity_range = (40, 70)  # Example humidity range (minimum, maximum)
wind_speed_threshold = 50  # Example wind speed threshold in km/h

# Step 4: Filter the data based on these parameters
# Select records where Temperature > defined threshold
temp_filtered = df[df['Temperature (°C)'] > temperature_threshold]

# Select records based on specific Humidity or Wind Speed criteria
humidity_filtered = df[(df['Humidity (%)'] >= humidity_range[0]) & (df['Humidity (%)'] <= humidity_range[1])]
wind_speed_filtered = df[df['Wind Speed (km/h)'] > wind_speed_threshold]

# Step 5: Output the filtered dataset
# Save filtered data to new CSV files
temp_filtered.to_csv('/path/to/output/temperature_filtered.csv', index=False)
humidity_filtered.to_csv('/path/to/output/humidity_filtered.csv', index=False)
wind_speed_filtered.to_csv('/path/to/output/wind_speed_filtered.csv', index=False)

# Step 6: (Optional) Perform further analysis or visualizations on the filtered data
# Additional code can be added here for more analysis or visualizations

