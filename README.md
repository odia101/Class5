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











Important Link

https://bigdata-madesimple.com/step-by-step-approach-to-perform-data-analysis-using-python/
