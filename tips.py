# Flatten a list.
[item for sublist in here_my_list for item in sublist]

# Remove empty strings from a list of strings.
here_my_list = filter(len, here_my_list)

import itertools
list(itertools.chain.from_iterable(here_my_list))

# Sort rows of a list by a column, keeping the position of each column.
here_my_numpy_array[here_my_numpy_array[:,here_my_column_number].argsort()]

# Extract a column from a numpy array (column is zero based).
here_my_numpy_array[:,column_number]
