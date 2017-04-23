import csv, re

def read_world_data(N=10, fn='0053-7-src-Ch06/src/rawdata_2001.txt'):
    """A function to read CIA World Factbook file.
    
N is the number of countries to process."""
    
    # initialize return lists
    gdp, labels= [], []

    # read the data and process it
    for i, row in enumerate(csv.reader(open(fn), delimiter='\t')):
        # remove the dollar, comma and space characters
        gdp_value = re.sub(r'[\$, ]', '', row[2])
        
        # store data in billions of dollars
        gdp.append(float(gdp_value)/1e9)
        labels.append(row[1].strip())
        
        # stop analyzing the data after N countries have been processed
        if i == N-1:
           break
    return (gdp, labels)

