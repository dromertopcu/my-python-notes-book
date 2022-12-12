#!/usr/bin/env python
# coding: utf-8

# ## Cleaning Data in Python !!

# ### Data type constraints

# **String to integers**
# ```python
# #Import CSV file and output header 
# sales = pd.read_csv('sales.csv') 
# 
# # Get data types of columns 
# sales.dtypes
# 
# # Get DataFrame information 
# sales.info()
# 
# # Print sum of all Revenue column 
# sales['Revenue'].sum()
# 
# # Remove $ from Revenue column 
# sales['Revenue'] = sales['Revenue'].str.strip('$') sales['Revenue'] = sales['Revenue'].astype('int') 
# 
# # Verify that Revenue is now an integer 
# assert sales['Revenue'].dtype == 'int'
# 
# ```

# **The assert statement**
# ```python
# #This will pass 
# assert 1+1 == 2 
# 
# # This will not pass 
# assert 1+1 == 3 
# # Output : AssertionError                            
# #        Traceback (most recent call last)          
# #        assert 1+1 == 3 
# #        AssertionError: 
# ```

# **Numeric or categorical?**
# ```python
# df["marriage_status"] = df["marriage_status"].astype('category') df.describe()
# ```

# **How to find duplicate values?**
# ```python
# #Get duplicate rows 
# duplicates = height_weight.duplicated() 
# height_weight[duplicates] 
# ```

# ```python
# #Column names to check for duplication 
# column_names = ['first_name','last_name','address'] 
# duplicates = height_weight.duplicated(subset = column_names, keep = False)
# ```

# **Treating duplicate values**
# ```python
# #Group by column names and produce statistical summaries 
# column_names = ['first_name','last_name','address'] 
# summaries = {'height': 'max', 'weight': 'mean'} 
# height_weight = height_weight.groupby(by = column_names).agg(summaries).reset_index()  
# 
# # Make sure aggregation is done 
# duplicates = height_weight.duplicated(subset = column_names, keep = False) 
# height_weight[duplicates].sort_values(by = 'first_name') 
# 
# ```

# ### Membership constraints

# **Finding inconsistent categories**
# ```python
# inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type']) 
# 
# print(inconsistent_categories) 
# 
# # Get and print rows with inconsistent categories 
# inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)  
# 
# study_data[inconsistent_rows] 
# 
# ```

# **Dropping inconsistent categories**
# ```python
# # Drop inconsistent categories and get consistent data only
# consistent_data = study_data[~inconsistent_rows]
# 
# ```

# ### Categorical Variables

# **Value consistency**
# ```python
# marriage_status = demographics['marriage_status'] 
# marriage_status.value_counts() 
# ```

# ```python
# marriage_status.groupby('marriage_status').count() 
# ```

# ```python
# # Capitalize  
# marriage_status['marriage_status'] = marriage_status['marriage_status'].str.upper() 
# 
# marriage_status['marriage_status'].value_counts()
# ```

# ```python
# # Lowercase
# marriage_status['marriage_status'] = marriage_status['marriage_status'].str.lower() 
# 
# marriage_status['marriage_status'].value_counts()
# ```

# ```python
# # Strip all spaces
# demographics = demographics['marriage_status'].str.strip() 
# 
# demographics['marriage_status'].value_counts()
# ```

# **Collapsing data into categories
# ```python
# # Using qcut() 
# import pandas as pd 
# group_names = ['First one', 'Second one', 'Third one'] 
# demographics['income_group'] = pd.qcut(demographics['household_income'], q = 3,                                         labels = group_names) 
# # Print income_group column 
# demographics[['income_group', 'household_income']]
# ```

# ```python
# # Using cut() - create category ranges and names 
# ranges = [0,200000,500000,np.inf] 
# group_names = ['0-200K', '200K-500K', '500K+'] 
# # Create income group column 
# demographics['income_group'] = pd.cut(demographics['household_income'], bins=ranges, labels=group_names) 
# 
# demographics[['income_group', 'household_income']]
# ```

# ```python
# # Create mapping dictionary and replace 
# mapping = {'Microsoft':'DesktopOS', 'MacOS':'DesktopOS', 'Linux':'DesktopOS','IOS':'MobileOS', 'Android':'MobileOS'} 
# 
# devices['operating_system'] = devices['operating_system'].replace(mapping) 
# 
# devices['operating_system'].unique() 
# ```

# ### Uniformity

# ```python
# temp_fah = temperatures.loc[temperatures['Temperature'] > 40, 'Temperature']  
# 
# temp_cels = (temp_fah - 32) * (5/9) 
# 
# temperatures.loc[temperatures['Temperature'] > 40, 'Temperature'] = temp_cels
# 
# #Assert conversion is correct 
# assert temperatures['Temperature'].max() < 40
# ```

