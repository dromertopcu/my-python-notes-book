#!/usr/bin/env python
# coding: utf-8

# ## Data Manipulation with Pandas

# ```python
# df.head(n) # first "n" rows default: n=5
# ```

# ```python
# df.info() # column names, non-nulls,dtype
# ```

# ```python
# df.shape
# ```

# ```python
# df.describe() # count, mean, std
# ```

# ```python
# df.values # array of rows
# ```

# ```python
# df.columns # array of column names
# ```

# ```python
# df.index # array of indexes
# ```

# ### Sorting and Subsetting

# ```python
# df.sort_values('col_name') # sorting that column as ascending
# ```

# ```python
# df.sort_values(col_names_list,ascending=bool_list) # sorting multiple variables
# ```

# ```python
# df['col_name'] # subsetting
# ```

# ```python
# df[col_names_list] # subsetting multiple columns
# ```

# ```python
# df[df['col_name']>=num] # subsetting rows
# ```

# ```python
# df[df['col_name'].isin(list_of_values)] # subsetting using .isin()
# ```

# ### New Columns

# ```python
# df['bmi'] = df['weight'] / df['height']**2
# ```

# ### Summary of Data

# ```python
# df['col_name'].mean()
# df['col_name'].median()
# df['col_name'].mode()
# df['col_name'].min()
# df['col_name'].max()
# df['col_name'].var()
# df['col_name'].std()
# df['col_name'].sum()
# df['col_name'].quantile()
# ```

# ```python
# def pct30(column)
#     return column.quantile(0.3)
# ```

# ```python
# df[col_names_list].agg(pct30) # summaries on multiple columns
# ```

# ```python
# df['col_name'].cumsum() # Cumulative sum
# df['col_name'].cummax()
# df['col_name'].cummin()
# df['col_name'].cumprod()
# ```

# ### Counting

# ```python
# df.drop_duplicates(subset='col_name') # dropping duplicates
# ```

# ```python
# df['col_name'].value_counts() # counting values of column
# ```

# ```python
# df['col_name'].value_counts(sort=True) # most ones first
# ```

# ```python
# df['col_name'].value_counts(normalize=True) # proportions of counts
# ```

# ### Grouped Summary Statistics

# ```python
# df.groupby('col_name_1')['col_name_2'].mean() # mean of col_name_2 when values grouped by col_name_1
# ```

# ```python
# df.groupby('col_name_1')['col_name_2'].agg([min,max,sum]) # multiple grouped summaries
# ```

# ### Pivot Tables

# ```python
# df.pivot_table(values = 'col_name_2', index = 'col_name_1')
# ```

# ```python
# df.pivot_table(values = 'col_name_2', index = 'col_name_1', aggfunc = np.median)
# ```

# ```python
# df.pivot_table(values = 'col_name_2', index = 'col_name_1', columns= 'col_name_3') # two variables
# ```

# ```python
# df.pivot_table(values = 'col_name_2', index = 'col_name_1', columns= 'col_name_3', fill_value = 0) # filling missing values in pivot tables
# ```

# ```python
# df.pivot_table(values = 'col_name_2', index = 'col_name_1', columns= 'col_name_3', fill_value = 0, margins = True) # summing columns and rows (Not just summing i.e. mean of all rows)
# ```

# ### Explicit Indexes

# ```python
# df_ind = df.set_index('col_name') # making a column as an index
# ```

# ```python
# df_ind.reset_index() # resetting index making a column again
# ```

# ```python
# df_ind.reset_index(drop = True) # dropping an index
# ```

# ```python
# df_ind.loc[subsetting_values_list] # simpler than .isin() subsetting
# ```

# ```python
# df_ind2 = df.set_index(col_names_list) # multi-level a.k.a. hierarchical indexing
# ```

# ```python
# df_ind2.loc[[value1_col1,value2_col1]] # subset outer level with list
# ```

# ```python
# df_ind2.loc[[(value1_col1,value1_col2),(value2_col1,value2_col2)]] # subset inner level with list of tuple
# ```

# ```python
# df_ind2.sort_index() # sorting by index values
# ```

# ```python
# df_ind2.sort_index(level=[col2,col1],ascending=[True,False]) # controlling sort_index
# ```

# ### Slicing and Subsetting with .loc and .iloc

# ```python
# df_srt = df_ind2.sort_index() # sort the index before slice
# ```

# ```python
# df_srt.loc[value1:value2] # slicing outer index level
# ```

# ```python
# df_srt.loc[(value1_col1,value1_col2):(value2_col1,value2_col2)] # slicing inner index level
# ```

# ```python
# df_srt.loc[:,col1:col2] # slicing columns
# ```

# ```python
# df = df.set_index(date_column).sort_index() # dates sorting as index
# ```

# ```python
# df.loc['2014-08-25':'2018-09-16'] # slicing by dates
# ```

# ```python
# df.loc['2014':'2018'] # slicing by partial dates
# ```

# ```python
# df.iloc[2:5,1:4] # subsetting by row/column number
# ```

# ### Working with Pivot Tables

# ```python
# df_pt.mean(axis='index') # mean of indexes by columns
# ```

# ```python
# df_pt.mean(axis='columns') # mean of columns by indexes
# ```

# ### Visualizing Your Data

# ```python
# import matplotlib.pyplot as plt
# df['col_name'].hist() 
# df['col_name'].hist(bins=20)
# df['col_name'].hist(bins=5)
# plt.show() # histograms
# ```

# ```python
# df_grouped = df.groupby('col_name_1')['col_name_2'].mean()
# df_grouped.plot(kind='bar', title= 'title_name')
# plt.show() # bar plots
# ```

# ```python
# df.plot(x='col_name_1', y='col_name_2', kind='line')
# plt.show() # line plots
# ```

# ```python
# df.plot(x='col_name_1', y='col_name_2', kind='scatter')
# plt.show() # scatter plots
# ```

# ```python
# df[df['sex'] == 'F']['height'].hist(alpha=0.7) # transparency
# df[df['sex'] == 'M']['height'].hist(alpha=0.7) 
# plt.legend(['F','M,]) # adding legend
# plt.show() # layering plots
# ```

# ### Missing Values

# ```python
# df.isna() # df of booleans
# ```

# ```python
# df.isna().any() # columns of booleans
# ```

# ```python
# df.isna().sum() # counting missing values of columns
# ```

# ```python
# df.isna().sum().plot(kind='bar) 
# plt.show() # plotting missing values
# ```

# ```python
# df.dropna() # removing rows with missing value 
# ```

# ```python
# df.fillna(0) # replacing missing value 
# ```

# ### Creating DataFrames

# ```python
# df = pd.DataFrame(list_of_dicts)
# ```

# ### Reading and Writing CSVs

# ```python
# df = pd.read_csv('df.csv')
# ```

# ```python
# df = pd.to_csv('df.csv')
# ```
