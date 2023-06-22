import pandas as pd
import pandas_diff
from IPython.core.display import HTML

# Define the two dataframes
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [5, 5, 6], 'C': [7, 10, 9]})

# Create a DataFrameDiff object
diff = pandas_diff.get_diffs(df1, df2,'A')

# Define a function to check if two values are different
def are_different(x, y):
    if pd.isnull(x) and pd.isnull(y):
        return False
    elif pd.isnull(x) or pd.isnull(y):
        return True
    else:
        return x != y

# Define a function to highlight the differences between two dataframes
def highlight_diff(df1, df2):
    # Create an empty dataframe with the same shape as df1 and df2
    df = pd.DataFrame('', index=df1.index, columns=df1.columns)
    # Highlight the differences between df1 and df2
    for column in df1.columns:
        is_different = are_different(df1[column], df2[column])
        df[column][is_different] = 'background-color: yellow'
    # Highlight the added values in df2
    if isinstance(df2, pd.Series):
        added = df2.index
    else:
        added = df2.index.difference(df1.index)
    df.loc[added, :] = 'background-color: lightgreen'
    # Highlight the deleted values in df1
    if isinstance(df1, pd.Series):
        deleted = df1.index
    else:
        deleted = df1.index.difference(df2.index)
    df.loc[deleted, :] = 'background-color: lightcoral'
    return df


# Get the styled dataframe with colored values
styled_diff = diff.style.apply(highlight_diff, args=(df1, df2))

# Get the HTML representation of the styled dataframe
html_diff = styled_diff.render()

# Display the HTML
HTML(html_diff)
