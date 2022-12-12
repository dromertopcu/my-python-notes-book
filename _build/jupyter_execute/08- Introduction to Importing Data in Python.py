#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Importing Data in Python

# ### Introduction to Importing 

# **Reading a text file**
# 
# 
# ```python
# filename = 'huck_finn.txt'  
# file = open(filename, mode='r')  # 'r' is to read  
# text = file.read()  
# 
# 
# print(file.closed) # Check whether file is closed
# 
# file.close() 
# ```

# **Printing a text file**
# ```python
# print(text)
# ```

# **Writing to a file**
# ```python
# filename = 'huck_finn.txt' 
# file = open(filename, mode='w')  # 'w' is to write 
# file.close() 
# 
# ```

# **Context manager with**
# ```python
# with open('huck_finn.txt', 'r') as file:     
#     print(file.read()) 
# ```

# ```python
# with open('huck_finn.txt', 'r') as file:     
#     print(file.readline())
#     print(file.readline())
# ```

# ### Importing flat files using NumPy

# ```python
# import numpy as np 
# filename = 'MNIST.txt' 
# data = np.loadtxt(filename, delimiter=',') 
# data 
# ```

# **Customizing your NumPy import**
# ```python
# import numpy as np 
# filename = 'MNIST_header.txt' 
# data = np.loadtxt(filename, delimiter=',', skiprows=1,usecols=[0, 2]) 
# print(data)
# ```

# **Visualizing NumPy import**
# ```python
# # Import package
# import numpy as np
# import matplotlib.pyplot as plt
# 
# # Assign filename to variable: file
# file = 'digits.csv'
# 
# # Load file as array: digits
# digits = np.loadtxt(file, delimiter=',')
# 
# # Print datatype of digits
# print(type(digits))
# 
# # Select and reshape a row
# im = digits[21, 1:]
# im_sq = np.reshape(im, (28, 28))
# 
# # Plot reshaped data ()
# plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
# plt.show()
# 
# ```

# **Mixed Data Types**
# ```python
# data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)
# 
# data = np.recfromcsv('titanic.csv') # default dtype=None
# ```

# ```python
# data = np.loadtxt(filename, delimiter=',', dtype=str)
# ```

# ### Importing flat files using Pandas

# **Importing using Pandas**
# ```python
# import pandas as pd 
# filename = 'winequality-red.csv' 
# data = pd.read_csv(filename, nrows=5) 
# data.head()
# ```

# ```python
# data_array = data.values 
# ```

# ```python
# data = pd.read_csv('titanic_corrupt.txt', sep='\t', comment='#', na_values='Nothing')
# ```

# ### Introduction to other file types

# **Pickled files**
# ```python
# import pickle 
# with open('pickled_fruit.pkl', 'rb') as file:     
#     data = pickle.load(file)     
# print(data) 
# ```

# **Excel spreadsheets**
# ```python
# import pandas as pd 
# file = 'urbanpop.xlsx' 
# data = pd.ExcelFile(file) 
# print(data.sheet_names)
# 
# df1 = data.parse('sheet1') # sheet name, as a string 
# df2 = data.parse(0, usecols=['Country'], skiprows=[0], names=['Country']) # sheet index, as a float 
# ```

# **SAS files**
# ```python
# import pandas as pd 
# from sas7bdat import SAS7BDAT 
# with SAS7BDAT('urbanpop.sas7bdat') as file:     
#     df_sas = file.to_data_frame()
# ```

# **Stata files**
# ```python
# import pandas as pd 
# data = pd.read_stata('urbanpop.dta') 
# ```

# **HDF5 files**
# ```python
# #Hierarchical Data Format version 5
# 
# import h5py 
# filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5' 
# data = h5py.File(filename, 'r') # 'r' is to read 
# print(type(data))
# ```

# **Structure of HDF5 files**
# ```python
# for key in data.keys():     
#     print(key)
#     
# print(type(data['meta']))
# 
# for key in data['meta'].keys():     
#     print(key)
#     
# print(np.array(data['meta']['Description']), np.array(data['meta']['Detector']))
# ```

# **MATLAB files**
# ```python
# scipy.io.loadmat() # read .mat files
# scipy.io.savemat() # write .mat files
# ```

# ```python
# import scipy.io 
# filename = 'workspace.mat' 
# 
# mat = scipy.io.loadmat(filename)  
#  
# print(type(mat) # <class 'dict'>
# ```

# ### Relational databases

# **Creating a database engine**
# ```python
# from sqlalchemy import create_engine 
# 
# engine = create_engine('sqlite:///Northwind.sqlite') 
# 
# table_names = engine.table_names() 
# print(table_names)
# ```

# **Querying relational databases**
# ```python
# from sqlalchemy import create_engine 
# import pandas as pd   
# engine = create_engine('sqlite:///Northwind.sqlite')  
# con = engine.connect()  
# rs = con.execute("SELECT * FROM Orders")  
# df = pd.DataFrame(rs.fetchall())  
# con.close()
# ```

# **Using the context manager**
# ```python
# from sqlalchemy import create_engine 
# import pandas as pd   
# engine = create_engine('sqlite:///Northwind.sqlite') 
# 
# with engine.connect() as con:     
#     rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")     
#     df = pd.DataFrame(rs.fetchmany(size=5))     
#     df.columns = rs.keys() 
# 
# ```

# **The pandas way to query**
# ```python
# from sqlalchemy import create_engine 
# import pandas as pd   
# engine = create_engine('sqlite:///Northwind.sqlite') 
# 
# df = pd.read_sql_query("SELECT * FROM Orders", engine) 
# 
# ```

# **Advanced querying**
# ```python
# from sqlalchemy import create_engine 
# import pandas as pd 
# engine = create_engine('sqlite:///Northwind.sqlite') 
# df = pd.read_sql_query("SELECT OrderID, CompanyName FROM Orders  INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID", engine) 
# 
# print(df.head()) 
# 
# ```
