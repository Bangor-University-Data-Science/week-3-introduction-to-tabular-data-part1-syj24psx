import pandas as pd
import os
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data_valid():
    # Assuming the path is correct for the test
    df = load_titanic_data("../../data/titanic.csv")
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"

def test_load_titanic_data_file_not_found():
    df = load_titanic_data("invalid_path/titanic.csv")
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert df.empty, "The DataFrame should be empty for a non-existent file"

def test_load_titanic_data_empty_file():
    # Create a temporary empty CSV file for testing
    temp_file = "empty_titanic.csv"
    with open(temp_file, 'w') as f:
        pass  # Just create an empty file

    df = load_titanic_data(temp_file)
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert df.empty, "The DataFrame should be empty for an empty file"

    # Clean up the temporary file
    os.remove(temp_file)
