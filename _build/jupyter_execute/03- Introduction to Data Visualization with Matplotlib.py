#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Data Visualization with Matplotlib

# ### Introduction to pyplot

# ```python
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# plt.show() # empty pyplot interface
# ```

# ```python
# ax.plot(df['col_x'], df['col_y']) # adding data to axes
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots()
# ax.plot(df['col_x'], df['col_y'])
# ax.plot(df2['col_x'], df2['col_y']) # adding more data
# plt.show()
# ```

# ### Customizing plots

# ```python
# ax.plot(df['col_x'],
#         df['col_y'],
#         marker='o') # adding markers
# plt.show()
# ```

# ```python
# ax.plot(df['col_x'],
#         df['col_y'],
#         marker='v') # choosing markers
# plt.show()
# ```
# https://matplotlib.org/api/markers_api.html

# ```python
# ax.plot(df['col_x'],
#         df['col_y'],
#         marker='v',
#         linestyle='--') # setting the linestyle
# plt.show()
# ```

# ```python
# ax.plot(df['col_x'],
#         df['col_y'],
#         marker='v',
#         linestyle='None') # eliminating lines
# plt.show()
# ```

# ```python
# ax.plot(df['col_x'],
#         df['col_y'],
#         marker='v',
#         linestyle='--', 
#         color='r') # choosing color
# plt.show()
# ```

# ```python
# ax.set_xlabel("x_label_string") # customizing the axes labels
# plt.show()
# ```

# ```python
# ax.set_xlabel("x_label_string")
# ax.set_ylabel("y_label_string") # customizing the axes labels
# plt.show()
# ```

# ```python
# ax.set_title("title_string") # adding a title
# plt.show()
# ```

# ### Small multiples

# ```python
# fig, ax = plt.subplots(3, 2) # small multiples with plt.subplots
# plt.show()
# ```

# ```python
# ax.shape
# ```
# ```
# (3, 2)
# ```

# ```python
# ax[0, 0].plot(df["col_x"], # adding data to subplots
#               df["col_y"],
#               color='b')
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots(2, 1) # subplots with data
# 
# ax[0].plot(df['col_x'], df['col_y_1'],
#            color='b')
# ax[0].plot(df['col_x'], df['col_y_2'],
#            linestyle='--', color='b')
# ax[0].plot(df['col_x'], df['col_y_3'],
#            linestyle='--', color='b')
# 
# ax[1].plot(df2['col_x'], df2['col_y_1'],
#            color='r')
# ax[1].plot(df2['col_x'], df2['col_y_2'],
#            linestyle='--', color='r')
# ax[1].plot(df2['col_x'], df2['col_y_3'],
#            linestyle='--', color='r')
# 
# ax[0].set_ylabel('y1_label_string')
# ax[1].set_ylabel('y2_label_string')
# 
# ax[1].set_xlabel('x_label_string')
# 
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots(2, 1, sharey=True) # sharing the y-axis range
# ```

# ### Plotting Time-Series Data

# ```python
# import pandas as pd
# df_time = pd.read_csv('df_time.csv',
#                       parse_dates=["date"],
#                       index_col="date")
# ```

# ```python
# df_time.index
# ```
# ```
# DatetimeIndex(...)
# ```

# ```python
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# 
# ax.plot(df_time.index, df_time['col_y']) # plotting time-series data
# ax.set_xlabel('Time')
# ax.set_ylabel('y_label_string')
# plt.show()
# ```

# ```python
# sixties = df_time["1960-01-01":"1969-12-31"] # zooming in on a decade
# 
# fig, ax = plt.subplots()
# ax.plot(sixties.index, sixties['col_y'])
# ax.set_xlabel('Time')
# ax.set_ylabel('y_label_string')
# plt.show()
# ```

