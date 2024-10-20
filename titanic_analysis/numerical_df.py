import pandas as pd

def get_numerical_df(df: pd.DataFrame, numerical_features: list) -> pd.DataFrame:
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    # Select only the numerical features that are present in the DataFrame
    numerical_df = df[numerical_features].copy()
    
    return numerical_df
    pass

# Example usage:
# df = load_titanic_data('path/to/titanic.csv')
# numerical_features = ['Age', 'Fare', 'SibSp', 'Parch']  # Example numerical features
# numerical_df = get_numerical_df(df, numerical_features)
# print(numerical_df.head())

