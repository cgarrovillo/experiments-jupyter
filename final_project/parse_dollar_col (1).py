"""
Created on Sat Jun 4 15:19:20 2022

@author: Christian Garrovillo

"""


def parse_dollar_col(df, dollar_col):
    import pandas as pd

    """
    Given a dataframe and a column name, parses a column of string values representing dollar amounts into floats for a more accurate and
    workable representation of the data.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        The dataframe containing a column that represents dollar amounts as a string
    dollar_col : str
        The name of the column that represents dollar amounts as a string to be converted into a float.
    
    Returns
    -------
    pandas.core.frame.DataFrame
        A DataFrame containing a column that represents dollar amounts as a float
    
    Raises
    ------
    TypeError 
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument col_name is not part of the data DataFrame.
        
    Examples
    --------
    >>> parse_dollar_col(df, 'total_gross')
    >>> df.dtypes['total_gross']
    dtype('float64')    
    """

    # Checks that the type of object being passed into the data argument is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The df argument is not of type DataFrame")

    # Tests that the column containing dollar amounts exists in the dataframe
    assert (
        dollar_col in df.columns
    ), "The specified column does not exist in the dataframe"

    df_copy = df.copy()
    df_copy[dollar_col] = (
        df_copy[dollar_col]
        .apply(
            lambda x: x.replace("$", "").replace(",", "") if isinstance(x, str) else x
        )
        .astype(float)
    )

    return df_copy
