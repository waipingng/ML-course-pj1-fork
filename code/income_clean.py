import pandas as pd
import re

# ------------------------------------------------------------------------
# 1. Helper function to parse out county name and map the state to its code
# ------------------------------------------------------------------------
def parse_county_and_state(label):
    """
    Expects a string like "Autauga County, Alabama".
    Returns:
        county_name: "Autauga County"
        state_code: "AL" if the state is "Alabama"
    """
    parts = label.split(',')
    county_name = parts[0].strip()  # e.g. "Autauga County"
    state_full = parts[1].strip() if len(parts) > 1 else ""

    # You can expand this mapping if there are multiple states
    state_code_map = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }
    state_code = state_code_map.get(state_full, "")

    return county_name, state_code


# ------------------------------------------------------------------------
# 2. List of CSV files to read
#    (Adjust these filenames/paths as needed in your environment)
# ------------------------------------------------------------------------
csv_files = ["income_2019.csv", "income_2020.csv", "income_2021.csv"]

# A list to hold our processed results before combining
all_data = []

# ------------------------------------------------------------------------
# 3. Iterate through each file, parse the year from the filename,
#    and extract the needed rows
# ------------------------------------------------------------------------
for file_name in csv_files:
    # Extract year from filename using regex (e.g. "income_2019.csv" -> 2019)
    match_year = re.search(r"(\d{4})", file_name)
    year = match_year.group(1) if match_year else "Unknown"

    # Read the CSV into a DataFrame
    df = pd.read_csv(f'raw_data/income_{year}.csv')

    # Convert the column "Label (Grouping)" to a list for iteration
    labels = df["Label (Grouping)"].tolist()

    # We'll assume the relevant numeric columns are exactly named as follows:
    median_col = "Median income"
    mean_col   = "Mean income"

    # We'll iterate row-by-row:
    i = 0
    while i < len(labels):
        label_text = labels[i]

        # --------------------------------------------------------------------
        # 4. If we see a row that ends with "County, Alabama",
        #    we parse that as our county name. Then:
        #    - The next row is "Households"
        #    - The row after that is "Estimate" with the needed data
        # --------------------------------------------------------------------
        if "County, Alabama" in label_text:
            county_name, state_code = parse_county_and_state(label_text)

            # We expect the row i+1 to be "Households" and i+2 to be "Estimate"
            # Make sure we don't go out of bounds
            if i + 2 < len(labels):
                # row i+2 should contain the actual data for median/mean
                median_val = df.loc[i+2, median_col]
                mean_val   = df.loc[i+2, mean_col]

                # Append the result to our list
                all_data.append({
                    "Year": year,
                    "Label (Grouping)": county_name,    # county only
                    "State Code": state_code,
                    "Median income (dollars)": median_val,
                    "Mean income (dollars)": mean_val
                })

                # Move past these 3 lines (county, households, estimate)
                i += 3
            else:
                i += 1
        else:
            i += 1

# ------------------------------------------------------------------------
# 5. Combine all extracted rows into one DataFrame and save as CSV
# ------------------------------------------------------------------------
combined_df = pd.DataFrame(all_data)

# Reorder columns if you prefer a specific sequence
combined_df = combined_df[
    ["Year", "Label (Grouping)", "State Code",
     "Median income (dollars)", "Mean income (dollars)"]
]

# Save to a new CSV
combined_df.to_csv("cleaned_data/income_combined.csv", index=False)

print("Done! The combined CSV has been saved as 'income_combined.csv'.")
