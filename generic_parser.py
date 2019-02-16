#1. Load a dataset from a file
#2. "organize" that file, so we can access columns *or* rows of it easily
#3. Compute some "summary statistics" about the dataset
#4. print those summary statistics


#1. Load a dataset
 # a. accept arbitrary filename as argument
 # b. load the file

#Solution
# 1(a)

from argparse import ArgumentParser

parser = ArgumentParser(description='A CSV reader + stats makes')
parser.add_argument('csvfile', help ='path to the input of csv file')

parsed_args = parser.parse_args()
print(parsed_args)
print(parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

import os

#if os.path.isfile(my_csv_file):
#	print("The file is Valid")
#else:
#	print("Opps! Invalid file. Enter a valid file")

#if not os.path.isfile(my_csv_file):
#	raise ValueError("not a valid file")
 
assert os.path.isfile(my_csv_file), "Please Enter a valid file"

print("The file exists")

#Solution 1(b) - Import the file

import pandas as pd

#data = pd.read_csv(my_csv_file)
data = pd.read_csv(my_csv_file, sep='\s+|,',header=None) #works for data without header
print(data.head())
print(data.shape)

#2 Organize file to access columns and rows
#2a. access any row "Pandas access rows"
print(data.iloc[3:5,:])
#2b. access any column "Pandas access column"
print(data.iloc[:,3])
#2c access any data
print(data.iloc[0,0])

#3. Compute Statistics
#a. Mean

import numpy as np

print(np.mean(data))
print(np.std(data))
