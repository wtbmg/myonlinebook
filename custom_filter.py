def custom_filter(colA, valueA, colB, df, N):
    import pandas as pd

    """
    Given a dataframe, a columnA in this dataframe to filter by valueA, return a loc new dataframe that contains the top N values in column B.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        The input dataframe for filter and loc
    colA : str
        The column to filter by
    valueA : str
        The value to filter columnA by
    colB: str
        The column to rank by values descending.      
    N: int
        The number of rows to loc for based on descending value in colB
    
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe with filter, rank and loc action applied.
    
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    TypeError
        If N is not an integer > 0 
    AssertError
        If the input argument colA is not in the data columns
    AssertError
        If the input argument colB is not in the data columns
    """
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The df argument is not of type DataFrame")

    # Tests that the the grouping column is in the dataframe
    assert (
        colA in df.columns
    ), "The filtering column colA does not exist in the dataframe"

    # Tests that the the action column is in the dataframe
    assert colB in df.columns, "The ranking column colB does not exist in the dataframe"

    # Test that N is an integer
    assert type(N) == int, "N is not an integer"

    filtered_df = df[df[colA] == valueA]
    new_df = filtered_df.sort_values(by=colB, ascending=False).head(N)

    return new_df
