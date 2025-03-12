import pandas as pd


df1 = pd.read_csv("cleaned_data/heart_disease_mortality_cleaned.csv")
df2 = pd.read_csv("cleaned_data/income_combined.csv") 

df1.rename(columns={"LocationDesc": "County"}, inplace=True)
df1.rename(columns={"LocationAbbr": "State Code"}, inplace=True)
df2.rename(columns={"Label (Grouping)": "County"}, inplace=True)
merged_df = pd.merge(df1, df2, on=["Year", "County", "State Code"], how="inner")

merged_df = merged_df.loc[(merged_df["Sex"] == "Overall") & (merged_df["ethnicity"] == "Overall")]
merged_df = merged_df.drop(columns=["GeographicLevel", "Data_Value_Unit", "Data_Value_Type", "LocationID", "Y_lat", "X_lon", "Georeference"])
merged_df.to_csv("cleaned_data/merged_data.csv", index=False)
