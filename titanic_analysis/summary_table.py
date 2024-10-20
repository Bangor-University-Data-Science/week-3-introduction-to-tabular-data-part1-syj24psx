import pandas as pd

def create_summary_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    # Create a summary DataFrame
    summary = pd.DataFrame({
        'Feature Name': df.columns,
        'Data Type': df.dtypes,
        'Number of Unique Values': [df[col].nunique() for col in df.columns],
        'Has Missing Values': [df[col].isnull().any() for col in df.columns]
    })
    
    return summary
    pass

# Example usage:
# df = load_titanic_data('path/to/titanic.csv')
# summary_table = create_summary_table(df)
# print(summary_table)
