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

#data = pd.read_csv(my_csv_file, sep='\s+|,',skiprows=[0],header=None, engine='python')
data = pd.read_csv(my_csv_file, sep='\s+|,', engine='python') #for data with default header
print("Data Preview","\n",data.head())
print("\n",data.shape)

# This session  Accesses Rows and Columns

print("\n","Rows 3 and 4","\n",data.iloc[3:5,:]) #Access Row
print("\n", "Column 3" "\n", data.iloc[:,3]) #Access Column


# This session computes Summary Statistics (Mean and Standard Deviation)

import numpy as np

print("\n","Mean of Features","\n",np.mean(data,axis=0))
print("\n")
print("Standard Deviation of Features", "\n", np.std(data,axis=0))

# This session is for plotting

import matplotlib.pyplot as plt
import seaborn as sns

# This session plots Histogram of each feature (column)

for i, column in enumerate(data.columns):
	plt.figure(i)
	sns.distplot(data[column])
	plt.savefig('{}.pdf'.format(column))
plt.show()
plt.close()

# This session plots Scatterplot for any 2 pairs of features (columns)

for i in range(data.shape[1]-1):
	for j in range(i+1):
		plt.figure(j)
		sns.scatterplot(data.iloc[:,i+1], data.iloc[:,j+1])
	plt.figure(i)
	sns.scatterplot(data.iloc[:,0], data.iloc[:,i+1])
	plt.show()
	plt.savefig('{}{}.pdf'.format(i,j))  #Only saves 10 of my files (The rest 45 overwrites)
#plt.show()

#  REACH
# This session plots KDE plots for 2 pairs of features

for x in range(data.shape[1]-1):
	for y in range(x+1):
		plt.figure(y)
		sns.kdeplot(data.iloc[:,x+1], data.iloc[:,y+1])
	plt.figure(x)
	sns.kdeplot(data.iloc[:,0], data.iloc[:, x+1])
	plt.show()


