# Class5

PSEUDOCODE FOR ANALYSIS ON DIABETES DATA

1(A). Accept arbitrary filename as argument and load the file

import argparse from ArgumentParser

Initialize parser

parser = argparse.ArgumentParser(description = '?')

Add positional parameter

parser.add_argument('csvfile', help = '?')

Parse the argument

parsed_args = parser.parse_args()

print parsed_args

print parsed_args.csvfile

my_csv_file = parsed_args.csvfile

assert os.path.isfile(my_csv_file), "error message"

print("No Error Message")

1(B). Organize to access columns and rows

import pandas as pd

data = pd.read.csv (my_csv_file, sep=\s+|,',header=None)

print (data.head())

print (data.shape)

print(data.iloc[0,0])

1.(C) Compute Summary Statistics

import numpy as np

print(np.mean(data))

print(np.std(data))

1.(D) Visualize the data, 1-feature (column) at a time, i.e. histogram, and save the figures to files

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.DataFrame(np.array(data))

for column in df.columns:  # Loop over all columns 

      sns.set()
   
      fig, ax = plt.subplots()
    
      sns.distplot(x='StringLabel', y=column, data=df)  # column is chosen here
    
      plt.savefig('{}.pdf'.format(column), bbox_inches='tight')  # filename chosen here

1.(E) Visualize the data, 2-features (columns) at a time, i.e. scatter plot, and save the figures to files
??????????

*
*
*

2. (intermediate)  Pseudocode for adding header data to table

df1 = pd.DataFrame(df, columns=['x', 'y1', 'y2', 'y3', 'y4'.....])

df1 = df1.sort_values('x')

3. (reach) Pseudocode for an additional type of plot (Google to find plot types of interest) for visualizing 2 or more of the features at a time.
????????

*
*
*
*
*
*
*
*
*
*
*
*
*
*
*








Important Link

https://bigdata-madesimple.com/step-by-step-approach-to-perform-data-analysis-using-python/
