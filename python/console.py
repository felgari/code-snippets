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
Console.
-------------------------------------------------------------------------------
"""

# An infinite loop that exits when Ctrl-C is pressed.
exit = False

while not exit:
    try:       
        
        # Do processing
        pass
                         
    # To catch a Ctrl-C.
    except KeyboardInterrupt:
        exit = True
        print "Exiting, Ctrl-C. pressed"