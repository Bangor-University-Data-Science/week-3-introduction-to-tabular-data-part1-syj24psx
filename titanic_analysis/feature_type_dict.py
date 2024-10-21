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
            # Classify features based on unique value counts and domain knowledge
            if column in ['Age', 'Fare'] or len(df[column].unique()) > 20:  # Treat Age and Fare as continuous
                feature_types['numerical']['continuous'].append(column)
            else:  # Heuristic for discrete
                feature_types['numerical']['discrete'].append(column)
        elif pd.api.types.is_categorical_dtype(df[column]) or isinstance(df[column].dtype, pd.CategoricalDtype):
            feature_types['categorical']['nominal'].append(column)
        elif df[column].dtype == 'object':
            feature_types['categorical']['nominal'].append(column)

    # Example of adding ordinal features based on domain knowledge
    ordinal_features = ['Pclass']  # Add any other ordinal features you know
    feature_types['categorical']['ordinal'].extend(ordinal_features)

    return feature_types
