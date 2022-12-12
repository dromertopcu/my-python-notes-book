#!/usr/bin/env python
# coding: utf-8

# ## Intermediate Data Visualization with Seaborn

# ### Introduction to Seaborn

# ```
# Matplotlib
# ```
# ```python
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv("df.csv")
# fig, ax = plt.subplots()
# ax.hist(df['col_name'])
# ````

# ```
# Pandas
# ```
# ```python
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv("df.csv")
# df['col_name'].plot.hist()
# ````

# ```python
# import seaborn as sns
# sns.histplot(df['col_name']) #seaborn histplot
# ````

# ```python
# import seaborn as sns
# sns.distplot(df['col_name'], kind='kde') #seaborn distplot
# ````
# By default, it generates a histogram but can also generate
# other plot types

# ### Using the Distribution Plot

# ```python
# sns.displot(df['col_name'], kde=True, bins=10) #overlay a KDE plot on the histogram and specify the number of bins
# ````
# 

# A rug plot is an alternative way to view the distribution of data by including small tickmarks along the x axis
# ```python
# sns.displot(df['col_name'], kind='kde', rug=True, fill=True) #A kde curve and rug plot can be combined
# ````
# 

# The displot function uses several functions including kdeplot , rugplot and ecdfplot
# ```python
# sns.displot(df['col_name'], kind='ecdf') #The ecdfplot shows the cumulative distribution of the data
# ````
# 

# ### Regression Plots in Seaborn

# The regplot function generates a sca er plot with a regression line
# ```python
# sns.regplot(data=df, x="col_name_1", y="col_name_2" ) # regplot
# ````
# 

# ```python
# sns.lmplot(data=df, x="col_name_1", y="col_name_2" ) # lmplot high level of regplot
# ````

# ```python
# sns.lmplot(data=df, x="col_name_1", y="col_name_2", hue='col_name_3') # Organize data by colors
# ````

# ```python
# sns.lmplot(data=df, x="col_name_1", y="col_name_2", col='col_name_3') # Organize data by columns
# ````

# ### Using Seaborn Styles

# ```python
# sns.set() # seaborn's default configurations
# ```

# ```python
# for style in ['white','dark','whitegrid','darkgrid','tick'] : 
#     sns.set_style(style) # theme examples with sns.set_style()
#     sns.displot(df['col_name'])
#     plt.show()
# ```

# ```python
# sns.despine(left=True) # removing the spines
# ```

# ### Colors in Seaborn

# ```python
# sns.set(color_codes=True) #assigning colors to plots using matplotlib color codes
# sns.displot(df['col_name'], color='g') 
# ```

# ```python
# palettes = ['deep', 'muted', 'pastel', 'bright', 'dark','colorblind']
# for p in palettes:
#     sns.set_palette(p) #defining a palette
#     sns.displot(df['col_name'])
# ```

# ```python
# sns.palplot() # displays a palette
# sns.color_palette() # returns the current palette
# sns.palplot(sns.color_palette()) # displays the current palette
# ```

# ### Customizing with matplotlib

# ```python
# fig, ax = plt.subplots()
# sns.histplot(df['col_name'], ax=ax)
# ax.set(xlabel='x_label') # customization
# ```

# ```python
# fig, ax = plt.subplots()
# sns.histplot(df['col_name'], ax=ax)
# ax.set(xlabel="x_label",
#        ylabel="y_label", xlim=(0, 50000), #further customizations
#        title="title")
# ```

# **Combining plots**
# ```python
# fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2,
#                                sharey=True, figsize=(7,4))
# sns.histplot(df['col_name'], stat='density', ax=ax0)
# sns.histplot(df.query('col_name_1 == "val_1"')['col_name'], stat='density', ax=ax1)
# ax1.set(xlabel='col_name (val_1)', xlim=(0, 70000))
# ax1.axvline(x=20000, label='label_vline', linestyle='--')
# ax1.legend()
# ```

# ### Categorical Plot Types

# **Combining plots**
# ```python
# fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2,
#                                sharey=True, figsize=(7,4))
# sns.histplot(df['col_name'], stat='density', ax=ax0)
# sns.histplot(df.query('col_name_1 == "val_1"')['col_name'], stat='density', ax=ax1)
# ax1.set(xlabel='col_name (val_1)', xlim=(0, 70000))
# ax1.axvline(x=20000, label='label_vline', linestyle='--')
# ax1.legend()
# ```
