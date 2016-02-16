# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This file is part of ycas: https://github.com/felgari/snippets
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

# Length of a vector.
length(the_vector)

# Get the first index of a vector where any of a set of values is found.
indexes <- match(c(val1, val2), the_vector)

# Get the indexes of a vector where a value is found.
indexes <- which(the_vector %in% c(val1, val2))

# Get a new vector that only contains one instance of each element.
unique(the_vector)

# Sort a vector.
sort(the_vector)

# Replace value in a vector that match a condition with another value.
the_vector[which(the_vector == old_value)] <- new_value

# Walk a vector by index.
for ( i in 1:length(the_vector) ) {
	the_vector[i] ...
}