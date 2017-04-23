
# Chapter5 Applications
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter5 Applications](#chapter5-applications)
	* [5.1 Find a Set of Items in a Large Collection of Files](#51-find-a-set-of-items-in-a-large-collection-of-files)
	* [5.2 Calculate a Statistic for Any Number of Categories from Data in a CSV File](#52-calculate-a-statistic-for-any-number-of-categories-from-data-in-a-csv-file)
	* [5.3 Calculate Statistics for Any Number of Categories from Data in a Text File](#53-calculate-statistics-for-any-number-of-categories-from-data-in-a-text-file)
	* [5.4 Chapter Exercises](#54-chapter-exercises)

<!-- tocstop -->


## 5.1 Find a Set of Items in a Large Collection of Files


```python
# %load applications/1search_for_items_write_found.py
#!/usr/bin/env python3
import csv
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple

item_numbers_file = sys.argv[1]
path_to_folder = sys.argv[2]
output_file = sys.argv[3]

item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
	filereader = csv.reader(item_numbers_csv_file)
	for row in filereader:
		item_numbers_to_find.append(row[0])
print(item_numbers_to_find)

filewriter = csv.writer(open(output_file, 'a', newline=''))

file_counter = 0
line_counter = 0
count_of_item_numbers = 0
for input_file in glob.glob(os.path.join(path_to_folder, '*.*')):
	file_counter += 1
	if input_file.split('.')[1] == 'csv':
		with open(input_file, 'r', newline='') as csv_in_file:
			filereader = csv.reader(csv_in_file)
			header = next(filereader)
			for row in filereader:
				row_of_output = []
				for column in range(len(header)):
					if column < 3:
						cell_value = str(row[column]).strip()
						row_of_output.append(cell_value)
					elif column == 3:
						cell_value = str(row[column]).lstrip('$').replace(',','').split('.')[0].strip()
						row_of_output.append(cell_value)
					else:
						cell_value = str(row[column]).strip()
						row_of_output.append(cell_value)
				row_of_output.append(os.path.basename(input_file))
				if row[0] in item_numbers_to_find:
					filewriter.writerow(row_of_output)
					count_of_item_numbers += 1
				line_counter += 1
	elif input_file.split('.')[1] == 'xls' or input_file.split('.')[1] == 'xlsx':
		workbook = open_workbook(input_file)
		for worksheet in workbook.sheets():
			try:
				header = worksheet.row_values(0)
			except IndexError:
				pass
			for row in range(1, worksheet.nrows):
				row_of_output = []
				for column in range(len(header)):
					if column < 3:
						cell_value = str(worksheet.cell_value(row,column)).strip()
						row_of_output.append(cell_value)
					elif column == 3:
						cell_value = str(worksheet.cell_value(row,column)).split('.')[0].strip()
						row_of_output.append(cell_value)
					else:
						cell_value = xldate_as_tuple(worksheet.cell(row,column).value,workbook.datemode)
						cell_value = str(date(*cell_value[0:3])).strip()
						row_of_output.append(cell_value)
				row_of_output.append(os.path.basename(input_file))
				row_of_output.append(worksheet.name)
				if str(worksheet.cell(row,0).value).split('.')[0].strip() in item_numbers_to_find:
					filewriter.writerow(row_of_output)
					count_of_item_numbers += 1
				line_counter += 1
print('Number of files: {}'.format(file_counter))
print('Number of lines: {}'.format(line_counter))
print('Number of item numbers: {}'.format(count_of_item_numbers))
```

## 5.2 Calculate a Statistic for Any Number of Categories from Data in a CSV File


```python
# %load applications/2calculate_statistic_by_category.py
#!/usr/bin/env python3
import csv
import sys
from datetime import date, datetime

def date_diff(date1, date2):
	try:
		diff = str(datetime.strptime(date1, '%m/%d/%Y') - \
				datetime.strptime(date2, '%m/%d/%Y')).split()[0]
	except:
		diff = 0
	if diff == '0:00:00':
		diff = 0
	return diff

input_file = sys.argv[1]
output_file = sys.argv[2]

packages = {}
previous_name = 'N/A'
previous_package = 'N/A'
previous_package_date = 'N/A'
first_row = True
today = date.today().strftime('%m/%d/%Y')

with open(input_file, 'r', newline='') as input_csv_file:
	filereader = csv.reader(input_csv_file)
	header = next(filereader)
	for row in filereader:
		current_name = row[0]
		current_package = row[1]
		current_package_date = row[3]
		if current_name not in packages:
			packages[current_name] = {}
		if current_package not in packages[current_name]:
			packages[current_name][current_package] = 0
		if current_name != previous_name:
			if first_row:
				first_row = False
			else:
				diff = date_diff(today, previous_package_date)
				if previous_package not in packages[previous_name]:
					packages[previous_name][previous_package] = int(diff)
				else:
					packages[previous_name][previous_package] += int(diff)
		else:
			diff = date_diff(current_package_date, previous_package_date)
			packages[previous_name][previous_package] += int(diff)
		previous_name = current_name
		previous_package = current_package
		previous_package_date = current_package_date

header = ['Customer Name', 'Category', 'Total Time (in Days)']
with open(output_file, 'w', newline='') as output_csv_file:
	filewriter = csv.writer(output_csv_file)
	filewriter.writerow(header)
for customer_name, customer_name_value in packages.items():
	for package_category, package_category_value in packages[customer_name].items():
		row_of_output = []
		print(customer_name, package_category, package_category_value)
		row_of_output.append(customer_name)
		row_of_output.append(package_category)
		row_of_output.append(package_category_value)
		filewriter.writerow(row_of_output)
```

## 5.3 Calculate Statistics for Any Number of Categories from Data in a Text File


```python
# %load applications/3parse_text_file.py
#!/usr/bin/env python3
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

messages = {}
notes = []
with open(input_file, 'r', newline='') as text_file:
	for row in text_file:
		if '[Note]' in row:
			row_list = row.split(' ', 4)
			day = row_list[0].strip()
			note = row_list[4].strip('\n').strip()
			if note not in notes:
				notes.append(note)
			if day not in messages:
				messages[day] = {}
			if note not in messages[day]:
				messages[day][note] = 1
			else:
				messages[day][note] += 1

filewriter = open(output_file, 'w', newline='')
header = ['Date']
header.extend(notes)
header = ','.join(map(str,header)) + '\n'
print(header)
filewriter.write(header)
for day, day_value in messages.items():
	row_of_output = []
	row_of_output.append(day)
	for index in range(len(notes)):
		if notes[index] in day_value.keys():
			row_of_output.append(day_value[notes[index]])
		else:
			row_of_output.append(0)
	output = ','.join(map(str,row_of_output)) + '\n'
	print(output)
	filewriter.write(output)
filewriter.close()
```


```python
# %load applications/3parse_text_file_skip_first_space.py
#!/usr/bin/python
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

messages = {}
notes = []
with open(input_file, 'rU') as text_file:
	for row in text_file:
		if '[Note]' in row:
			n = 2
			groups = row.split(' ')
			date_time = ' '.join(groups[:n])
			rest_of_line_string = ' '.join(groups[n:])
			rest_of_line_list = rest_of_line_string.split(' ', 2)
			note = rest_of_line_list[2].strip('\n').strip()
			row_list = []
			row_list.append(date_time)
			row_list.append(note)
			print row_list

			day = row_list[0]
			note = row_list[1]
			if note not in notes:
				notes.append(note)
			if day not in messages:
				messages[day] = {}
			if note not in messages[day]:
				messages[day][note] = 1
			else:
				messages[day][note] += 1

#filewriter = open(output_file, 'wb')
header = ['Date']
header.extend(notes)
header = ','.join(map(str,header)) + '\n'
print header
#filewriter.write(header)
for day, day_value in messages.items():
	row_of_output = []
	row_of_output.append(day)
	for index in range(len(notes)):
		if notes[index] in day_value.keys():
			row_of_output.append(day_value[notes[index]])
		else:
			row_of_output.append(0)
	output = ','.join(map(str,row_of_output)) + '\n'
	print output
	#filewriter.write(output)
#filewriter.close()
```

## 5.4 Chapter Exercises


```python

```
