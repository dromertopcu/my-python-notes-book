#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Numpy

# ```python
# import numpy as np
# python_list = [3, 2, 5, 8, 4, 9, 7, 6, 1]
# array = np.array(python_list) # creating 1D arrays from lists
# ```

# ```python
# python_list_of_lists = [[3, 2, 5],
#                         [9, 7, 1],
#                         [4, 3, 6]]
# array = np.array(python_list_of_lists) # creating 2D arrays from lists
# ```

# NumPy arrays
# * Can contain only a single data type
# * Use less space in memory

# ```python
# #creating arrays from scratch
# np.zeros((5, 3))
# np.random.random((2, 4)) # 2 row 4 column
# np.arange(-3, 4)
# ```

# ```python
# .shape # array attribute
# 
# .flatten() # array methods
# .reshape()
# 
# 
# ```

# ### Numpy data types 

# Sample NumPy data types:
# * np.int64
# * np.int32
# * np.float64
# * np.float32

# ```python
# .dtype #attribute
# ```

# ```python
# boolean_array = np.array([[True, False], [False, False]], dtype=np.bool_) #dtype as an argument
# 
# boolean_array.astype(np.int32) # type conversion
# ```
# ```
# array([[1, 0],
#        [0, 0]], dtype=int32)
# ```

# ```python
# np.array([True, "Boop", 42, 42.42]) # type coercion
# ```
# ```
# array(['True', 'Boop', '42', '42.42'], dtype='<U5')
# ```

# ### Sorting arrays

# ```python
# np.sort(array) # default axis=1 sorting rows
# np.sort(array, axis=0) # sorting columns
# ```

# ### Filtering arrays

# ```python
# np.where(array[:, 1] % 2 == 0)
# ```
# ```
# (array([0, 3]),) # returns array of indices
# ```

# ```python
# row_ind, column_ind = np.where(array == 0)
# row_ind, column_ind
# ```
# ```
# (array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]),
# array([0, 1, 4, 5, 7, 0, 1, 3, 4, 6, 7, 0, 2, 3, 5, 6, 0, 1, 3, 4, 6, 2,3, 4, 7, 8, 0, 2, 3, 6, 7, 8, 1, 2, 3, 4, 5, 7, 0, 1, 4, 8, 0, 5, 7, 8]))
# ```

# ```python
# np.where(array == 0, "", array) #find and replace
# ```

# ### Adding and removing data

# ```np.concatenate()``` concatenates along the first axis by default.
# ```python
# np.concatenate((array1, array2)) #concatenating rows
# ```

# ```python
# np.concatenate((array1, array2), axis=1) #concatenating columns
# ```

# ```python
# array_1D = np.array([1, 2, 3])
# column_array_2D = array_1D.reshape((3, 1)) # creating compatibility
# row_array_2D = array_1D.reshape((1, 3))
# ```

# ```python
# np.delete(array, 1, axis=0) # deleting with np.delete() (deleting second row)
# np.delete(array, 1, axis=1) # deleting second column
# np.delete(array, 1) # deleting without axis (flattened and deleting second item)
# ```

# ### Summarizing data

# ```python
# array.sum() # summing all data
# array.sum(axis=0) # summing along column and making a sum row
# array.sum(axis=1) # summing along row and making a sum column
# ```

# ```python
# array.min() # min of all data
# array.min(axis=0) # min of column and making a min row
# ```

# ```python
# array.mean() # mean of all data
# array.mean(axis=1) # mean of row and making a mean column
# ```

# ```python
# array.sum(axis=1, keepdims=True) # keeping dimension same
# ```

# ```python
# array.cumsum(axis=0) # cumulative sums summing along column
# ```

# ```python
# cum_sums_array = array.cumsum(axis=0) # graphing summary values
# plt.plot(np.arange(1, 6), cum_sums_array[:, 0], label="col_1")
# plt.plot(np.arange(1, 6), cum_sums_array.mean(axis=1), label="Average")
# plt.legend()
# plt.show()```

# ### Vectorized Operations

# ```python
# np.arange(1000000).sum() # little help from C. faster than python
# array + 3
# array * 3 # multiplying by scalar
# array_1+array_2 # adding two arrays together
# array_1*array_2 # multiplying two arrays together
# array > 2 # not just for math making boolean list
# ```

# ```python
# array = np.array(["NumPy", "is", "awesome"])
# len(array) > 2
# ```
# ```
# True
# ```

# ```python
# vectorized_len = np.vectorize(len) # vectorizing functions
# 
# vectorized_len(array) > 2
# ```
# ```
# array([ True, False, True])
# ```

# ### Broadcasting

# **Compatibility rules**
# * NumPy compares sets of array dimensions from right to left.
# * Two dimensions are compatible when...
#     * One of them has a length of one or
#     * They are of equal lengths
# * All dimension sets must be compatible

# |Broadcastable shapes:|Shapes which are not broadcastable:|
# |---------------------|-----------------------------------|
# |```(10, 5)``` and ```(10, 1)```|```(10, 5)``` and ```(5, 10)```|
# |```(10, 5)``` and ```(5, )```|```(10, 5)``` and ```(10, )```

# ```python
# array = np.arange(10).reshape((2, 5))
# array + np.array([0, 1, 2, 3, 4])
# ```
# ```
# array([[ 0, 2, 4, 6, 8],
#        [ 5, 7, 9, 11, 13]])
# ```

