#!/usr/bin/env python
# coding: utf-8

# ## Working with Dates and Times in Python

# ### Dates in Python

# **Creating date objects**
# ```python
# #Import date 
# from datetime import date 
# #Create dates 
# two_hurricanes_dates = [date(2016, 10, 7), date(2017, 6, 21)] 
# 
# print(two_hurricanes_dates[0].year) 
# print(two_hurricanes_dates[0].month) 
# print(two_hurricanes_dates[0].day) 
# print(two_hurricanes_dates[0].weekday()) 
# ```

# ### Math with dates

# ```python
# #Import date 
# from datetime import date  
# #Create our dates 
# d1 = date(2017, 11, 5)
# d2 = date(2017, 12, 4)
# 
# #Subtract two dates 
# delta = d2 - d1 
# print(delta.days)
# ```

# **Timedelta**
# ```python
# #Import timedelta 
# from datetime import timedelta  
# 
# #Create a 29 day timedelta 
# td = timedelta(days=29) 
# print(d1 + td)
# ```

# ### Turning dates into strings

# **ISO 8601 format**
# ```python
# from datetime import date  
# #Example date 
# d = date(2017, 11, 5)   
# 
# #ISO format: YYYY-MM-DD 
# print(d) 
# 
# #Express the date in ISO 8601 format and put it in a list 
# print( [d.isoformat()] ) 
# ```

# **Every other format: strftime**
# ```python
# #Example date 
# d = date(2017, 1, 5)  
# print(d.strftime("%Y"))
# #Output: 2017
# 
# #Format string with more text in it 
# print(d.strftime("Year is %Y")) 
# #Output: Year is 2017 
# 
# #Format: YYYY/MM/DD 
# print(d.strftime("%Y/%m/%d")) 
# #Output: 2017/01/05 
# ```

# ### Adding time to the mix

# **Dates and Times**
# ```python
# #Import datetime 
# from datetime import datetime 
# dt = datetime(2017, 10, 1, 15, 23, 25, 500000) 
# 
# dt = datetime(year=2017, month=10, day=1, hour=15, minute=23, second=25, microsecond=500000)
# ```

# **Replacing parts of a datetime**
# ```python
# dt_hr = dt.replace(minute=0, second=0, microsecond=0) 
# print(dt_hr)
# ```
