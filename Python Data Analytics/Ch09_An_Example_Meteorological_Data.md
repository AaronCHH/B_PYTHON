
# Chapter 9: An Example—Meteorological Data
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 9: An Example—Meteorological Data](#chapter-9-an-examplemeteorological-data)
  * [9.1 A Hypothesis to Be Tested: The Influence of the Proximity of the Sea](#91-a-hypothesis-to-be-tested-the-influence-of-the-proximity-of-the-sea)
    * [The System in the Study: The Adriatic Sea and the Po Valley](#the-system-in-the-study-the-adriatic-sea-and-the-po-valley)
  * [9.2 Data Source](#92-data-source)
  * [9.3 Data Analysis on IPython Notebook](#93-data-analysis-on-ipython-notebook)
  * [9.4 The RoseWind](#94-the-rosewind)
    * [Calculating the Distribution of the Wind Speed Means](#calculating-the-distribution-of-the-wind-speed-means)
  * [9.5 Conclusions](#95-conclusions)

<!-- tocstop -->


## 9.1 A Hypothesis to Be Tested: The Influence of the Proximity of the Sea

### The System in the Study: The Adriatic Sea and the Po Valley

## 9.2 Data Source

## 9.3 Data Analysis on IPython Notebook

http://api.openweathermap.org/data/2.5/history/city?q=Atlanta,US

http://history.openweathermap.org/data/2.5/history/city?q=London,UK


```python
test = pd.read_json('http://samples.openweathermap.org/data/2.5/history/city?q=London,UK&appid=b1b15e88fa797225412429c1c50c122a1')
```


```python
test1 = pd.read_json('http://samples.openweathermap.org/data/2.5/history/city?q=London,UK&appid=1917b771f43a3e44b8c3cb8adc0e90bc')
```


```python
test1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>calctime</th>
      <th>city_id</th>
      <th>cnt</th>
      <th>cod</th>
      <th>list</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0875</td>
      <td>2643743</td>
      <td>3</td>
      <td>200</td>
      <td>{'main': {'temp': 279.946, 'temp_min': 279.946...</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0875</td>
      <td>2643743</td>
      <td>3</td>
      <td>200</td>
      <td>{'main': {'temp': 282.597, 'temp_min': 282.597...</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0875</td>
      <td>2643743</td>
      <td>3</td>
      <td>200</td>
      <td>{'main': {'temp': 279.38, 'pressure': 1011, 'h...</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python
est1 = pd.read_json('http://samples.openweathermap.org/data/2.5/history/city?q=London,UK')
```


```python
import numpy as np
import pandas as pd
import datetime
```


```python
ferrara = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Ferrara,IT')
torino = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Torino,IT')
mantova = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Mantova,IT')
milano = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Milano,IT')
ravenna = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Ravenna,IT')
asti = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Asti,IT')
bologna = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Bologna,IT')
piacenza = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Piacenza,IT')
cesena = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Cesena,IT')
faenza = pd.read_json('http://api.openweathermap.org/data/2.5/history/city?q=Faenza,IT')
```


```python

```


```python
ferrara = pd.read_json('http://openweathermap.org/data/2.5/history/city?q=Ferrara,IT&appid=1917b771f43a3e44b8c3cb8adc0e90bc')
torino = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Torino,IT')
mantova = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Mantova,IT')
milano = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Milano,IT')
ravenna = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Ravenna,IT')
asti = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Asti,IT')
bologna = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Bologna,IT')
piacenza = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Piacenza,IT')
cesena = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Cesena,IT')
faenza = pd.read_json('http://history.openweathermap.org/data/2.5/history/city?q=Faenza,IT')
```

## 9.4 The RoseWind

### Calculating the Distribution of the Wind Speed Means

## 9.5 Conclusions


```python

```