# ```python
# array = np.arange(10).reshape((2, 5))
# array + np.array([0, 1])
# ```
# ```
# ValueError: operands could not be broadcast together with shapes (2,5) (2,)
# ```

# ### Saving and loading arrays

# ```python
# rgb = np.array([[[255, 0, 0], [255, 0, 0], [255, 0, 0]],
#                 [[0, 255, 0], [0, 255, 0], [0, 255, 0]],
#                 [[0, 0, 255], [0, 0, 255], [0, 0, 255]]])
# plt.imshow(rgb)
# plt.show()
# ```

# ```python
# with open("logo.npy", "rb") as f: # loading .npy files
#     logo_rgb_array = np.load(f)
# plt.imshow(logo_rgb_array)
# plt.show()
# ```
# Save arrays in many formats:
# * .csv
# * .txt
# * .pkl
# * .npy

# ```python
# red_array = logo_rgb_array[:, :, 0] # examining rgb data
# blue_array = logo_rgb_array[:, :, 1]
# green_array = logo_rgb_array[:, :, 2]
# ```

# ```python
# dark_logo_array = np.where(logo_rgb_array == 255, 50, logo_rgb_array) # updating rgb data
# plt.imshow(dark_logo_array)
# plt.show()
# ```

# ```python
# with open("dark_logo.npy", "wb") as f:
#     np.save(f, dark_logo_array) # saving array as .npy file
# ```

# ### Array acrobatics

# ```python
# flipped_logo = np.flip(logo_rgb_array) # it flipped colors also
# plt.imshow(flipped_logo)
# plt.show()
# ```

# ```python
# flipped_rows_logo = np.flip(logo_rgb_array, axis=0) # fliping along an axis (horizontal mirroring)
# plt.imshow(flipped_rows_logo)
# plt.show()
# ```

# ```python
# flipped_colors_logo = np.flip(logo_rgb_array, axis=2) # flipping only colors
# plt.imshow(flipped_colors_logo)
# plt.show()
# ```

# ```python
# flipped_colors_logo = np.flip(logo_rgb_array, axis=(0,1)) # flipping without colors (horizontal and vertical mirroring)
# plt.imshow(flipped_colors_logo)
# plt.show()
# ```

# ```python
# array = np.array([[1.1, 1.2, 1.3],
#                   [2.1, 2.2, 2.3],
#                   [3.1, 3.2, 3.3],
#                   [4.1, 4.2, 4.3]])
# np.flip(array) # flipping an array(without axis, all axis flipped)
# ```
# ```
# array([[4.3, 4.2, 4.1],
#        [3.3, 3.2, 3.1],
#        [2.3, 2.2, 2.1],
#        [1.3, 1.2, 1.1]])
# ```
# 

# ```python
# array = np.array([[1.1, 1.2, 1.3],
#                   [2.1, 2.2, 2.3],
#                   [3.1, 3.2, 3.3],
#                   [4.1, 4.2, 4.3]])
# np.transpose(array) # transposing an array
# ```
# ```
# array([[1.1, 2.1, 3.1, 4.1],
#        [1.2, 2.2, 3.2, 4.2],
#        [1.3, 2.3, 3.3, 4.3]])
# ```
# 

# ```python
# transposed_logo = np.transpose(logo_rgb_array, axes=(1, 0, 2)) # setting transposed axis order(without changing colors) (mirroring crossed axes )
# plt.imshow(transposed_logo)
# plt.show()
# ```

# ### Stacking and splitting

# ```python
# rgb = np.array([[[255, 0, 0], [255, 255, 0], [255, 255, 255]],
#                 [[255, 0, 255], [0, 255, 0], [0, 255, 255]],
#                 [[0, 0, 0], [0, 255, 255], [0, 0, 255]]])
# red_array = rgb[:, :, 0]
# blue_array = rgb[:, :, 1]
# green_array = rgb[:, :, 2]
# red_array
# ```
# ```
# array([[255, 255, 255],
#        [255, 0, 0],
#        [255, 0, 0]])
# ```
# ```python
# red_array.shape
# ```
# ```
# (3, 3)
# ```

# ```python
# red_array, green_array, blue_array = np.split(rgb, 3, axis=2) # splitting array
# red_array
# ```
# ```
# array([[[255], [255], [255]],
#        [[255], [ 0], [ 0]],
#        [[255], [ 0], [ 0]]])
# ```
# ```python
# red_array.shape
# ```
# ```
# (3, 3, 1)
# ```

# ```python
# red_array_2D = red_array.reshape((3, 3)) # trailing dimensions
# red_array_2D
# ```
# ```
# array([[255, 255, 255],
#        [255, 0, 0],
#        [255, 0, 0]])
# ```
# ```python
# red_array_2D.shape
# ```
# ```
# (3, 3)
# ```

# ```python
# red_array, green_array, blue_array = np.split(rgb, 5, axis=2)
# ```
# ```
# ValueError: array split does not result in an equal division
# ```

# ```python
# red_array, green_array, blue_array = np.split(logo_rgb_array, 3, axis=2)
# plt.imshow(red_array) # plotting 2D image data
# plt.show()
# ```

# ```python
# red_array = np.zeros((1001, 1001)).astype(np.int32) # changing red array
# green_array = green_array.reshape((1001, 1001))
# blue_array = blue_array.reshape((1001, 1001))
# ```

# ```python
# stacked_rgb = np.stack([red_array, green_array, blue_array], axis=2) # stacking 2D arrays
# plt.imshow(stacked_rgb)
# plt.show()
# ```
