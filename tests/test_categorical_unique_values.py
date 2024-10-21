from titanic_analysis.categorical_unique_values import display_unique_values
import pandas as pd

def test_display_unique_values():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Sex': ['male', 'female', 'female', 'male'],
        'Embarked': ['S', 'C', 'S', 'Q']
    })
    categorical_features = ['Sex', 'Embarked']
    
    unique_values = display_unique_values(mock_df, categorical_features)
    
    # Assertions
    assert isinstance(unique_values, dict), "The result should be a dictionary"
    assert 'Sex' in unique_values and 'Embarked' in unique_values, "Both categorical features should be in the result"
    assert unique_values['Sex'] == ['male', 'female'], "Unique values for 'Sex' should be ['male', 'female']"
    assert unique_values['Embarked'] == ['S', 'C', 'Q'], "Unique values for 'Embarked' should be ['S', 'C', 'Q']"

# To run the test, you can call:
test_display_unique_values()

