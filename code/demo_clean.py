import pandas as pd
import os

# 1) Ensure the output directory exists
os.makedirs('cleaned_data', exist_ok=True)

# 2) Define the mapping from original columns to new column names
columns_map = {
    'Label (Grouping)': 'county',
    'SEX AND AGE!!Total population': 'total population',
    'SEX AND AGE!!Total population!!Male': 'male',
    'SEX AND AGE!!Total population!!Female': 'female',
    'RACE!!Total population': 'race',
    'Race alone or in combination with one or more other races!!Total population!!White': 'white',
    'Race alone or in combination with one or more other races!!Total population!!Black or African American': 'black or African American',
    'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native': 'American Indian and Alaska Native',
    'Race alone or in combination with one or more other races!!Total population!!Asian': 'Asian'
}

def clean_demo_file(year):
    """
    Reads demo_{year}.csv from raw_data/,
    extracts rows corresponding to '2015-2019 Estimates' (replacing its label with the county name),
    keeps only the selected columns, renames them, and writes the cleaned data to cleaned_data/demo_clean_{year}.csv.
    """
    # Read the CSV file from raw_data folder
    df = pd.read_csv(f'raw_data/demo_{year}.csv')

    # Initialize the current county variable and list for cleaned rows
    current_county = None
    cleaned_rows = []
    label_col = 'Label (Grouping)'

    # Iterate over each row in the DataFrame
    for idx, row in df.iterrows():
        label_value = str(row[label_col]).strip()

        # If the row is a county name (i.e. not one of the special labels), update current_county
        if label_value not in ["2015-2019 Estimates", "2010-2014 Estimates", "Statistical Significance"]:
            current_county = label_value

        # If the row is the '2015-2019 Estimates', use the current county as its label and save it
        elif label_value in ["2015-2019 Estimates", "2016-2020 Estimates", "2017-2021 Estimates"]:

            if current_county is not None:
                new_row = row.copy()
                new_row[label_col] = current_county
                cleaned_rows.append(new_row)

    # Convert the list of cleaned rows into a DataFrame
    df_cleaned = pd.DataFrame(cleaned_rows)

    # Keep only the columns specified in columns_map and rename them accordingly
    df_clean = df[list(columns_map.keys())].copy()
    df_cleaned.rename(columns=columns_map, inplace=True)

    # Save the cleaned DataFrame to the cleaned_data folder
    output_path = f'cleaned_data/demo_clean_{year}.csv'
    df_cleaned.to_csv(output_path, index=False)
    print(f"Finished cleaning demo_{year}.csv → {output_path}")

# Process the files for 2019, 2020, and 2021
for year in ["2019", "2020", "2021"]:
    clean_demo_file(year)
