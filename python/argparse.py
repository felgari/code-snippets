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

# Template for a class that uses argparse.

import argparse

class ProgramArgumentsException(Exception):
    """ A minimum class for exceptions processing program arguments. """
    
    def __init__(self, msg):
        
        self._msg = msg
        
    def __str__(self):
        return self._msg

class ProgramArguments(object):
    """Encapsulates the definition and processing of program arguments.
	
	"""
    
    # Constants


    def __init__(self):
        """Initializes parser. 
        
        Initialization of variables and the object ProgramArguments 
        with the definition of arguments to use.

        """   
        
        # Initializes variables with default values.  
    
        
        self._min_number_of_args = 1             
                
        self._args = None   
        
        self._parser = None                                              
        
        # Properties that return values of program arguments.

    
    def init_parser(self):
        """Initializes the ArgumentParser object.
		
		"""
        
        self._parser = argparse.ArgumentParser()
        
        # Initialize arguments of the parser.        
        self._parser.add_argument("-file", dest="file", metavar="file", 
                                  help="A program argument with a file.")
        self._parser.add_argument("-bool", dest="bool", action="store_true", 
                                  help="A program argument for a bool value.")

    def parse_and_update(self):
        """Parse the program arguments and update attributes.
		
		"""

        try:
            # Parse program arguments.        
            self._args = self._parser.parse_args()
    
            # Process self._args to check values and update attributes.
            
        except argparse.ArgumentError as ae:
            print ae.message
            raise ProgramArgumentsException(ae.message)                         
                
    def process_program_arguments(self):
        """Parse and check coherence of program arguments.
		
		"""     
        
        self.init_parser() 

        self.parse_and_update()
 
    def print_usage(self):
        """Print arguments options.
		
		"""
                
        self._parser.print_usage()     
        
    def print_help(self):
        """Print help for arguments options.
		
		"""
                
        self._parser.print_help()