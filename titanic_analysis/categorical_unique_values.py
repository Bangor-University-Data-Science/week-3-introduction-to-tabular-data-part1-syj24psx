import pandas as pd

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values = {}
    
    for feature in categorical_features:
        if feature in df.columns:
            unique_values[feature] = df[feature].unique().tolist()
        else:
            unique_values[feature] = None  # Handle case where feature is not in DataFrame
    
    return unique_values

# Example usage:
# df = pd.read_csv('titanic.csv')
# categorical_features = ['Sex', 'Embarked', 'Pclass']
# unique_values = display_unique_values(df, categorical_features)
# print(unique_values)

