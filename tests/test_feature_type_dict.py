import pandas as pd
from titanic_analysis.feature_type_dict import create_feature_type_dict

def test_create_feature_type_dict():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Age': [22, 38, 26, 35],
        'Sex': ['male', 'female', 'female', 'male'],
        'Survived': [0, 1, 1, 0],
        'Pclass': [1, 3, 2, 3]
    })
    
    feature_types = create_feature_type_dict(mock_df)
    
    # Check for 'numerical' and 'categorical' keys
    assert 'numerical' in feature_types, "The dictionary should have a 'numerical' key"
    assert 'categorical' in feature_types, "The dictionary should have a 'categorical' key"
    
    # Check numerical features
    assert 'continuous' in feature_types['numerical'], "The 'numerical' dictionary should have a 'continuous' key"
    assert 'discrete' in feature_types['numerical'], "The 'numerical' dictionary should have a 'discrete' key"
    
    assert 'Age' in feature_types['numerical']['continuous'], "Age should be classified as continuous"
    assert 'Survived' in feature_types['numerical']['discrete'], "Survived should be classified as discrete"
    
    # Check categorical features
    assert 'nominal' in feature_types['categorical'], "The 'categorical' dictionary should have a 'nominal' key"
    assert 'ordinal' in feature_types['categorical'], "The 'categorical' dictionary should have an 'ordinal' key"
    
    assert 'Sex' in feature_types['categorical']['nominal'], "Sex should be classified as nominal"
    assert 'Pclass' in feature_types['categorical']['ordinal'], "Pclass should be classified as ordinal"