# ```python
# sixty_nine = df_time["1969-01-01":"1969-12-31"] # zooming in on one year
# 
# fig, ax = plt.subplots()
# ax.plot(sixty_nine.index, sixty_nine['col_y'])
# ax.set_xlabel('Time')
# ax.set_ylabel('y_label_string')
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots()
# ax.plot(df_time.index, df_time["col_y1"])
# ax.set_xlabel('Time')
# ax.set_ylabel('y1_label_string')
# 
# ax2 = ax.twinx() # using twin axes plotting two time-series together
# ax2.plot(df_time.index, df_time["col_y2"])
# ax2.set_ylabel('y2_label_string')
# 
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots() # seperating variables by color
# ax.plot(df_time.index, df_time["col_y1"], color= 'blue')
# ax.set_xlabel('Time')
# ax.set_ylabel('y1_label_string', color='blue')
# 
# ax2 = ax.twinx() 
# ax2.plot(df_time.index, df_time["col_y2"], color= 'red')
# ax2.set_ylabel('y2_label_string', color= 'red')
# 
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots()
# ax.plot(df_time.index, df_time["col_y1"], color= 'blue')
# ax.set_xlabel('Time')
# ax.set_ylabel('y1_label_string', color='blue')
# ax.tick_params('y', colors='blue')  # coloring the ticks
# 
# ax2 = ax.twinx() 
# ax2.plot(df_time.index, df_time["col_y2"], color= 'red')
# ax2.set_ylabel('y2_label_string', color= 'red')
# ax.tick_params('y', colors='red')
# 
# plt.show()
# ```

# ### Using our function

# A function that plots time-series
# ```python
# def plot_timeseries(axes, x, y, color, xlabel, ylabel):
#     axes.plot(x, y, color=color)
#     axes.set_xlabel(xlabel)
#     axes.set_ylabel(ylabel, color=color)
#     axes.tick_params('y', colors=color)
# ```

# ```python
# fig, ax = plt.subplots()
# 
# plot_timeseries(ax, df_time.index, df_time['col_y1'],
#                 'blue', 'Time', 'y1_label_string')
# ax2 = ax.twinx()
# plot_timeseries(ax, df_time.index, df_time['col_y2'],
#                 'red', 'Time', 'y2_label_string')
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots()
# 
# plot_timeseries(ax, df_time.index, df_time['col_y1'],
#                 'blue', 'Time', 'y1_label_string')
# ax2 = ax.twinx()
# plot_timeseries(ax, df_time.index, df_time['col_y2'],
#                 'red', 'Time', 'y2_label_string')
# ax2.annotate("string", xy=[pd.TimeStamp("2015-10-06"), y_tick]) # annotation
# plt.show()
# ```

# ```python
# ax2.annotate("string",
#              xy=(pd.Timestamp('2015-10-06'), y_tick),
#              xytext=(pd.Timestamp('2008-10-06'), y_tick2),
#              arrowprops={}) # adding arrows to annotation
# ```

# ```python
# ax2.annotate("string",
#              xy=(pd.Timestamp('2015-10-06'), y_tick),
#              xytext=(pd.Timestamp('2008-10-06'), y_tick2),
#              arrowprops={"arrowstyle":"->", "color":"gray"}) # customizing arrow properties
# ```

# ### Quantitative comparisons: bar-charts

# ```python
# df = pd.read_csv('df.csv', index_col=0)
# fig, ax = plt.subplots()
# ax.bar(df.index, df["col_y"])
# plt.show()
# ```

# ```python
# df = pd.read_csv('df.csv', index_col=0)
# fig, ax = plt.subplots()
# ax.bar(df.index, df["col_y"])
# 
# ax.set_xticklabels(df.index, rotation=90) # rotate the tick labels
# ax.set_ylabel("y_label_string")
# 
# plt.show()
# ```

# ```python
# df = pd.read_csv('df.csv', index_col=0)
# fig, ax = plt.subplots()
# ax.bar(df.index, df["col_y1"])
# ax.bar(df.index, df["col_y2"], bottom= df['col_y1']) # visualizing other col, stacked bar chart
# 
# ax.set_xticklabels(df.index, rotation=90)
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ```python
# df = pd.read_csv('df.csv', index_col=0)
# fig, ax = plt.subplots()
# ax.bar(df.index, df["col_y1"])
# ax.bar(df.index, df["col_y2"], bottom= df['col_y1']) 
# ax.bar(df.index, df["col_y3"], bottom= df['col_y1'] + df['col_y2']) # visualizing other cols
# 
# ax.set_xticklabels(df.index, rotation=90)
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ```python
# df = pd.read_csv('df.csv', index_col=0)
# fig, ax = plt.subplots()
# ax.bar(df.index, df["col_y1"], label='y1')
# ax.bar(df.index, df["col_y2"], bottom= df['col_y1'], label='y2') 
# ax.bar(df.index, df["col_y3"], bottom= df['col_y1'] + df['col_y2'], label= 'y3')
# ax.set_xticklabels(df.index, rotation=90)
# ax.set_ylabel("y_label_string")
# 
# ax.legend() # adding labels and a legend
# 
# plt.show()
# ```

