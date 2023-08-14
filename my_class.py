# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df. 
# BONUS: Return the data grouped in the best manner you see fit.
import os,pandas as pd
class FormatCSV:
    def __init__(self, filename):
        self.filename = filename

    def fix_amount_values(self, value):
        # print("Value:", value) 
        if isinstance(value, str) and value.startswith("$"):
            return float(value.replace("$", "").replace(",", ""))
        elif (isinstance(value, str) and value.strip() == "") or pd.isna(value):
            return 0.0
        return value
    
    def clean_data(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), self.filename)
            df = pd.read_csv(file_path)
            df = df.applymap(self.fix_amount_values)
            return df
        except Exception as e:
            print("An error occurred:", e)
            return None
    def group_data(self, df, grouping_column):
        numeric_columns = df.columns.drop(grouping_column)
        print('numeric_columns',numeric_columns)
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
        grouped_df = df.groupby(grouping_column).sum()
        return grouped_df

csv_formatter=FormatCSV('sample.csv')
formatted_df = csv_formatter.clean_data()

print('formatted_df',formatted_df)
if formatted_df is not None:
    column = "Master"
    grouped_df = csv_formatter.group_data(formatted_df, column)
    print(grouped_df)