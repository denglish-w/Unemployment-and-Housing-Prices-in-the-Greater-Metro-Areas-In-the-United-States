import pandas as pd

class DataCleaner:

    def __init__(self, housing_data_file_path: str, unemployment_data_file_path: str):
        raw_data_housing = pd.read_csv(housing_data_file_path)
        raw_data_unemployment = pd.read_csv(unemployment_data_file_path, skiprows=2).dropna()
        self.clean_unemployment_data = self.full_clean(raw_data_unemployment)
        
    
    @staticmethod
    def rename_unemployment_columns(df_to_clean: pd.DataFrame) -> pd.DataFrame: 
        """
        This function changes the names of the columns on the unemployment dataset.
        Args: 
            df_to_clean: is the dataframe with the columns to change
                
        Return:
            pd.DataFrame: dataframe with the changed columns.
        """
        columns_to_rename = {
        "Area FIPS Code" : "FIPS Code",
        "ST FIPS Code" : "State FIPS Code",
        }
        return df_to_clean.rename(columns=columns_to_rename)

    # drops rows where there is found an '(n)' value
    @staticmethod
    def drop_n_values_for_unemployment_df(raw_data: pd.DataFrame) -> pd.DataFrame:
        df_to_clean = raw_data.copy()
        column_names = df_to_clean.columns
        for column in column_names:
            if df_to_clean[column].dtype == 'object':
                mask = df_to_clean[column].str.contains(r'\(n\)', na=False)
                df_to_clean = df_to_clean[~mask]
            else:
                pass
        return df_to_clean

    # changes all object columns to int64 type
    @staticmethod
    def unemployment_object_columns_to_int64(raw_data: pd.DataFrame) -> pd.DataFrame:
        df_to_clean = raw_data.copy()
        object_columns = ['Employment', 'Unemployment', "Unemployment Rate", "Civilian Labor Force"]
        for column in object_columns:
            df_to_clean[column] = (df_to_clean[column]
                               .astype(str)
                               .str.replace(",", "")
                               .str.replace(".", "")
                               .astype(int))
        return df_to_clean
    
    @staticmethod
    def unemployment_float_cols_to_int64(raw_data: pd.DataFrame) -> pd.DataFrame:
        data_to_clean = raw_data.copy()
        float_columns = ['State FIPS Code', 'FIPS Code', 'Year', 'Month']
        for column in float_columns:
            data_to_clean[column] = data_to_clean[column].astype(int)
        return data_to_clean
    
    def full_clean(self, unemployment_dataframe: pd.DataFrame):
        renamed_columns = self.rename_unemployment_columns(unemployment_dataframe)
        no_nas = self.drop_n_values_for_unemployment_df(renamed_columns)
        object_now_int_columns = self.unemployment_object_columns_to_int64(no_nas)
        float_now_int_columns = self.unemployment_float_cols_to_int64(object_now_int_columns)
        return float_now_int_columns
    
    # load raw csv file from file path    
    # def load_raw_csv(self, filepath):
    #         try:
    #             df = pd.read_csv(filepath)
    #             return df   
    #         except FileNotFoundError:
    #             print(f"Error, file not found: {FileNotFoundError}")
    #             return None