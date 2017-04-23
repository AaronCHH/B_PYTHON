
# Chapter2 Comma-Separated Values (CSV) Files
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter2 Comma-Separated Values (CSV) Files](#chapter2-comma-separated-values-csv-files)
	* [2.1 Base Python Versus pandas](#21-base-python-versus-pandas)
		* [2.1.1 Reading and Writing a CSV File (String Manipulation)](#211-reading-and-writing-a-csv-file-string-manipulation)
		* [2.1.2 何時基本的字串解析會失敗](#212-何時基本的字串解析會失敗)
		* [2.1.3 Reading and Writing a CSV File (Standard csv Module)](#213-reading-and-writing-a-csv-file-standard-csv-module)
	* [2.2 Filter for Specific Rows](#22-filter-for-specific-rows)
		* [2.2.1 Value in Row Meets a Condition](#221-value-in-row-meets-a-condition)
		* [2.2.2 Value in Row is in a Set of Interest](#222-value-in-row-is-in-a-set-of-interest)
		* [2.2.3 Value in Row Matches a Pattern (Regular Expression)](#223-value-in-row-matches-a-pattern-regular-expression)
	* [2.3 Select Specific Columns](#23-select-specific-columns)
		* [2.3.1 Index Values](#231-index-values)
		* [2.3.2 Column Headings](#232-column-headings)
	* [2.4 Select Contiguous Rows](#24-select-contiguous-rows)
	* [2.5 Add a Header Row](#25-add-a-header-row)
	* [2.6 Reading Multiple CSV Files](#26-reading-multiple-csv-files)
		* [2.6.1 Count Number of Files and Rows and Columns in Each File](#261-count-number-of-files-and-rows-and-columns-in-each-file)
	* [2.7 Concatenate Data from Multiple Files](#27-concatenate-data-from-multiple-files)
	* [2.8 Sum and Average a Set of Values per File](#28-sum-and-average-a-set-of-values-per-file)
	* [2.9 Chapter Exercises](#29-chapter-exercises)

<!-- tocstop -->


## 2.1 Base Python Versus pandas

### 2.1.1 Reading and Writing a CSV File (String Manipulation)


```python
# %load csv/1csv_simple_parsing_and_write.py
#!/usr/bin/env python3
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as filereader:
	with open(output_file, 'w', newline='') as filewriter:
		header = filereader.readline()
		header = header.strip()
		header_list = header.split(',')
		print(header_list)
		filewriter.write(','.join(map(str,header_list))+'\n')
		for row in filereader:
			row = row.strip()
			row_list = row.split(',')
			print(row_list)
			filewriter.write(','.join(map(str,row_list))+'\n')
```


```python
# %load csv/pandas_parsing_and_write.py
#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)
```

### 2.1.2 何時基本的字串解析會失敗

### 2.1.3 Reading and Writing a CSV File (Standard csv Module)


```python
# %load csv/2csv_reader_parsing_and_write.py
#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		filewriter = csv.writer(csv_out_file, delimiter=',')
		for row_list in filereader:
			filewriter.writerow(row_list)
```

## 2.2 Filter for Specific Rows

### 2.2.1 Value in Row Meets a Condition


```python
# %load csv/3csv_reader_value_meets_condition.py
#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0]).strip()
			cost = str(row_list[3]).strip('$').replace(',', '')
			if supplier == 'Supplier Z' or float(cost) > 600.0:
				filewriter.writerow(row_list)
```


```python
# %load csv/pandas_value_meets_condition.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)
```

### 2.2.2 Value in Row is in a Set of Interest


```python
# %load csv/4csv_reader_value_in_set.py
#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			a_date = row_list[4]
			if a_date in important_dates:
				filewriter.writerow(row_list)
```


```python
# %load csv/pandas_value_in_set.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

important_dates = ['1/20/14', '1/30/14']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date']\
.isin(important_dates), :]

data_frame_value_in_set.to_csv(output_file, index=False)
```

### 2.2.3 Value in Row Matches a Pattern (Regular Expression)


```python
# %load csv/5csv_reader_value_matches_pattern.py
#!/usr/bin/env python3
import csv
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			invoice_number = row_list[1]
			if pattern.search(invoice_number):
				filewriter.writerow(row_list)
```


```python
# %load csv/pandas_value_matches_pattern.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number']\
.str.startswith("001-"), :]

data_frame_value_matches_pattern.to_csv(output_file, index=False)
```

## 2.3 Select Specific Columns

### 2.3.1 Index Values


```python
# %load csv/6csv_reader_column_by_index.py
#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		for row_list in filereader:
			row_list_output = [ ]
			for index_value in my_columns:
				row_list_output.append(row_list[index_value])
			filewriter.writerow(row_list_output)
```


```python
# %load csv/pandas_column_by_index.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]

data_frame_column_by_index.to_csv(output_file, index=False)
```

### 2.3.2 Column Headings


```python
# %load csv/7csv_reader_column_by_name.py
#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		for index_value in range(len(header)):
			if header[index_value] in my_columns:
				my_columns_index.append(index_value)
		filewriter.writerow(my_columns)
		for row_list in filereader:
			row_list_output = [ ]
			for index_value in my_columns_index:
				row_list_output.append(row_list[index_value])
			filewriter.writerow(row_list_output)
```


```python
# %load csv/pandas_column_by_name.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]

data_frame_column_by_name.to_csv(output_file, index=False)
```

## 2.4 Select Contiguous Rows


```python
# %load csv/11csv_reader_select_contiguous_rows.py
#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		for row in filereader:
			if row_counter >= 3 and row_counter <= 15:
				filewriter.writerow([value.strip() for value in row])
			row_counter += 1
```


```python
# %load csv/pandas_select_contiguous_rows.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))

data_frame.to_csv(output_file, index=False)
```

## 2.5 Add a Header Row


```python
# %load csv/12csv_reader_add_header_row.py
#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header_list = ['Supplier Name', 'Invoice Number', \
					   'Part Number', 'Cost', 'Purchase Date']
		filewriter.writerow(header_list)
		for row in filereader:
			filewriter.writerow (row)
```


```python
# %load csv/pandas_add_header_row.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name', 'Invoice Number', \
'Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)

data_frame.to_csv(output_file, index=False)
```

## 2.6 Reading Multiple CSV Files

### 2.6.1 Count Number of Files and Rows and Columns in Each File


```python
# %load csv/8csv_reader_counts_for_multiple_files.py
#!/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = sys.argv[1]

file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	row_counter = 1
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader)
		for row in filereader:
			row_counter += 1
	print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(\
	os.path.basename(input_file), row_counter, len(header)))
	file_counter += 1
print('Number of files: {0:d}'.format(file_counter))
```

## 2.7 Concatenate Data from Multiple Files


```python
# %load csv/9csv_reader_concat_rows_from_multiple_files.py
#!/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	print(os.path.basename(input_file))
	with open(input_file, 'r', newline='') as csv_in_file:
		with open(output_file, 'a', newline='') as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)
			if first_file:
				for row in filereader:
					filewriter.writerow(row)
				first_file = False
			else:
				header = next(filereader)
				for row in filereader:
					filewriter.writerow(row)
```


```python
# %load csv/pandas_concat_rows_from_multiple_files.py
#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path,'sales_*'))

all_data_frames = []
for file in all_files:
	data_frame = pd.read_csv(file, index_col=None)
	all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)

data_frame_concat.to_csv(output_file, index = False)
```

## 2.8 Sum and Average a Set of Values per File


```python
# %load csv/10csv_reader_sum_average_from_multiple_files.py
#!/usr/bin/env python3
import csv
import glob
import os
import string
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

output_header_list = ['file_name', 'total_cost', 'average_cost']

csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		output_list = [ ]
		output_list.append(os.path.basename(input_file))
		header = next(filereader)
		total_sales = 0.0
		number_of_sales = 0.0
		for row in filereader:
			sale_amount = row[3]
			total_sales += float(str(sale_amount).strip('$').replace(',',''))
			number_of_sales += 1.0
		average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
		output_list.append(total_sales)
		output_list.append(average_sales)
		filewriter.writerow(output_list)
csv_out_file.close()
```


```python
# %load csv/pandas_sum_average_from_multiple_files.py
#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path,'sales_*'))
all_data_frames = []
for input_file in all_files:
	data_frame = pd.read_csv(input_file, index_col=None)

	total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
						for value in data_frame.loc[:, 'Sale Amount']]).sum()

	average_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
						for value in data_frame.loc[:, 'Sale Amount']]).mean()

	data = {'file_name': os.path.basename(input_file),
			'total_sales': total_sales,
			'average_sales': average_sales}

	all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'average_sales']))

data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)

data_frames_concat.to_csv(output_file, index = False)
```

## 2.9 Chapter Exercises
