#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Data Visualization with Seaborn

# ### Introduction to Seaborn

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# ```
# Samuel Norman Seaborn
# * "The West Wing" television show

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.scatterplot(x=df['col_x'], y=df['col_y']) # scatter plot
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.countplot(x=df['col_x']) # count plot
# plt.show()
# ```

# ### Using pandas with Seaborn

# ```python
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.countplot(x="col_x", data=df) # using dataframes with countplot
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.scatterplot(x="col_x", y="col_y", data=df) # using dataframes with scatter plot
# plt.show()
# ```

# ### Adding a third variable with hue

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.scatterplot(x="col_x", y="col_y", data=df, 
#                 hue='col_z') # scatter plot with hue
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.scatterplot(x="col_x", y="col_y", data=df, 
#                 hue='col_z', 
#                 hue_order=['var_1', 'var_2']) # setting hue order
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# 
# hue_colors = {"var_1": "#808080",
#               "var_2": "#00FF00"}
# 
# sns.scatterplot(x="col_x", y="col_y", data=df, 
#                 hue='col_z', 
#                 hue_order=['var_1', 'var_2'], 
#                 palette=hue_colors) # using html hex color codes with hue
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.countplot(x="col_x",
#               data=df,
#               hue="col_y") # using hue with count plots
# plt.show()
# ```

# ### Introduction to relational plots and subplots

# **Questions about quantitative variables :**
# <br>Relational plots
# * Height vs. weight
# * Number of school absences vs.  nal grade
# * GDP vs. percent literate

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.relplot(x="col_x", # using relplot
#             y="col_y",
#             data=df,
#             kind="scatter")
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.relplot(x="col_x",
#             y="col_y",
#             data=df,
#             kind="scatter",
#             col='col_z') # subplots in columns
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.relplot(x="col_x",
#             y="col_y",
#             data=df,
#             kind="scatter",
#             row='col_z') # subplots in rows
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.relplot(x="col_x",
#             y="col_y",
#             data=df,
#             kind="scatter",
#             col='col_z', 
#             row='col_w') # subplots in rows and columns
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.relplot(x="col_x",
#             y="col_y",
#             data=df,
#             kind="scatter",
#             col='col_z', 
#             col_wrap=2) # wrapping columns
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.relplot(x="col_x",
#             y="col_y",
#             data=df,
#             kind="scatter",
#             col='col_z', 
#             col_wrap=2, 
#             col_order=['var_1',
#                        'var_2',
#                        'var_3',
#                        'var_4']) # ordering columns
# plt.show()
# ```

# ### Customizing scatter plots

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt 
# sns.relplot(x= "col_x", y= "col_y", 
#             data=df, 
#             kind= "scatter", 
#             size="col_z") # subgroups with point size
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt 
# sns.relplot(x= "col_x", y= "col_y", 
#             data=df, 
#             kind= "scatter", 
#             size="col_z", 
#             hue='col_z') # point size and hue
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt 
# sns.relplot(x= "col_x", y= "col_y", 
#             data=df, 
#             kind= "scatter",
#             hue='col_z',
#             style="col_z") # subgroups with point style
# plt.show()
# ```

# ```python
# import seaborn as sns
# import matplotlib.pyplot as plt 
# sns.relplot(x= "col_x", y= "col_y", 
#             data=df, 
#             kind= "scatter",
#             alpha=0.4) # changing point transparency
# plt.show()
# ```

# ### Introduction to line plots

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="col_x", y="col_y", 
#             data=df, 
#             kind="line") # line plot
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="col_x", y="col_y", 
#             data=df, 
#             kind="line", 
#             style='col_z', 
#             hue='col_z') # subgroups
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="col_x", y="col_y", 
#             data=df, 
#             kind="line", 
#             style='col_z', 
#             hue='col_z',
#             markers=True) # adding markers
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="col_x", y="col_y", 
#             data=df, 
#             kind="line", 
#             style='col_z', 
#             hue='col_z',
#             markers=True,
#             dashes=False) # turning off line style
# plt.show()
# ```

# **Multiple observations per x-value**
# Shaded region is the confidence interval
# * Assumes dataset is a random sample
# * 95% confident that the mean is within this interval
# * Indicates uncertainty in our estimate

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="col_x", y="col_y",
#             data=df,
#             kind="line",
#             ci="sd") # replacing confidence interval with standard deviation
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="col_x", y="col_y",
#             data=df,
#             kind="line",
#             ci=None) # turning off confidence interval
# plt.show()
# ```

# ### Categorical plots: Count plots and bar plots

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x",
#             data=df,
#             kind="count") # countplots with catplot
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# category_order = ['var_1',
#                   'var_2',
#                   'var_3',
#                   'var_4',
#                   'var_5']
# sns.catplot(x="col_x",
#             data=df,
#             kind="count",
#             order=category_order) # changing the order
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x",
#             y="col_y",
#             data=df,
#             kind="bar") # bar plots with catplot
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x",
#             y="col_y",
#             data=df,
#             kind="bar", 
#             ci=None) # turning off confidence interval
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_y", # changing the orientation
#             y="col_x",
#             data=df,
#             kind="bar")
# plt.show()
# ```

# ### Creating a box plot

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             kind="box") # box plot with catplot
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             kind="box",
#             order=['var_1', 'var_2']) # changing order
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             kind="box",
#             sym='') # omitting the outliers using 'sym'
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             kind="box",
#             whis=[0,100]) # changing the whiskers using 'whis'
# plt.show()
# ```
# * By default, the whiskers extend to 1.5 * the interquartile range
# * Make them extend to 2.0 * IQR: ```whis=2.0```
# * Show the 5th and 95th percentiles: ```whis=[5, 95]```
# * Show min and max values: ```whis=[0, 100]```

# ### Point plots

# **Point plots vs. line plots**
# Both show:
# * Mean of quantitative variable
# * 95% confidence intervals for the mean
# <br>Differences:
# * Line plot has **quantitative** variable (usually time) on x-axis
# * Point plot has **categorical** variable on x-axis

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             hue='col_z',
#             kind="point") # creating a point plot
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             hue='col_z',
#             kind="point",
#             join=False) # disconnecting the points
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             hue='col_z',
#             kind="point",
#             estimator=median) # displaying the median
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             hue='col_z',
#             kind="point",
#             capsize=0.2) # customizing the confidence intervals
# plt.show()
# ```

# ```python
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.catplot(x="col_x", 
#             y="col_y",
#             data=df,
#             hue='col_z',
#             kind="point",
#             ci=None) #turning off confidence intervals
# plt.show()
# ```

# ### Changing plot style and color

# ```python
# sns.set_style() # changing the figure style
# ```
# ```
# 'white', 'dark', 'whitegrid', 'darkgrid', 'ticks' 
# ```
# Default figure style ("white")

# ```python
# sns.set_palette() # changing the palette
# ```
# 
# Diverging palettes: ```'RdBu', 'PRGn', 'RdBu_r', 'PRGn_r' ```
# <br>Sequential palettes: ```'Greys', 'Blues', 'PuRd', 'GnBu' ```

# ```python
# custom_palette = ["red", "green", "orange", "blue", "yellow", "purple"]
# sns.set_palette(custom_palette) # custom palettes
# ```

# ```python
# custom_palette = ['#FBB4AE', '#B3CDE3', '#CCEBC5',
#                   '#DECBE4', '#FED9A6', '#FFFFCC',
#                   '#E5D8BD', '#FDDAEC', '#F2F2F2']
# sns.set_palette(custom_palette) # custom palettes
# ```

# ```python
# sns.set_context() # changing the scale
# ```
# Smallest to largest: ```'paper', 'notebook', 'talk', 'paper' ```
# Default context ("paper")

# ### Adding titles and labels

# |Object Type| Plot Types| Characteristics|
# ------------|-----------|----------------|
# |FacetGrid |relplot(), catplot()| Can create subplots|
# |AxesSubplot| scatterplot() , countplot() , etc. |Only creates a single plot|

# ```python
# g = sns.catplot(x="col_x",
#                 y="col_y",
#                 data=df,
#                 kind="box")
# g.fig.suptitle("New Title") # .fig.suptitle : adding a title to FacetGrid
# plt.show()
# ```

# ```python
# g = sns.catplot(x="col_x",
#                 y="col_y",
#                 data=df,
#                 kind="box")
# 
# g.fig.suptitle("New Title", 
#                y=1.03) # adjusting height of title in FacetGrid
# 
# plt.show()
# ```

# ```python
# g = sns.boxplot(x="col_x",
#                y="col_y",
#                data=df)
# 
# g.set_title("New Title", # adding a title to AxesSubplot
#             y=1.03)
# ```

# ```python
# g = sns.catplot(x="col_x",
#                 y="col_y",
#                 data=df,
#                 kind="box",
#                 col="col_z")
# 
# g.fig.suptitle("New Title",
#                y=1.03)
# 
# g.set_titles("This is {col_name}") # Titles for subplots
# ```

# ```python
# g = sns.catplot(x="col_x",
#                 y="col_y",
#                 data=df,
#                 kind="box")
# 
# g.set(xlabel="New X Label", # adding axis labels
#       ylabel="New Y Label") 
# ```

# ```python
# g = sns.catplot(x="col_x",
#                 y="col_y",
#                 data=df,
#                 kind="box")
# 
# plt.xticks(rotation=90) # rotating x-axis tick labels
# 
# plt.show()
# ```
