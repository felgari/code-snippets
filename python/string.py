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
Strings.
-------------------------------------------------------------------------------
"""

# Remove empty characters at the start and the end of a string.
the_string.strip()

# Find the position of a string into another, returns -1 if not found.
pos = the_string.find(string_to_find)

# Find the last position (find begins at the right) of a string into another, 
# returns -1 if not found.
pos = the_string.rfind(string_to_find)

# Check if a string starts with a given substring.
the_string.startswith(substring)

# Replace in a string a given substring with another.
the_string.replace(substring_1, substring_2)

# Get a string of file names from a list containing the file names.
list_of_files = str(list_with_strings).translate(None, "[]\'")

# Generate a list from a string whose elements are substrings delimited by separators.
the_list = the_string.split(separator)

# Putting leading zeros when converting integer to string 
# (Add 0 in this case if necessary to get two digits).
str(the_int).zfill(2)