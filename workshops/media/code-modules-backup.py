#remove example
import pandas as pd

#create dataframe
libraries = pd.read_csv('libraries.csv')
bpl_branches = pd.DataFrame(libraries)

# Drop Columns
# Syntax: your_dataframe.drop('1st_dropped_column','2nd_column', 'n_dropped_column' ) - Use axis 0 for rows and axis 1 for columns
drop_columns = bpl_branches.drop(columns=['phone', 'network'])
print(drop_columns)