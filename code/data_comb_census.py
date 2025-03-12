import pandas as pd
import re
import os

# Step 1: Define a function to restructure the basic demographic CSV file into a tabular format.
def restructure_csv_tabular(input_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    columns = df.columns.tolist()
    
    # Initialize a list to store the transformed rows
    transformed_rows = []
    
    # Variables to keep track of the current county and state
    current_county = None
    current_state = None
    
    # Process each row in the DataFrame
    for i, row in df.iterrows():
        first_column_value = str(row[columns[0]]).strip()
        
        # Check if the row contains county and state information (using regex)
        county_match = re.match(r'(.+) County, (.+)', first_column_value)
        if county_match:
            current_county = county_match.group(1)
            current_state = county_match.group(2)
            continue
        
        # If the row is an "Estimate" row, extract the income data
        if first_column_value == 'Estimate':
            # Create a new dictionary (tuple) with the county and state information
            new_row = {
                'County': current_county,
                'State': current_state,
            }
            # Iterate over the remaining columns to add income data
            for j in range(1, len(columns)):
                # Clean up the column name for better readability
                clean_col_name = columns[j].replace('Total!!', '').strip()
                new_row[clean_col_name] = row[columns[j]]
            transformed_rows.append(new_row)
    
    # Convert the list of dictionaries into a DataFrame
    result_df = pd.DataFrame(transformed_rows)
    return result_df

# Step 2: Process the basic demographic file using the above function.
basic_demog_file = "../raw_data/basic_demographic_2020.csv"
df_basic = restructure_csv_tabular(basic_demog_file)

# Step 3: Read the second CSV file ("merged_data.csv") from the cleaned_data folder.
merged_file = "../cleaned_data/merged_data.csv"
df_merged = pd.read_csv(merged_file)

# Step 4: Merge the two DataFrames using an outer join on the common keys "County" and "State".
# In relational algebra, this is R ⟕ S on the attributes {County, State}.
final_df = pd.merge(df_basic, df_merged, on=["County", "State"], how="outer")

# Step 5: Save the merged DataFrame to a CSV file in the cleaned_data folder.
output_dir = "../cleaned_data"
os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
output_file = os.path.join(output_dir, "merged_data_gender_race.csv")
final_df.to_csv(output_file, index=False)

print("Merged file saved to:", output_file)
