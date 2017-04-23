
# Chapter3 Excel Files
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter3 Excel Files](#chapter3-excel-files)
  * [3.1 Introspecting an Excel Workbook](#31-introspecting-an-excel-workbook)
  * [3.2 Processing a Single Worksheet](#32-processing-a-single-worksheet)
    * [3.2.1 讀取與寫入Excel檔](#321-讀取與寫入excel檔)
    * [3.2.2 篩選特定的資料列](#322-篩選特定的資料列)
      * [在資料列中，符合條件的值](#在資料列中符合條件的值)
      * [資料列的值屬於一組關注的對象](#資料列的值屬於一組關注的對象)
      * [在資料列中，符合特定文字組合的值](#在資料列中符合特定文字組合的值)
    * [3.2.3 選擇特定欄位](#323-選擇特定欄位)
      * [欄位索引值](#欄位索引值)
      * [欄位標題](#欄位標題)
  * [3.3 Reading All Worksheets in a Workbook](#33-reading-all-worksheets-in-a-workbook)
    * [3.3.1 Filtering for Rows from All Worksheets](#331-filtering-for-rows-from-all-worksheets)
    * [3.3.2 Selecting Columns from All Worksheets](#332-selecting-columns-from-all-worksheets)
  * [3.4 Reading a Set of Worksheets in an Excel Workbook](#34-reading-a-set-of-worksheets-in-an-excel-workbook)
    * [3.4.1 Filtering for Rows from Subset of Worksheets](#341-filtering-for-rows-from-subset-of-worksheets)
  * [3.5 Processing Multiple Workbooks](#35-processing-multiple-workbooks)
    * [3.5.1 Count Number of Workbooks and Rows and Columns in Each Workbook](#351-count-number-of-workbooks-and-rows-and-columns-in-each-workbook)
    * [3.5.2 Concatenate Data from Multiple Workbooks](#352-concatenate-data-from-multiple-workbooks)
    * [3.5.3 Sum and Average a Set of Values Per Worksheet Per Workbook](#353-sum-and-average-a-set-of-values-per-worksheet-per-workbook)
  * [3.6 Chapter Exercises](#36-chapter-exercises)

<!-- tocstop -->


## 3.1 Introspecting an Excel Workbook


```python
# %load excel/1excel_introspect_workbook.py
#!/usr/bin/env python3
import sys
from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRows:", \
          worksheet.nrows, "\tColumns:", worksheet.ncols)

```

## 3.2 Processing a Single Worksheet

### 3.2.1 讀取與寫入Excel檔


```python
# %load excel/2excel_parsing_and_write.py
#!/usr/bin/env python3
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	for row_index in range(worksheet.nrows):
		for column_index in range(worksheet.ncols):
			output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
output_workbook.save(output_file)
```


```python
# %load excel/3excel_parsing_and_write_keep_dates.py
#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	for row_index in range(worksheet.nrows):
		row_list_output = []
		for col_index in range(worksheet.ncols):
			if worksheet.cell_type(row_index, col_index) == 3:
				date_cell = xldate_as_tuple(worksheet.cell_value\
					(row_index, col_index),workbook.datemode)
				date_cell = date(*date_cell[0:3]).strftime\
					('%m/%d/%Y')
				row_list_output.append(date_cell)
				output_worksheet.write(row_index, col_index, date_cell)
			else:
				non_date_cell = worksheet.cell_value\
					(row_index,col_index)
				row_list_output.append(non_date_cell)
				output_worksheet.write(row_index, col_index,\
					non_date_cell)
output_workbook.save(output_file)
```


```python
# %load excel/pandas_parsing_and_write_keep_dates.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheetname='january_2013')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
```

### 3.2.2 篩選特定的資料列

#### 在資料列中，符合條件的值


```python
# %load excel/4excel_value_meets_condition.py
#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

sale_amount_column_index = 3
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = []
	header = worksheet.row_values(0)
	data.append(header)
	for row_index in range(1,worksheet.nrows):
			row_list = []
			sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)
			if sale_amount > 1400.0:
				for column_index in range(worksheet.ncols):
					cell_value = worksheet.cell_value(row_index,column_index)
					cell_type = worksheet.cell_type(row_index, column_index)
					if cell_type == 3:
						date_cell = xldate_as_tuple(cell_value,workbook.datemode)
						date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
						row_list.append(date_cell)
					else:
						row_list.append(cell_value)
			if row_list:
				data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_value_meets_condition.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_meets_condition = \
	data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
```

#### 資料列的值屬於一組關注的對象


```python
# %load excel/5excel_value_in_set.py
#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

important_dates = ['01/24/2013', '01/31/2013']

purchase_date_column_index = 4
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = []
	header = worksheet.row_values(0)
	data.append(header)
	for row_index in range(1, worksheet.nrows):
		purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchase_date_column_index),workbook.datemode)
		purchase_date = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')
		row_list = []
		if purchase_date in important_dates:
			for column_index in range(worksheet.ncols):
				cell_value = worksheet.cell_value(row_index,column_index)
				cell_type = worksheet.cell_type(row_index, column_index)
				if cell_type == 3:
					date_cell = xldate_as_tuple(cell_value,workbook.datemode)
					date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
					row_list.append(date_cell)
				else:
					row_list.append(cell_value)
		if row_list:
			data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)

```


```python
# %load excel/pandas_value_in_set.py
#!/usr/bin/env python3
import pandas as pd
import string
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

important_dates = ['01/24/2013','01/31/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]

writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
```

#### 在資料列中，符合特定文字組合的值


```python
# %load excel/6excel_value_matches_pattern.py
#!/usr/bin/env python3
import re
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

pattern = re.compile(r'(?P<my_pattern>^J.*)')

customer_name_column_index = 1
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = []
	header = worksheet.row_values(0)
	data.append(header)
	for row_index in range(1, worksheet.nrows):
		row_list = []
		if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)):
			for column_index in range(worksheet.ncols):
				cell_value = worksheet.cell_value(row_index,column_index)
				cell_type = worksheet.cell_type(row_index, column_index)
				if cell_type == 3:
					date_cell = xldate_as_tuple(cell_value,workbook.datemode)
					date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
					row_list.append(date_cell)
				else:
					row_list.append(cell_value)
		if row_list:
			data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_value_matches_pattern.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]

writer = pd.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
```

### 3.2.3 選擇特定欄位

#### 欄位索引值


```python
# %load excel/7excel_column_by_index.py
#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

my_columns = [1, 4]

with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = []
	for row_index in range(worksheet.nrows):
		row_list = []
		for column_index in my_columns:
			cell_value = worksheet.cell_value(row_index,column_index)
			cell_type = worksheet.cell_type(row_index, column_index)
			if cell_type == 3:
				date_cell = xldate_as_tuple(cell_value,workbook.datemode)
				date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
				row_list.append(date_cell)
			else:
				row_list.append(cell_value)
		data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_column_by_index.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_by_index = data_frame.iloc[:, [1, 4]]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
```

#### 欄位標題


```python
# %load excel/8excel_column_by_name.py
#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

my_columns = ['Customer ID', 'Purchase Date']

with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = [my_columns]
	header_list = worksheet.row_values(0)
	header_index_list = []
	for header_index in range(len(header_list)):
		if header_list[header_index] in my_columns:
			header_index_list.append(header_index)
	for row_index in range(1,worksheet.nrows):
		row_list = []
		for column_index in header_index_list:
			cell_value = worksheet.cell_value(row_index,column_index)
			cell_type = worksheet.cell_type(row_index, column_index)
			if cell_type == 3:
				date_cell = xldate_as_tuple(cell_value,workbook.datemode)
				date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
				row_list.append(date_cell)
			else:
				row_list.append(cell_value)
		data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_column_by_name.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_by_name = data_frame.loc[:, ['Customer ID', 'Purchase Date']]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
```

## 3.3 Reading All Worksheets in a Workbook

### 3.3.1 Filtering for Rows from All Worksheets


```python
# %load excel/9excel_value_meets_condition_all_worksheets.py
#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')

sales_column_index = 3
threshold = 2000.0

first_worksheet = True
with open_workbook(input_file) as workbook:
	data = []
	for worksheet in workbook.sheets():
		if first_worksheet:
			header_row = worksheet.row_values(0)
			data.append(header_row)
			first_worksheet = False
		for row_index in range(1,worksheet.nrows):
			row_list = []
			sale_amount = worksheet.cell_value(row_index, sales_column_index)
			if sale_amount > threshold:
				for column_index in range(worksheet.ncols):
					cell_value = worksheet.cell_value(row_index,column_index)
					cell_type = worksheet.cell_type(row_index, column_index)
					if cell_type == 3:
						date_cell = xldate_as_tuple(cell_value,workbook.datemode)
						date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
						row_list.append(date_cell)
					else:
						row_list.append(cell_value)
			if row_list:
				data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_value_meets_condition_all_worksheets.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)

row_output = []
for worksheet_name, data in data_frame.items():
	row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()
```

### 3.3.2 Selecting Columns from All Worksheets


```python
# %load excel/10excel_column_by_name_all_worksheets.py
#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')

my_columns = ['Customer Name', 'Sale Amount']

first_worksheet = True
with open_workbook(input_file) as workbook:
	data = [my_columns]
	index_of_cols_to_keep = []
	for worksheet in workbook.sheets():
		if first_worksheet:
			header = worksheet.row_values(0)
			for column_index in range(len(header)):
				if header[column_index] in my_columns:
					index_of_cols_to_keep.append(column_index)
			first_worksheet = False
		for row_index in range(1, worksheet.nrows):
			row_list = []
			for column_index in index_of_cols_to_keep:
				cell_value = worksheet.cell_value(row_index, column_index)
				cell_type = worksheet.cell_type(row_index, column_index)
				if cell_type == 3:
					date_cell = xldate_as_tuple(cell_value,workbook.datemode)
					date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
					row_list.append(date_cell)
				else:
					row_list.append(cell_value)
			data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_column_by_name_all_worksheets.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)

column_output = []
for worksheet_name, data in data_frame.items():
	column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()
```

## 3.4 Reading a Set of Worksheets in an Excel Workbook

### 3.4.1 Filtering for Rows from Subset of Worksheets


```python
# %load excel/11excel_value_meets_condition_set_of_worksheets.py
#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('set_of_worksheets')

my_sheets = [0,1]
threshold = 1900.0
sales_column_index = 3

first_worksheet = True
with open_workbook(input_file) as workbook:
	data = []
	for sheet_index in range(workbook.nsheets):
		if sheet_index in my_sheets:
			worksheet = workbook.sheet_by_index(sheet_index)
			if first_worksheet:
				header_row = worksheet.row_values(0)
				data.append(header_row)
				first_worksheet = False
			for row_index in range(1,worksheet.nrows):
				row_list = []
				sale_amount = worksheet.cell_value(row_index, sales_column_index)
				if sale_amount > threshold:
					for column_index in range(worksheet.ncols):
						cell_value = worksheet.cell_value(row_index,column_index)
						cell_type = worksheet.cell_type(row_index, column_index)
						if cell_type == 3:
							date_cell = xldate_as_tuple(cell_value,workbook.datemode)
							date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
							row_list.append(date_cell)
						else:
							row_list.append(cell_value)
				if row_list:
					data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_value_meets_condition_set_of_worksheets.py
#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_sheets = [0,1]
threshold = 1900.0

data_frame = pd.read_excel(input_file, sheetname=my_sheets, index_col=None)

row_list = []
for worksheet_name, data in data_frame.items():
	row_list.append(data[data['Sale Amount'].astype(float) > threshold])
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()
```

## 3.5 Processing Multiple Workbooks

### 3.5.1 Count Number of Workbooks and Rows and Columns in Each Workbook


```python
# %load excel/12excel_introspect_all_workbooks.py
#!/usr/bin/env python3
import glob
import os
import sys
from xlrd import open_workbook

input_directory = sys.argv[1]

workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
	workbook = open_workbook(input_file)
	print('Workbook: {}'.format(os.path.basename(input_file)))
	print('Number of worksheets: {}'.format(workbook.nsheets))
	for worksheet in workbook.sheets():
		print('Worksheet name:', worksheet.name, '\tRows:',\
				worksheet.nrows, '\tColumns:', worksheet.ncols)
	workbook_counter += 1
print('Number of Excel workbooks: {}'.format(workbook_counter))
```

### 3.5.2 Concatenate Data from Multiple Workbooks


```python
# %load excel/13excel_concat_data_from_multiple_workbooks.py
#!/usr/bin/env python3
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_folder = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')

data = []
first_worksheet = True
for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
	print os.path.basename(input_file)
	with open_workbook(input_file) as workbook:
		for worksheet in workbook.sheets():
			if first_worksheet:
				header_row = worksheet.row_values(0)
				data.append(header_row)
				first_worksheet = False
			for row_index in range(1,worksheet.nrows):
				row_list = []
				for column_index in range(worksheet.ncols):
					cell_value = worksheet.cell_value(row_index,column_index)
					cell_type = worksheet.cell_type(row_index, column_index)
					if cell_type == 3:
						date_cell = xldate_as_tuple(cell_value,workbook.datemode)
						date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
						row_list.append(date_cell)
					else:
						row_list.append(cell_value)
				data.append(row_list)

for list_index, output_list in enumerate(data):
	for element_index, element in enumerate(output_list):
		output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_concat_data_from_multiple_workbooks.py
#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_workbooks = glob.glob(os.path.join(input_path,'*.xls*'))
data_frames = []
for workbook in all_workbooks:
	all_worksheets = pd.read_excel(workbook, sheetname=None, index_col=None)
	for worksheet_name, data in all_worksheets.items():
		data_frames.append(data)
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()
```

### 3.5.3 Sum and Average a Set of Values Per Worksheet Per Workbook


```python
# %load excel/14excel_sum_average_multiple_workbooks.py
#!/usr/bin/env python3
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_folder = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sums_and_averages')

all_data = []
sales_column_index = 3

header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average',\
 					'workbook_total', 'workbook_average']
all_data.append(header)

for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
	with open_workbook(input_file) as workbook:
		list_of_totals = []
		list_of_numbers = []
		workbook_output = []
		for worksheet in workbook.sheets():
			total_sales = 0
			number_of_sales = 0
			worksheet_list = []
			worksheet_list.append(os.path.basename(input_file))
			worksheet_list.append(worksheet.name)
			for row_index in range(1,worksheet.nrows):
				try:
					total_sales += float(str(worksheet.cell_value(row_index,sales_column_index)).strip('$').replace(',',''))
					number_of_sales += 1.
				except:
					total_sales += 0.
					number_of_sales += 0.
			average_sales = '%.2f' % (total_sales / number_of_sales)
			worksheet_list.append(total_sales)
			worksheet_list.append(float(average_sales))
			list_of_totals.append(total_sales)
			list_of_numbers.append(float(number_of_sales))
			workbook_output.append(worksheet_list)
		workbook_total = sum(list_of_totals)
		workbook_average = sum(list_of_totals)/sum(list_of_numbers)
		for list_element in workbook_output:
			list_element.append(workbook_total)
			list_element.append(workbook_average)
		all_data.extend(workbook_output)

for list_index, output_list in enumerate(all_data):
	for element_index, element in enumerate(output_list):
		output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
```


```python
# %load excel/pandas_sum_average_multiple_workbooks.py
#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_workbooks = glob.glob(os.path.join(input_path,'*.xls*'))
data_frames = []
for workbook in all_workbooks:
	all_worksheets = pd.read_excel(workbook, sheetname=None, index_col=None)
	workbook_total_sales = []
	workbook_number_of_sales = []
	worksheet_data_frames = []
	worksheets_data_frame = None
	workbook_data_frame = None
	for worksheet_name, data in all_worksheets.items():
		total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in data.ix[:, 'Sale Amount']]).sum()
		number_of_sales = len(data.loc[:, 'Sale Amount'])
		average_sales = pd.DataFrame(total_sales / number_of_sales)

		workbook_total_sales.append(total_sales)
		workbook_number_of_sales.append(number_of_sales)

		data = {'workbook': os.path.basename(workbook),
				'worksheet': worksheet_name,
				'worksheet_total': total_sales,
				'worksheet_average': average_sales}

		worksheet_data_frames.append(pd.DataFrame(data, columns=['workbook', 'worksheet', 'worksheet_total', 'worksheet_average']))
	worksheets_data_frame = pd.concat(worksheet_data_frames, axis=0, ignore_index=True)

	workbook_total = pd.DataFrame(workbook_total_sales).sum()
	workbook_total_number_of_sales = pd.DataFrame(workbook_number_of_sales).sum()
	workbook_average = pd.DataFrame(workbook_total / workbook_total_number_of_sales)

	workbook_stats = {'workbook': os.path.basename(workbook),
					 'workbook_total': workbook_total,
					 'workbook_average': workbook_average}

	workbook_stats = pd.DataFrame(workbook_stats, columns=['workbook', 'workbook_total', 'workbook_average'])
	workbook_data_frame = pd.merge(worksheets_data_frame, workbook_stats, on='workbook', how='left')
	data_frames.append(workbook_data_frame)

all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='sums_and_averages', index=False)
writer.save()
```

## 3.6 Chapter Exercises
