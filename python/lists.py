# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This file is part of code-snippets: https://github.com/felgari/snippets
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

""" 
Lists.
-------------------------------------------------------------------------------
"""

# Creating some lists.
l = []
sublist = []

# Creating a list with the elements of the list given repeated NUMBER times.
final_list = source_list * NUMBER

# Creating a matrix filled with 0 values.
[[ 0 for _ in range(num_col)] for _ in range(num_row)]

# Insert an item at the beginning of a list.
the_list.insert(0, item)
item_list + the_list

# Copy a list.
the_list = source_list[:]

# Flatten a list.
[item for sublist in l for item in sublist]

# Get a sublist with the elements that accomplisehd the condition.
[ x for x in the_list if x > 0 ]

# Remove empty strings from a list of strings.
the_list = filter(len, source_list)

# Getting a string of file names from a list containing the file names.
list_of_files = str(list_with_files_names).translate(None, "[]\'")

# Getting a range to iterate over a list in reverse order.
range(len(l)-1,-1,-1)

# Getting a list where the elements are the characters of the strings
# contained in another list.
# Ex: l = [ 'A', 'BC', 'DE F' ] -> ['A', 'B', 'C', 'D', 'E', ' ', 'F'] 
import itertools
list(itertools.chain.from_iterable(source_list))

# Extract a column from a numpy array (column is zero based).
here_my_numpy_array[:,column_number]

# Concatenate elements of a list using a fixed string as separator.
','.join(the_list)

# Generate a list from a string whose elements are substrings delimited by separators.
the_list = data_line.split(separator)

# Get a list sorted using the first item of each element.
sorted(the_list, key=lambda a_element: a_element[0])

# Sort the characters of a string.
''.join(sorted(the_string[i]))

# Sort rows of a list by a column, keeping the position of each column.
import numpy as np
here_my_numpy_array[here_my_numpy_array[:,here_my_column_number].argsort()]