# Class5
#INSTRUCTION TO RUN THE SCRIPT
$ python generic_parser.py diabetes.tab.txt



PSEUDOCODE FOR ANALYSIS ON DIABETES DATA

1. Accept arbitrary filename as argument and load the file

1.1 import argparse from ArgumentParser

1.1.1 Initialize parser

1.1.2 parser = argparse.ArgumentParser(description = '?')

1.1.3 Add positional parameter

1.1.4 parser.add_argument('csvfile', help = '?')

1.1.5 Parse the argument

1.1.6 parsed_args = parser.parse_args()

1.1.7 print parsed_args

1.1.8 print parsed_args.csvfile

1.1.9 my_csv_file = parsed_args.csvfile

1.1.10 use assert to verify file validity 

      os.path.isfile(my_csv_file), "error message"

      print("No Error Message")


2. Organize to access columns and rows

2.1 import pandas as pd

2.1.1 data = pd.read.csv (my_csv_file, sep=\s+|,',header=None)

2.1.2 print the data table using the data.head function

2.1.3 print the shape of data using (data.shape)

2.1.4 View any row or column using iloc for pandas (data.iloc[0,0])


3. Compute Summary Statistics

3.1 import numpy as np

3.1.1 compute mean with numpy function

3.1.2 compute standard deviation with standard deviation


4. Visualize the data, 1-feature (column) at a time, i.e. histogram, and save the figures to files

4.1 import matplotlib.pyplot as plt

4.1.1 import seaborn as sns

4.1.2 Assign variable to data or array df = pd.DataFrame(np.array(data))

4.1.3 Visualize each column at a time by Histogram plot and save figures to files.

      for column in df.columns:  # Loop over all columns 

            sns.set()
   
            fig, ax = plt.subplots()
    
            sns.distplot(x='StringLabel', y=column, data=df)  # column is chosen here
    
            plt.savefig('{}.pdf'.format(column), bbox_inches='tight')  # filename chosen here

5. Visualize the data, 2-features (columns) at a time, i.e. scatter plot, and save the figures to files

      for column in df.columns
      
            plot one column against other columns
            
            do same plot for other columns without repeating already plotted columns
            
            plt.savefig to save files


6. Adding header data to table (Intermediate)

6.1 df1 = pd.DataFrame(df, columns=['x', 'y1', 'y2', 'y3', 'y4'.....])

6.2 df1 = df1.sort_values('x')


7. Additional type of plot for visualizing 2 or more of the features at a time (REACH).

7.1 Visualize data using violin plot

7.1.1 import seaborn as sns

7.1.2 sns.violin plot

      plot one column against other columns
      
      do same plot for other columns without repeating already plotted columns
      
      plt.savefig to save files

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
