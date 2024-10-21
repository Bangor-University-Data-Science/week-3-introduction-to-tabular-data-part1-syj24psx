import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data_valid():
    # Use an absolute path to the Titanic CSV file
    df = load_titanic_data("D:/DataScience_W3/week-3-introduction-to-tabular-data-part1-syj24psx/data/titanic.csv")
    
    # Check that the returned object is a DataFrame
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    
    # Check that the DataFrame is not empty
    assert not df.empty, "The DataFrame should not be empty"
