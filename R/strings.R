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

# Concatenate strings.
cat(string_1, string_2, string_3)
paste0(string_1, string_2)
# Concatenate strings with a space between them.
paste(string_1, string_2)

# Get a string formatted as a C printf.
sprintf("%s %d", the_string, a_number)

# Length of a string.
nchar(the_string)

# Get a substring.
substr(the_string, start_pos, end_pos)

# Replace a subtring.
sub( perl_pattern, replacement_string, the_string, perl=TRUE )