# **Completeness**
# ```python
# # Get summary of missingness 
# airquality.isna().sum()
# ```

# **Missingno**
# ```python
# import missingno as msno 
# import matplotlib.pyplot as plt 
# 
# #Visualize missingness 
# msno.matrix(airquality) 
# plt.show()
# ```

# **Missingno**
# ```python
# #Isolate missing and complete values aside 
# missing = airquality[airquality['CO2'].isna()] 
# complete = airquality[~airquality['CO2'].isna()]
# 
# complete.describe()
# missing.describe()
# ```

# **Replacing with statistical measures**
# ```python
# co2_mean = airquality['CO2'].mean() 
# 
# airquality_imputed = airquality.fillna({'CO2': co2_mean}) 
# ```

# ### Comparing strings

# **Minimum edit distance algorithms**
# Algorithm                 Operations
# 
# Damerau-Levenshtein       insertion, substitution, deletion, transposition
# 
# Levenshtein               insertion, substitution, deletion
# 
# Hamming                   substitution only
# 
# Jaro distance             transposition only
# 
# Possible packages: nltk , fuzzywuzzy , textdistanc
# ```python
# # Lets us compare between two strings 
# from fuzzywuzzy import fuzz   
# 
# # Compare reeding vs reading 
# 
# fuzz.WRatio('Reeding', 'Reading') 
# ```

# **Partial strings and different orderings**
# ```python
# # Partial string comparison 
# 
# fuzz.WRatio('Houston Rockets', 'Rockets') 
# 
# # Partial string comparison with different order 
# 
# fuzz.WRatio('Houston Rockets vs Los Angeles Lakers', 'Lakers vs Rockets')
# ```

# **Comparison with arrays**
# ```python
# # Import process 
# from fuzzywuzzy import process 
# 
# # Define string and array of possible matches 
# 
# string = "Houston Rockets vs Los Angeles Lakers" 
# choices = pd.Series(['Rockets vs Lakers', 'Lakers vs Rockets',                       'Houson vs Los Angeles', 'Heat vs Bulls']) 
# 
# process.extract(string, choices, limit = 2)
# # Output:
# # [('Rockets vs Lakers', 86, 0), ('Lakers vs Rockets', 86, 1)]
# ```

# **Collapsing all of the state : Categories with string similarity**
# ```python
# # For each correct category 
# for state in categories['state']:    
#     # Find potential matches in states with typoes     
#     matches = process.extract(state, survey['state'], limit = survey.shape[0])      
#     # For each potential match match     
#     for potential_match in matches:        
#         # If high similarity score         
#         if potential_match[1] >= 80:            
#             # Replace typo with correct category   
#             survey.loc[survey['state'] == potential_match[0], 'state'] = state 
# 
# ```

# **Generating pairs**
# ```python
# # Import recordlinkage 
# import recordlinkage   
# 
# # Create indexing object 
# indexer = recordlinkage.Index()  
# 
# # Generate pairs blocked on state 
# indexer.block('state') 
# pairs = indexer.index(census_A, census_B)
# 
# ```

# **Comparing the DataFrames**
# ```python
# # Generate the pairs 
# pairs = indexer.index(census_A, census_B)  
# 
# # Create a Compare object 
# compare_cl = recordlinkage.Compare()  
#  
# # Find exact matches for pairs of date_of_birth and state 
# compare_cl.exact('date_of_birth', 'date_of_birth', label='date_of_birth') 
# compare_cl.exact('state', 'state', label='state')   
# 
# # Find similar matches for pairs of surname and address_1 using string similarity 
# compare_cl.string('surname', 'surname', threshold=0.85, label='surname') 
# compare_cl.string('address_1', 'address_1', threshold=0.85, label='address_1')   
#  
# # Find matches 
# potential_matches = compare_cl.compute(pairs, census_A, census_B)
# 
# ```

# **Finding the only pairs we want**
# ```python
# matches = potential_matches[potential_matches.sum(axis = 1) >= 2]
# ```

# ### Linking DataFrames

# **Get the indices**
# ```python
# # Get indices from census_B only 
# duplicate_rows = matches.index.get_level_values(1) 
# print(census_B_index)
# 
# # Finding duplicates in census_B 
# census_B_duplicates = census_B[census_B.index.isin(duplicate_rows)]  
# 
# # Finding new rows in census_B 
# census_B_new = census_B[~census_B.index.isin(duplicate_rows)]
# 
# # Link the DataFrames! 
# full_census = census_A.append(census_B_new) 
# ```
