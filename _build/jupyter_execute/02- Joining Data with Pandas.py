#!/usr/bin/env python
# coding: utf-8

# ## Joining Data with Pandas

# ### Inner Join

# ```python
# df_merged = df.merge(df2, on='col_name') # inner join
# ```

# ```python
# df_merged = df.merge(df2, on='col_name', suffixes=('_1','_2')) # suffixes
# ```

# ```python
# df_merged = df.merge(df2, on=['col_name_1','col_name_2'], suffixes=('_1','_2')) # multiple columns check
# ```

# ```python
# df_merged = df.merge(df2, on=['col_name_1','col_name_2']) \
#     .merge(df3, on='col_name_3',suffixes=('_1','_2')) # merging multiple tables
# ```

# ```python
# import matplotlib.pyplot as plt
# df_merged.groupby('col_name_3').agg('sum').plot(kind='bar', y='col_name')
# plt.show() # plotting result
# ```

# ```python
# df1.merge(df2, on='col') \
#     .merge(df3, on='col') \
#     .merge(df4, on='col') # merging four tables
# ```
# 

# ### Left Join

# ```python
# df_merged = df.merge(df2, on='col_name', how='left') # left join
# ```

# ### Right Join

# ```python
# df_merged = df.merge(df2, how='right', left_on='col_name_left', right_on='col_name_right') # right join with different column names
# ```

# ### Outer Join

# ```python
# df_merged = df.merge(df2, on='col_name', how='outer', suffixes=('_1','_2')) # outer join
# ```

# ### Merging to itself

# ```python
# df_sequels = df.merge(df, left_on='sequel', right_on='id', suffixes=('_org','_seq')) # merging a table to itself with different relating rows
# ```

# ```python
# df_sequels = df.merge(df, left_on='sequel', right_on='id', how='left', suffixes=('_org','_seq')) # merging a table to itself with left join
# ```

# ### Merging on indexes

# ```python
# df1 = pd.read_csv('df1.csv', index_col=['id'])
# df2 = pd.read_csv('df2.csv', index_col=['id'])
# df_merged = df1.merge(df2, on='id', how='left') # merging on index
# ```

# ```python
# df1 = pd.read_csv('df1.csv', index_col=['id1','id2'])
# df2 = pd.read_csv('df2.csv', index_col=['id1','id2'])
# df_merged = df1.merge(df2, on=['id1','id2']) # multiIndex merge
# ```

# ```python
# df1 = pd.read_csv('df1.csv', index_col=['id1'])
# df2 = pd.read_csv('df2.csv', index_col=['id2'])
# df_merged = df1.merge(df2, left_on='id1', left_index=True, right_on='id2', right_index=True) # index merge with left_on, right_on
# ```

# ### Filtering Joins

# ```python
# df_merged = df.merge(df2, on='col_name')
# df_semi = df[df['col_name'].isin(df_merged['col_name'])] # semi join
# ```
# Semi joins
# * Returns the intersection, similar to an inner join
# * Returns only columns from the left table and not the right
# * No duplicates

# ```python
# df_merged = df.merge(df2, on='col_name', how='left', indicator=True)
# left_only_list = df_merged.loc[df_merged['_merge'] == 'left_only', 'col_name']
# df_anti = df[df['col_name'].isin(left_only_list)] # anti join
# ```
# Anti join
# * Returns the left table, excluding the intersection
# * Returns only columns from the left table and not the right

# ### Concatenate DataFrames vertically

# ```python
# df_concat = pd.concat([df1, df2, df3]) # basic concatenation
# ```

# ```python
# df_concat = pd.concat([df1, df2, df3],ignore_index=True) # ignoring index
# ```

# ```python
# df_concat = pd.concat([df1, df2, df3],ignore_index=False, keys=['_1','_2','_3']) # setting labels as outer index
# ```

# ```python
# df_concat = pd.concat([df1, df2, df3], join = 'inner') # concatenate tables with different column names
# ```

# ### Using append method

# ```python
# .append()
# ```
# * Simplified version of the .concat() method
# * Supports: ignore_index , and sort
# * Does Not Support: keys and join
#     * Always join = outer

# ```python
# df_appended = df1.append([df2,df3], ignore_index=True, sort=True)
# ```

# ### Validating merges

# ```python
# .merge(validate=None)
# ```
# Checks if merge is of specified type
# * 'one_to_one'
# * 'one_to_many'
# * 'many_to_one'
# * 'many_to_many'

# ```python
# df.merge(df2, on='col_name', validate='one_to_one')
# ```
# ```
# Traceback (most recent call last):
# MergeError: Merge keys are not unique in right dataset; not a one-to-one merge
# ```
# ```python
# df.merge(df2, on='col_name', validate='one_to_many') # without error
# ```

# ### Verifying concatenations

# ```python
# .concat(verify_integrity=False)
# ```
# * Check whether the new concatenated index contains duplicates
# * Default value is False

# ```python
# pd.concat([df1, df2], verify_integrity=True)
# ```
# ```
# Traceback (most recent call last):
# ValueError: Indexes have overlapping
# ```
# ```python
# pd.concat([df1, df2], verify_integrity=False) # without error
# ```

# ### Using merge_ordered()

# When to use merge_ordered()?
# * Ordered data / time series
# * Filling in missing values
# 
# Method comparison
# | .merge()  | merge_ordered()  |
# |-------|------------|
# | Type of join <br>  * default inner | Type of join <br> * default outer |
# |Calling the method <br> * df1.merge(df2) | Calling the method <br> * pd.merge_ordered(df1, df2)  |

# ```python
# import pandas as pd
# pd.merge_ordered(df1, df2, on='col_name', suffixes=('_1','_2'))
# ```

# ```python
# import pandas as pd
# pd.merge_ordered(df1, df2, on='col_name', suffixes=('_1','_2'), fill_method='ffill') # forward fill
# ```

# ### Using merge_asof()

# Similar to a merge_ordered() left  join
# * Similar features as merge_ordered()
# 
# 
# Match on the nearest key column and not exact matches.
# * Merged "on" columns must be sorted.

# ```python
# import pandas as pd
# pd.merge_asof(df1, df2, on='col_name', suffixes=('_1','_2'))
# ```

# ```python
# import pandas as pd
# pd.merge_asof(df1, df2, on='col_name', suffixes=('_1','_2'), direction= 'forward') # with direction
# ```

# ### Selecting data with .query()

# ```python
# df.query('col_name >= num1') # querying
# ```

# ```python
# df.query('col_name_1 > num1 and col_name_2 < num2') #querying multiple conditions
# ```

# ```python
# df.query('col_name_1 > num1 or col_name_2 < num2') #querying multiple conditions
# ```

# ```python
# df.query('col_name_1 == "text_string_1" or (col_name_1 == "text_string_2" and col_name_2 < num)') #querying to select text
# ```

# ### Reshaping data with .melt()

# ![Wide versus long data](https://img001.prntscr.com/file/img001/vIxFAwa-S3yXky968DWtsg.jpg)
# The melt method will allow us to unpivot our dataset

# ```python
# df_long = df.melt(id_vars=['col_name_1','col_name_2']) # id columns of rows
# ```

# ```python
# df_long = df.melt(id_vars=['col_name_1','col_name_2'],
#                  value_vars=['value_1','value_2']) # melting only selected values 
# ```

# ```python
# df_long = df.melt(id_vars=['col_name_1','col_name_2'],
#                  value_vars=['value_1','value_2'],
#                  var_name=['string_var'], value_name='string_val') # melting only selected values 
# ```
