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

import csv
import pyfits

CSV_MIN_NUM_OF_ITEMS = 2
FIELD_NAME = "EXPOSURE"

""" 
File names.
-------------------------------------------------------------------------------
"""
# Get the path and the name of a complete file name.
import os
path, file_name = os.path.split(complete_file_name)

# Build the complete name of a file using a path and the file name.
import os
complete_file_name = os.path.join(path, file_name)

# Returns a string that contains only the part with the names of the directories.
import os
os.path.basename(path)

# Get a list whose elements are the parts of the path.
import os
path_splitted = os.path.split(os.sep)

""" 
Directories.
-------------------------------------------------------------------------------
"""

# Get all the files names in a path with a given extension.    
import glob
files_full_path = [f for f in glob.glob(os.path.join(path, "*." + FILE_EXT))]

""" 
Text files.
-------------------------------------------------------------------------------
"""

def read_text_file(file_name):
    """Read a text file.
    
    Args:
        file_name: Name of the file to read.
    
    Returns:
        ?
        
    """    
    
    try:
        with open(file_name, "r") as f:
            for line in f:
                
                # Process text line.        
                pass
        
    except IOError as ioe:
         print "Error reading text file: '%s'" % file_name  

"""
CSV files.
-------------------------------------------------------------------------------
"""

def read_csv_file(file_name):
    """Read a CSV file.
    
    Args:
        file_name: Name of the file to read.
    
    Returns:
        ?
        
    """
    
    try:
        with open(file_name, "rb") as fr:
            
            reader = csv.reader(fr, delimiter=',', quotechar='"')        
            
            for row in reader:   
                 
                # Check minimum.number of elements.
                if len(row) < CSV_MIN_NUM_OF_ITEMS:
                     
                    # Process CSV line.
                    pass
                
    except csv.Error as e:
        print "Error reading data from CSV file: '%s'" % file_name 
                
    except IOError as ioe:
        print "Error reading CSV file: '%s'" % file_name   
        
def write_csv_file(file_name, data):
    """Write a CSV file.
    
    Args:
        file_name: Name of the file to write.
    
    Returns:
        ?
        
    """    
    
    try:                
        with open(file_name, 'wb') as fw:
            
            writer = csv.writer(fw, delimiter='\t')
    
            # Walk the data.
            for d in data:
            
                # Write a row.
                writer.writerow(d)   
    except csv.Error as e:
        print "Error writing data in CSV file: '%s'" % file_name                
                
    except IOError as ioe:
        print "Error writing CSV file: '%s'" % file_name        
        
"""
FIT files.
-------------------------------------------------------------------------------
"""

def open_fit_file(file_name):
    """Read a FIT file.
    
    Args:
        file_name: Name of the file to open
    
    Returns:
        ?
        
    """       
    
    try:
        # Open FIT file.
        hdulist = pyfits.open(file_name)
        
        # Get header of first hdu, only one hdu is used.
        header = hdulist[0].header
        
        header_field_value = header[FIELD_NAME]
        
        # Process header value.
        pass
        
        hdulist.close() 
    except IOError as ioe:
        print "Error reading fit file '%s'. Error is: %s" % (file_name, ioe)
    except KeyError as ke:
        print "Header field not found in file: '%s'" % file_name   
    except:
        print "Unknown error reading fit file: '%s'" % file_name                          