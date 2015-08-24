# Template for a class that uses argparse.

import argparse

class ProgramArgumentsException(Exception):
    """ A minimum class for exceptions processing program arguments. """
    
    def __init__(self, msg):
        
        self._msg = msg
        
    def __str__(self):
        return self._msg

class ProgramArguments(object):
    """ Encapsulates the definition and processing of program arguments. """
    
    # Constants


    def __init__(self):
        """ Initializes parser. 
        
        Initialization of variables and the object ProgramArguments 
        with the definition of arguments to use.

        """   
        
        # Initializes variables with default values.  
    
        
        self._min_number_of_args = 1             
                
        self._args = None   
        
        self._parser = None                                              
        
        # Properties that return values of program arguments.

    
    def init_parser(self):
        """Initializes the ArgumentParser object."""
        
        self._parser = argparse.ArgumentParser()
        
        # Initialize arguments of the parser.        
        self._parser.add_argument("-file", dest="file", metavar="file", 
                                  help="A program argument with a file.")
        self._parser.add_argument("-bool", dest="bool", action="store_true", 
                                  help="A program argument for a bool value.")

    def parse_and_update(self):
        """Parse the program arguments and update attributes."""

        try:
            # Parse program arguments.        
            self._args = self._parser.parse_args()
    
            # Process self._args to check values and update attributes.
            
        except argparse.ArgumentError as ae:
            print ae.message
            raise ProgramArgumentsException(ae.message)                         
                
    def process_program_arguments(self):
        """Parse and check coherence of program arguments."""     
        
        self.init_parser() 

        self.parse_and_update()
 
    def print_usage(self):
        """Print arguments options """
                
        self._parser.print_usage()     
        
    def print_help(self):
        """Print help for arguments options """
                
        self._parser.print_help()