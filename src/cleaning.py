import pandas as pd

class DataCleaner:
    
    def __init__(self, df):
        self.df = df.copy()
    
    # drops rows where there is found an '(n)' value
    def drop_n_values(self):
        column_names = self.df.columns
        for column in column_names:
            if self.df[column].dtype == 'object':
                mask = self.df[column].str.contains(r'\(n\)', na=False)
                self.df = self.df[~mask]
            else:
                pass     
        return self
        
    # renames columns in unemployment dataset    
    def rename_emp(self):
        self.df.rename(columns={
        "Area FIPS Code" : "FIPS Code",
        "ST FIPS Code" : "State FIPS Code",
        }, inplace=True)
        return self

    # changes all object columns to int64 type
    def unemployment_object_cols_to_int64(self):
        object_columns = ['Employment', 'Unemployment', "Unemployment Rate", "Civilian Labor Force"]
        for column in object_columns:
            self.df[column] = (self.df[column]
                               .astype(str)
                               .str.replace(",", "")
                               .str.replace(".", "")
                               .astype(int))
        return self
        
    # def load_raw_data(self, df):
        