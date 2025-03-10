import os
import pandas as pd

def consolidate_demographic_data():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    raw_data_dir = os.path.join(base_dir, "..", "Raw_data")
    cleaned_data_dir = os.path.join(base_dir, "..", "Cleaned_data")

    years = [2019, 2020, 2021]

    all_years_data = []

    for year in years:

        demo_file = os.path.join(raw_data_dir, f"{year}_demo_raw.csv")
        income_file = os.path.join(raw_data_dir, f"{year}_income_raw.csv")

        df_demo = pd.read_csv(demo_file)
        df_income = pd.read_csv(income_file)

        df_merged = pd.merge(df_demo, df_income,
                             on=["state name", "state code"],
                             how="outer")


        all_years_data.append(df_merged)

    df_final = pd.concat(all_years_data, ignore_index=True)

    all_columns = list(df_final.columns)
    all_columns.remove("state name")
    all_columns.remove("state code")
    new_column_order = ["state name", "state code"] + all_columns
    df_final = df_final[new_column_order]

    output_csv = os.path.join(cleaned_data_dir, "demographic_clean.csv")
    df_final.to_csv(output_csv, index=False)

if __name__ == "__main__":
    consolidate_demographic_data()
