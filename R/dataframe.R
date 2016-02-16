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

# Shows the strcture of a data frame.
str(data)

# Builds a table that summarizes the values of the column.
table(data$col)

# Add a column with the row number.
dat$order <- seq.int(nrow(dat))

# Remove the names of the rows.
rownames(data) <- NULL

# Change the name of a column.
names(data)[names(data) == "old_name"] <- "new_name"
# Or usint the rename function from the plyr package.
rename(data, "old_name", "new_name")

# Change the name of all the columns.
names(data) <- c("name_1", ... "name_n")

# Combine two data frames by rows.
dat <- rbind(a, b)

# Combine two data frames by columns.
dat <- cbind(a, b)

# Accesing a data frame by number of row and number of column.
data[i, j]

# Get the rows that met a condition.
data[data$col == X, ]
subset(data, col == X)

# Get the rows with column values not NA.
data <- data[! is.na(data$col), ]

# Get only the columns whose names are indicated.
data[, c("column_name")]

# Remove the columns not included in the vector.
data$col <- data$col[, !(names(data$col) %in% vector_with_columns_names)]

# Convert to factor a column considering as unique each value.
data$col <- factor(data$col, levels=unique((data$col)))

# Add a new column wit numeric values associated to the values of a column in the order indicated by the vector.
data$col.num <- as.numeric(factor(data$col, levels=c("Val_x", "Val_y")))

# Change the levels of a vector putting the indicated as the first and moving down the rest.
data$col = relevel(data$col, "level_name")

# Sort a data frama, first ascending by col1 and descending by col2.
with(data, order(col1,-col2))

# Summarize the data using the columns that are factors.
melt(data)