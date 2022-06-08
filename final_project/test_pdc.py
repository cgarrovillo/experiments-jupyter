import parse_dollar_col as pdc
import pandas as pd
import numpy as np

"""
Created on Sat Jun 4 15:19:20 2022

@author: Christian Garrovillo

This function tests the parse_dollar_col utility function by creating helper data representing dollar amounts.

"""


def test_pdc():

    # Creates test data
    raw = {"income_sources": ["$2,147,483,647", 0]}

    # Create test data frame from raw test data
    test_data = pd.DataFrame.from_dict(raw)

    # Parse dollar values
    test_data_parsed = pdc.parse_dollar_col(test_data, "income_sources")

    assert test_data_parsed.shape == (2, 1)
    assert test_data_parsed[:1]["income_sources"].dtype == np.float64
    assert test_data_parsed[:1]["income_sources"][0] == 2147483647.00
    assert test_data_parsed[1:2]["income_sources"][1] == 0.00
