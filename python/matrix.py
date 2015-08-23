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
Matrix.
-------------------------------------------------------------------------------
"""

NUM_OF_COL = 10
NUM_OF_ROW = 10

# Create a matrix with NUM_OF_ROW rows and NUM_OF_COL columns.
matrix = [[0 for x in range(NUM_OF_COL)] for x in range(NUM_OF_ROW)]

# Assign a value to a cell of the matrix.
matrix[row][col] = val 

# Get the value of a cell of the matrix.
val = matrix[row][col]