##### Lists.
# Insert at the beginning of a list.
my_list(o, item)

# Flatten a list.
[item for sublist in here_my_list for item in sublist]

# Remove empty strings from a list of strings.
here_my_list = filter(len, here_my_list)

import itertools
list(itertools.chain.from_iterable(here_my_list))

# Sort rows of a list by a column, keeping the position of each column.
here_my_numpy_array[here_my_numpy_array[:,here_my_column_number].argsort()]

# Sort the characters of a string.
''.join(sorted(the_string[i])) 

# Extract a column from a numpy array (column is zero based).
here_my_numpy_array[:,column_number]

# Getting a string of file names from a list containing the file names.
list_of_files = str(files).translate(None, "[]\'")

# Getting indexes to iterate over a list in reverse order.
range(len(my_list)-1,-1,-1)
