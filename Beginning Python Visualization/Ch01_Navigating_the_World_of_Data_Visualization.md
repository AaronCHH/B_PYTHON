
# Chapter 1: Navigating the World of Data Visualization
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 1: Navigating the World of Data Visualization](#chapter-1-navigating-the-world-of-data-visualization)
  * [1.1 Gathering Data](#11-gathering-data)
    * [1.1.1 Case Study: GPS Data](#111-case-study-gps-data)
    * [1.1.2 Scanning Serial Ports](#112-scanning-serial-ports)
    * [1.1.3 Recording GPS Data](#113-recording-gps-data)
  * [1.2 Data Organization](#12-data-organization)
    * [1.2.1 File Format](#121-file-format)
    * [1.2.2 File Naming Conventions](#122-file-naming-conventions)
    * [1.2.3 Data Location](#123-data-location)
  * [1.3 Data Analysis](#13-data-analysis)
    * [1.3.1 Walking Directories](#131-walking-directories)
    * [1.3.2 Reading CSV Files](#132-reading-csv-files)
    * [1.3.3 Analyzing GPS Data](#133-analyzing-gps-data)
    * [1.3.4 Extracting GPS Data](#134-extracting-gps-data)
  * [1.4 Data Visualization](#14-data-visualization)
    * [1.4.1 GPS Location Plot](#141-gps-location-plot)
    * [1.4.2 Annotating the Graph](#142-annotating-the-graph)
    * [1.4.3 Velocity Plot](#143-velocity-plot)
    * [1.4.4 Subplots](#144-subplots)
    * [1.4.5 Text](#145-text)
  * [1.5 Tying It All Together](#15-tying-it-all-together)
  * [1.6 Final Notes and References](#16-final-notes-and-references)

<!-- tocstop -->


## 1.1 Gathering Data

### 1.1.1 Case Study: GPS Data


```python
import serial
```

### 1.1.2 Scanning Serial Ports


```python
from serial.tools.list_ports import comports
list(comports())
```




    [<serial.tools.list_ports_common.ListPortInfo at 0x35f56d4a8>,
     <serial.tools.list_ports_common.ListPortInfo at 0x35f56d518>]



### 1.1.3 Recording GPS Data


```python
# %load 0053-7-src-Ch01/src/record_gps.py
import time, serial

# change these parameters to your GPS parameters
port = '/dev/ttyUSB0'  # in Windows, set this to 'COMx'
ser = serial.Serial(port)

ser.baudrate = 4800
fmt = "../data/GPS-%4d-%02d-%02d-%02d-%02d-%02d.csv"

filename = fmt % time.localtime()[0:6]
f = open(filename, 'wb')
while True:
    line = ser.readline()
    f.write(line)
    print(line)

```

## 1.2 Data Organization

### 1.2.1 File Format

### 1.2.2 File Naming Conventions

### 1.2.3 Data Location

## 1.3 Data Analysis

### 1.3.1 Walking Directories


```python
import os
for root, dirs, files in os.walk('../data'):
    print(root, dirs, files)
```


```python
os.listdir('../data')
```

### 1.3.2 Reading CSV Files


```python
def read_csv_file(filename):
    """Reads a CSV file and return it as a list of rows."""
    data = []
    for row in csv.reader(open(filename)):
        data.append(row)
    return data
```


```python
import csv
x = read_csv_file('../data/GPS-2008-06-04-09-03-45.csv')
len(x)
```


```python
x[10]
```


```python
x[1676]
```


```python
help(read_csv_file)
```


```python
help(csv)
```


```python
import csv
f = open('0053-7-src-Ch01/data/GPS-2008-06-04-09-03-45.csv')
cr = csv.reader(f)
for row in cr:
    print(row)
```


```python
f.close()
```


```python
cr = csv.reader(open('../data/GPS-2008-06-04-09-03-45.csv')):
for row in cr:
    print(row)
```


```python
for row in csv.reader(open('../data/GPS-2008-06-04-09-03-45.csv')):
    print(row)
```

### 1.3.3 Analyzing GPS Data

* Note NMea stands for the National Marine electronics association; see http://www.nmea.org for more information.
The NMea 0183 data format is described at http://www.gpsinformation.org/dale/nmea.htm.


```python
def list_gps_commands(data):
    """Counts the number of times a GPS command is observed.
    Returns a dictionary object."""
    gps_cmds = dict()
    for row in data:
        try:
            gps_cmds[row[0]] += 1
        except KeyError:
            gps_cmds[row[0]] = 1
    return gps_cmds
```


```python
x = read_csv_file('../data/GPS-2008-05-30-09-00-50.csv')
list_gps_commands(x)
```


```python
from pylab import *
```

### 1.3.4 Extracting GPS Data


```python
x[12]
```


```python
row = x[18]
row
```


```python
float(row[1][0:2])*3600+float(row[1][2:4])*60+float(row[1][4:6])
```


```python
row = x[18]
row
```


```python
float(row[3][0:2])+float(row[3][2:])/60.0
```


```python
100/60
```




    1.6666666666666667




```python
100//60
```




    1




```python
int(100/60)
```




    1




```python
NMI = 1852.0
def process_gps_data(data):
    """Processes GPS data, NMEA 0183 format.
    Returns a tuple of arrays: latitude, longitude, velocity [km/h],
    time [sec] and number of satellites.
    See also: http://www.gpsinformation.org/dale/nmea.htm.
    """
    latitude = []
    longitude = []
    velocity = []
    t_seconds = []
    num_sats = []
    for row in data:
        if row[0] == '$GPGSV':
            num_sats.append(float(row[3]))
        elif row[0] == '$GPRMC':
            t_seconds.append(float(row[1][0:2])*3600 + \
                             float(row[1][2:4])*60+float(row[1][4:6]))
            latitude.append(float(row[3][0:2]) + \
                            float(row[3][2:])/60.0)
            longitude.append((float(row[5][0:3]) + \
                              float(row[5][3:])/60.0))
            velocity.append(float(row[7])*NMI/1000.0)
    return (array(latitude), array(longitude), \
            array(velocity), array(t_seconds), array(num_sats))
```


```python
y = read_csv_file('../data/GPS-2008-05-30-09-00-50.csv')
(lat, long, v, t, sats) = process_gps_data(y)
```

## 1.4 Data Visualization


```python
x = longitude*NMI*60.0*cos(latitude)
y = latitude*NMI*60.0
```


```python
py = (lat-min(latitude))*NMI*60.0
px = (long-min(longitude))*NMI*60.0*cos(D2R*latitude)
```

### 1.4.1 GPS Location Plot


```python
filename = 'GPS-2008-05-30-09-00-50.csv'
y = read_csv_file('../data/'+filename)
(lat, long, v, t, sats) = process_gps_data(y)
px = (long-min(long))*NMI*60.0*cos(D2R*lat)
py = (lat-min(lat))*NMI*60.0
figure()
gca().axes.invert_xaxis()
plot(px, py, 'b', label='Cruising', linewidth=3)
title(filename[:-4])
legend(loc='upper left')
xlabel('east-west (meters)')
ylabel('south-north (meters)')
grid()
axis('equal')
show()
```

### 1.4.2 Annotating the Graph


```python
STANDING_KMH = 10.0
SPEEDING_KMH = 50.0
Istand = find(v < STANDING_KMH)
Ispeed = find(v > SPEEDING_KMH)
Icruise = find((v >=STANDING_KMH) & (v <= SPEEDING_KMH))
```


```python
plot(px[Istand], py[Istand], 'sg', label='Standing')
plot(px[Ispeed], py[Ispeed], 'or', label='Speeding!')
legend(loc='upper left')
```


```python
dx = px[i+1]-px[i]
dy = py[i+1]-py[i]
heading = arctan2(dy, dx)
```


```python
for i in range(0, len(v), len(v)//10-1):
    text(px[i], py[i], ">>>", \
         rotation = arctan2(py[i+1]-py[i], -(px[i+1]-px[i]))/D2R, \
         ha='center')
```

### 1.4.3 Velocity Plot


```python
figure()
t = (t-t[0])/60.0
plot(t, v, 'k')
plot([t[0], t[-1]], [STANDING_KMH, STANDING_KMH], '-g')
text(t[0], STANDING_KMH, \
     " Standing threshold: "+str(STANDING_KMH))
plot([t[0], t[-1]], [SPEEDING_KMH, SPEEDING_KMH], '-r')
text(t[0], SPEEDING_KMH, \
     " Speeding threshold: "+str(SPEEDING_KMH))
grid()
title('Velocity')
xlabel('Time from start of file (minutes)')
ylabel('Speed (Km/H)')
show()
```

### 1.4.4 Subplots


```python

```

### 1.4.5 Text


```python
subplot(2, 2, 4)
axis('off')
```


```python
diff([1, 4, 0, 2])
```


```python
sum(sqrt(diff(px)**2+diff(py)**2))
```


```python
Total_distance = float(sum(sqrt(diff(px)**2+diff(py)**2))/1000.0)
Stand_time = len(Istand)/60.0
Cruise_time = len(Icruise)/60.0
Speed_time = len(Ispeed)/60.0
Stand_per = 100*len(Istand)/len(v)
Cruise_per = 100*len(Icruise)/len(v)
Speed_per = 100*len(Ispeed)/len(v)
Stats=['Statistics', \
       '%s' % filename, \
       'Number of data points: %d' % len(y), \
       'Average number of satellites: %d' % mean(sats), \
       'Total driving time: %.1f minutes:' % (len(v)/60.0), \
       ' Standing: %.1f minutes (%d%%)' % \
       (Stand_time, Stand_per), \
       ' Cruising: %.1f minutes (%d%%)' % \
       (Cruise_time, Cruise_per), \
       ' Speeding: %.1f minutes (%d%%)' % \
       (Speed_time, Speed_per), \
       'Average speed: %d km/h' % mean(v), \
       'Total distance travelled: %.1f Km' % Total_distance ]
```


```python
for index, stat_line in enumerate(reversed(stats)):
    text(0, index, stat_line, va='bottom')
plot([index-.2, index-.2])
axis([0, 1, -1, len(stats)])
```

## 1.5 Tying It All Together


```python
# %load 0053-7-src-Ch01/src/gps.py
from pylab import *
import csv, os

# constant definitions
STANDING_KMH = 10.0
SPEEDING_KMH = 50.0
NMI = 1852.0
D2R = pi/180.0

def read_csv_file(filename):
    """Reads a CSV file and return it as a list of rows."""

    data = []
    for row in csv.reader(open(filename)):
        data.append(row)
    return data

def process_gps_data(data):
    """Processes GPS data, NMEA 0183 format.

Returns a tuple of arrays: latitude, longitude, velocity [km/h],
time [sec] and number of satellites.
See also: http://www.gpsinformation.org/dale/nmea.htm.
    """

    latitude    = []
    longitude   = []
    velocity    = []
    t_seconds   = []
    num_sats    = []

    for row in data:
        if row[0] == '$GPGSV':
            num_sats.append(float(row[3]))
        elif row[0] == '$GPRMC':
            t_seconds.append(float(row[1][0:2])*3600 + \
                float(row[1][2:4])*60+float(row[1][4:6]))
            latitude.append(float(row[3][0:2]) + \
                float(row[3][2:])/60.0)
            longitude.append((float(row[5][0:3]) + \
                float(row[5][3:])/60.0))
            velocity.append(float(row[7])*NMI/1000.0)

    return (array(latitude), array(longitude), \
        array(velocity), array(t_seconds), array(num_sats))

# read every data file, filter and plot the data
for root, dirs, files in os.walk('../data'):
    for filename in files:
        # create full filename including path
        cur_file = os.path.join(root, filename)
        if filename.endswith('csv'):
            y = read_csv_file(cur_file)
        else:
            continue

        # only files with the .csv extension from here on

        # process GPS data
        (lat, long, v, t, sats) = process_gps_data(y)

        # translate spherical coordinates to Cartesian
        py = (lat-min(lat))*NMI*60.0
        px = (long-min(long))*NMI*60.0*cos(D2R*lat)

        # find out when standing, speeding or cruising
        Istand = find(v < STANDING_KMH)
        Ispeed = find(v > SPEEDING_KMH)
        Icruise = find((v >= STANDING_KMH) & (v <= SPEEDING_KMH))

        # left side, GPS location graph
        figure()
        subplot(1, 2, 1)

        # longitude values go from right to left,
        # we want increasing values from left to right
        gca().axes.invert_xaxis()

        plot(px, py, 'b', label=' Cruising', linewidth=3)
        plot(px[Istand], py[Istand], 'sg', label=' Standing')
        plot(px[Ispeed], py[Ispeed], 'or', label=' Speeding!')

        # add direction of travel
        for i in range(0, len(v), len(v)//10-1):
            text(px[i], py[i], ">>>", \
                rotation=arctan2(py[i+1]-py[i], -(px[i+1]-px[i]))/D2R, \
                ha='center')

        # legends and labels
        title(filename[:-4])
        legend(loc='upper left')
        xlabel('east-west (meters)')
        ylabel('south-north (meters)')
        grid()
        axis('equal')

        # top right corner,  speed graph
        subplot(2, 2, 2)

        # set the start time as t[0]; convert to minutes
        t = (t-t[0])/60.0
        plot(t, v, 'k')

        # plot the standing and speeding threshold lines
        plot([t[0], t[-1]], [STANDING_KMH, STANDING_KMH], '-g')
        text(t[0], STANDING_KMH, \
            " Standing threshold: "+str(STANDING_KMH))
        plot([t[0], t[-1]], [SPEEDING_KMH, SPEEDING_KMH], '-r')
        text(t[0], SPEEDING_KMH, \
            " Speeding threshold: "+str(SPEEDING_KMH))
        grid()

        # legend and labels
        title('Velocity')
        xlabel('Time from start of file (minutes)')
        ylabel('Speed (Km/H)')

        # right side corner, statistics data
        subplot(2, 2, 4)

        # remove the frame and x/y axes. we want a clean slate
        axis('off')

        # generate an array of strings to be printed
        Total_distance  = sum(sqrt(diff(px)**2+diff(py)**2)/1000.0)
        Stand_time  = len(Istand)/60.0
        Cruise_time = len(Icruise)/60.0
        Speed_time  = len(Ispeed)/60.0
        Stand_per   = 100*len(Istand)/len(v)
        Cruise_per  = 100*len(Icruise)/len(v)
        Speed_per   = 100*len(Ispeed)/len(v)
        stats = ['Statistics', \
        '%s' % filename, \
        'Number of data points: %d' % len(y), \
        'Average number of satellites: %d' % mean(sats), \
        'Total driving time: %.1f minutes:' % (len(v)/60.0), \
        '    Standing: %.1f minutes (%d%%)' % \
        (Stand_time, Stand_per), \
        '    Cruising: %.1f minutes (%d%%)' % \
        (Cruise_time, Cruise_per), \
        '    Speeding: %.1f minutes (%d%%)' % \
        (Speed_time, Speed_per), \
        'Average speed: %d km/h' % mean(v), \
        'Total distance traveled: %.1f Km' % Total_distance ]

        # display statistics information
        for index, stat_line in enumerate(reversed(stats)):
            text(0, index, stat_line, va='bottom')

        # draw a line below the "Statistics" text
        plot([index-.2, index-.2])

        # set axis properly so all the text is displayed
        axis([0, 1, -1, len(stats)])
show()


```

## 1.6 Final Notes and References

* Python Programming Language—Official Website, http://www.python.org Other references used in this chapter include:
* pySerial, http://pyserial.sourceforge.net/
* “Data elements and interchange formats—Information interchange—Representation of dates and times”, http://www.iso.org
* NMEA 0183, http://www.nmea.org and http://www.gpsinformation.org/dale/nmea.htm
