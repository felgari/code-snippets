# -*- coding: utf-8 -*-

# Copyright (c) 2015 Felipe Gallego. All rights reserved.
#
# This file is part of code-snippets: https://github.com/felgari/code-snippets
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

here_my_numpy_array = np.array()

# Insert at the beginning of a list.
my_list(l, item)

# Flatten a list.
[item for sublist in l for item in sublist]

# Remove empty strings from a list of strings.
l = filter(len, l)

# Getting a string of file names from a list containing the file names.
list_of_files = str(list_with_files_names).translate(None, "[]\'")

# Getting a range to iterate over a list in reverse order.
range(len(l)-1,-1,-1)

import itertools
list(itertools.chain.from_iterable(l))

import numpy as np
# Sort rows of a list by a column, keeping the position of each column.
here_my_numpy_array[here_my_numpy_array[:,here_my_column_number].argsort()]

# Extract a column from a numpy array (column is zero based).
here_my_numpy_array[:,column_number]