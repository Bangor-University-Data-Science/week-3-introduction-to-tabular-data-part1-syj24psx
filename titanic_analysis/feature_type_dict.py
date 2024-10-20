import pandas as pd

def create_feature_type_dict(df: pd.DataFrame) -> dict:
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],
            'discrete': []
        },
        'categorical': {
            'nominal': [],
            'ordinal': []
        }
    }

    # Iterate through DataFrame columns
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            if len(df[column].unique()) > 20:  # Heuristic for continuous
                feature_types['numerical']['continuous'].append(column)
            else:  # Heuristic for discrete
                feature_types['numerical']['discrete'].append(column)
        elif pd.api.types.is_categorical_dtype(df[column]) or df[column].dtype == 'object':
            # Assume nominal if no order is defined; adjust based on your dataset
            feature_types['categorical']['nominal'].append(column)

    # Example of adding ordinal features based on domain knowledge
    ordinal_features = ['Pclass']  # Add any other ordinal features you know
    feature_types['categorical']['ordinal'].extend(ordinal_features)

    return feature_types
    pass

# Example usage:
# df = load_titanic_data('path/to/titanic.csv')
# feature_types = create_feature_type_dict(df)
# print(feature_types)

