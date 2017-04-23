
# Chapter4 Databases
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter4 Databases](#chapter4-databases)
	* [4.1 Python's Built-in sqlite3 Module](#41-pythons-built-in-sqlite3-module)
		* [4.1.1 將新記錄插入資料表](#411-將新記錄插入資料表)
		* [4.1.2 更新資料表的記錄](#412-更新資料表的記錄)
	* [4.2 MySQL Database](#42-mysql-database)
		* [4.2.1 將新記錄插入資料表](#421-將新記錄插入資料表)
		* [4.2.2 查詢資料表，並將輸出寫到CSV檔](#422-查詢資料表並將輸出寫到csv檔)
		* [4.2.3 更新資料表的記錄](#423-更新資料表的記錄)
	* [4.3 Chapter Exercises](#43-chapter-exercises)

<!-- tocstop -->


## 4.1 Python's Built-in sqlite3 Module


```python
# %load database/1db_count_rows.py
#!/usr/bin/env python3
import sqlite3

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')
query = """CREATE TABLE sales
			(customer VARCHAR(20),
			 product VARCHAR(40),
			 amount FLOAT,
			 date DATE);"""
con.execute(query)
con.commit()

# Insert a few rows of data into the table
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
		('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
		('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
		('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows:
	print(row)
	row_counter += 1
print('Number of rows: {}'.format(row_counter))

```

### 4.1.1 將新記錄插入資料表


```python
# %load database/2db_insert_rows.py
#!/usr/bin/env python3
import csv
import sqlite3
import sys

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Create an in-memory SQLite3 database
# Create a table called Suppliers with five attributes
con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
				(Supplier_Name VARCHAR(20),
				Invoice_Number VARCHAR(20),
				Part_Number VARCHAR(20),
				Cost FLOAT,
				Purchase_Date DATE);"""
c.execute(create_table)
con.commit()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])
	print(data)
	c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
con.commit()

# Query the Suppliers table
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print(output)

```

### 4.1.2 更新資料表的記錄


```python
# %load database/3db_update_rows.py
#!/usr/bin/env python3
import csv
import sqlite3
import sys

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')
query = """CREATE TABLE IF NOT EXISTS sales
			(customer VARCHAR(20),
				product VARCHAR(40),
				amount FLOAT,
				date DATE);"""
con.execute(query)
con.commit()

# Insert a few rows of data into the table
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
		('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
		('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
		('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
for tuple in data:
	print(tuple)
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# Read the CSV file and update the specific rows
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])
	print(data)
	con.execute("UPDATE sales SET amount=?, date=? WHERE customer=?;", data)
con.commit()

# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print(output)
```

## 4.2 MySQL Database

### 4.2.1 將新記錄插入資料表


```python
# %load database/4db_mysql_load_from_csv.py
#!/usr/bin/env python3
import csv
import MySQLdb
import sys
from datetime import datetime, date

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='python_training', passwd='python_training')
c = con.cursor()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
			data.append(str(row[column_index]).lstrip('$')\
			.replace(',', '').strip())
		else:
			a_date = datetime.date(datetime.strptime(\
			str(row[column_index]), '%m/%d/%Y'))
			# %Y: year is 2016; %y: year is 15
			a_date = a_date.strftime('%Y-%m-%d')
			data.append(a_date)
	print(data)
	c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print(row_list_output)

```

### 4.2.2 查詢資料表，並將輸出寫到CSV檔


```python
# %load database/5db_mysql_write_to_file.py
#!/usr/bin/env python3
import csv
import MySQLdb
import sys

# Path to and name of a CSV output file
output_file = sys.argv[1]

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', \
user='root', passwd='my_password')
c = con.cursor()

# Create a file writer object and write the header row
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
filewriter.writerow(header)

# Query the Suppliers table and write the output to a CSV file
c.execute("""SELECT *
		FROM Suppliers
		WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
	filewriter.writerow(row)

```

### 4.2.3 更新資料表的記錄


```python
# %load database/6db_mysql_update_from_csv.py
#!/usr/bin/env python3
import csv
import MySQLdb
import sys

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', \
user='root', passwd='my_password')
c = con.cursor()

# Read the CSV file and update the specific rows
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(str(row[column_index]).strip())
	print(data)
	c.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s;""", data)
con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print(output)

```

## 4.3 Chapter Exercises


```python

```
