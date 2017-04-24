
# Chapter 10: Embedding the JavaScript D3 Library in IPython Notebook
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 10: Embedding the JavaScript D3 Library in IPython Notebook](#chapter-10-embedding-the-javascript-d3-library-in-ipython-notebook)
  * [10.1 The Open Data Source for Demographics](#101-the-open-data-source-for-demographics)
  * [10.2 The JavaScript D3 Library](#102-the-javascript-d3-library)
  * [10.3 Drawing a Clustered Bar Chart](#103-drawing-a-clustered-bar-chart)
  * [10.4 The Choropleth Maps](#104-the-choropleth-maps)
  * [10.5 The Choropleth Map of the US Population in 2014](#105-the-choropleth-map-of-the-us-population-in-2014)
  * [10.6 Conclusions](#106-conclusions)

<!-- tocstop -->


## 10.1 The Open Data Source for Demographics

written by Agustin Barto (http://www.machinalis.com/blog/embedding-interactive-charts-on-an-ipython-nb/).
This article suggested the site of the United States Census Bureau (http://www.census.gov) as the data source for demographics (see Figure  10-1).


```python
from urllib2 import urlopen
pop2014 = pd.read_csv(
urlopen(' http://www.census.gov/popest/data/counties/totals/2014/files/CO-EST2014-alldata.csv'),
    encoding='latin-1',
    dtype={'STATE': 'str', 'COUNTY': 'str'}
)
```

## 10.2 The JavaScript D3 Library

## 10.3 Drawing a Clustered Bar Chart

## 10.4 The Choropleth Maps

## 10.5 The Choropleth Map of the US Population in 2014

## 10.6 Conclusions


```python

```
