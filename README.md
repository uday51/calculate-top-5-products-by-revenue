# calculate-top-5-products-by-revenue


# Summary
The purpose of this project was to analyze the data using Python and pandas to gain insights into total revenue. This project involved reading and processing data, performing calculations, and validating results to ensure accuracy. Pandas, a powerful data manipulation library, was used for handling and analyzing the data efficiently.

Functions and Methods:

## dd.read_csv: 
1 Used dask to read csv file.
2 Since dask is better than pandas to read file when data is in large set.

## data.dropna:
1 Used to remove the rows which contain null values.
2 Used subset parameter to remove the null values in specific columns

### pd.to_numeric:
Used to convert argument to numeric type

### Groupby:
Used to group the Dataframe into group based on one or more columns

### sum:
Used to add the values in the columns

### reset_index:
Used to reset the index back to the default 0, 1, 2 etc

### sort_values:
Used to sort the values based on condition

### head:
return the specific number of rows from top

