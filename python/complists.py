#!/usr/bin/env python
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

import sys
import os

MIN_ARGS = 3

def get_file_lines_sorted(file):
    
    lines = []
    
    try:
        with open(file, "r") as f:
            for line in f:
                
                lines.append(line)
        
    except IOError as ioe:
         print "Error reading file: '%s'" % file_name  
         
    return sorted(lines) 

def compare_files(file1, file2):
    
    lines_in_1_not_in_2 = []
    lines_in_2_not_in_1 = []
    
    lines1 = get_file_lines_sorted(file1)
    lines2 = get_file_lines_sorted(file2)
        
    n1 = 0
    n2 = 0
    while n1 < len(lines1) and n2 < len(lines2):
        l1 = lines1[n1].strip()
        l2 = lines2[n2].strip()
        
        if l1 < l2:
            lines_in_1_not_in_2.append(l1)
            n1 += 1
        elif l1 == l2:
            n1 += 1
            n2 += 1
        else:
            lines_in_2_not_in_1.append(l2)
            n2 += 1
            
    if len(lines_in_1_not_in_2) > 0:
        print "Lines only in first file: %s" % lines_in_1_not_in_2 
        
    if len(lines_in_2_not_in_1) > 0:
        print "Lines only in second file: %s" % ", ".join(lines_in_2_not_in_1) 
        
    if len(lines_in_1_not_in_2) == 0 and len(lines_in_2_not_in_1) == 0:
        print "Both files have the same lines."                  

if __name__ == "__main__":
    
    if len(sys.argv) < MIN_ARGS:
        print "Error, not enough parameters. Use: %s file1 file2" % \
            sys.argv[0]
    else:
        
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        
        if not os.path.exists(file1):
            print "File %s doesn't exist." % file1
        elif not os.path.exists(file2):
            print "File %s doesn't exist." % file2
        else:
            print "Comparing files %s and %s" % (file1, file2)
            compare_files(file1, file2)