# ### Quantitative comparisons: histograms

# ```python
# fig, ax = plt.subplots()
# ax.hist(df["col_y"]) # introducing histograms
# ax.hist(df2["col_y"])
# ax.set_xlabel("x_label_string")
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots()
# ax.hist(df["col_y"], label='y1') 
# ax.hist(df2["col_y"], label='y2')
# ax.set_xlabel("x_label_string")
# ax.set_ylabel("y_label_string")
# ax.legend() # labels and legend
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots()
# ax.hist(df["col_y"], label='y1', 
#         bins=[150, 160, 170, 180, 190, 200, 210],
#         histtype="step") # customizing transparency
# ax.hist(df2["col_y"], label='y2',
#         bins=[150, 160, 170, 180, 190, 200, 210],
#         histtype="step")
# ax.set_xlabel("x_label_string")
# ax.set_ylabel("y_label_string")
# ax.legend() 
# plt.show()
# ```

# ### Statistical plotting

# ```python
# fig, ax = plt.subplots()
# 
# ax.bar("col_y1",
#        df["col_y"].mean(),
#        yerr=df["col_y"].std()) # adding error bars to bar charts
# ax.bar("col_y2",
#        df2["col_y"].mean(),
#        yerr=df2["col_y"].std())
# 
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots() # adding error bars to line plots
# 
# ax.errorbar(df["col_x"],
#             df["col_y"],
#             yerr=df["col_y_std"])
# 
# ax.errorbar(df2["col_x"],
#             df2["col_y"],
#             yerr=df2["col_y_std"])
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots() # adding boxplots
# 
# ax.boxplot((df["col_y"],
#             df2["col_y"])
#            
# ax.set_xticklabels(["df_label_string", "df2_label_string"])
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ### Quantitative comparisons: scatter plots

# ```python
# fig, ax = plt.subplots() # introducing scatter plots
# 
# ax.scatter((df["col_x"], df["col_y"])
#            
# ax.set_xlabel(["x_label_string"])
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ```python        
# eighties = df_time["1980-01-01":"1989-12-31"]
# nineties = df_time["1990-01-01":"1999-12-31"]
#            
# fig, ax = plt.subplots() 
# 
# ax.scatter(eighties["col_x"], eighties["col_y"],
#            color="red", label="eighties") # comparison by color
# ax.scatter(nineties["col_x"], nineties["col_y"],
#            color="blue", label="nineties")
# ax.legend()
# ax.set_xlabel("x_label_string")
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ```python
# fig, ax = plt.subplots()
# 
# ax.scatter((df_time["col_x"], df_time["col_y"],
#            c= df_time.index) # encoding a third variable by color
#            
# ax.set_xlabel(["x_label_string"])
# ax.set_ylabel("y_label_string")
# plt.show()
# ```

# ### Preparing figures to share with others

# ```python
# plt.style.use("ggplot") # choosing a style
# ```

# ```python
# plt.style.use("default") # back to default
# ```

# ```python
# plt.style.use("bmh") # bmh style
# ```

# ```python
# plt.style.use("seaborn-colorblind") # seaborn styles
# ```

# ### Saving figure

# ```python
# fig.savefig("figure.png") # saving the figure to file
# ```

# ```python
# fig.savefig("figure.jpg") # different file formats
# fig.savefig("figure.jpg", quality=50)
# fig.savefig("figure.svg")
# ```

# ```python
# fig.savefig("figure.png", dpi=300) # resolution
# ```

# ```python
# fig.set_size_inches([5, 3]) # size
# ```
