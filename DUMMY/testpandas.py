import pandas as pd
import pandas_diff
from IPython.core.display import HTML

# Define the two dataframes
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [5, 5, 6], 'C': [7, 10, 9]})

# Create a DataFrameDiff object
diff = pandas_diff.get_diffs(df1, df2,'A')

html_diff = diff.style.highlight_between().render()
# Get the HTML representation of the diff with colored values
# html_diff = diff.color(added='green', deleted='red', changed='yellow').to_html()

# Display the HTML
HTML(html_diff)