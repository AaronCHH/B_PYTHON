
# Ch06 Python繪圖：Matplotlib
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Ch06 Python繪圖：Matplotlib](#ch06-python繪圖matplotlib)
  * [6.1 繪圖視窗之設定](#61-繪圖視窗之設定)
  * [6.2 常用的圖形參數](#62-常用的圖形參數)
  * [6.3 座標軸與刻度](#63-座標軸與刻度)
  * [6.4 加入文字](#64-加入文字)
  * [6.5 多張圈形](#65-多張圈形)
  * [6.6 加入圖形元件](#66-加入圖形元件)
  * [6.7 數學函數繪圖](#67-數學函數繪圖)
  * [6.8 等高圖與速度向量圖](#68-等高圖與速度向量圖)
  * [6.9 習題](#69-習題)

<!-- tocstop -->



```python
## Python Codes for Chapter 6: Python Graphics: Matplotlib

#########
%matplotlib inline
import numpy as np
import os
mywd = "Python-Data-Sets"
os.chdir(mywd)
speed, dist = np.loadtxt("cars.txt", unpack = True, usecols = [0,1])
```


```python
speed
```




    array([  4.,   4.,   7.,   7.,   8.,   9.,  10.,  10.,  10.,  11.,  11.,
            12.,  12.,  12.,  12.,  13.,  13.,  13.,  13.,  14.,  14.,  14.,
            14.,  15.,  15.,  15.,  16.,  16.,  17.,  17.,  17.,  18.,  18.,
            18.,  18.,  19.,  19.,  19.,  20.,  20.,  20.,  20.,  20.,  22.,
            23.,  24.,  24.,  24.,  24.,  25.])




```python
dist
```




    array([   2.,   10.,    4.,   22.,   16.,   10.,   18.,   26.,   34.,
             17.,   28.,   14.,   20.,   24.,   28.,   26.,   34.,   34.,
             46.,   26.,   36.,   60.,   80.,   20.,   26.,   54.,   32.,
             40.,   32.,   40.,   50.,   42.,   56.,   76.,   84.,   36.,
             46.,   68.,   32.,   48.,   52.,   56.,   64.,   66.,   54.,
             70.,   92.,   93.,  120.,   85.])




```python
import matplotlib.pyplot as plt
plt.plot(speed, dist, 'o')
# plt.plot(speed, dist, "wo")
plt.xlabel("speed")
plt.ylabel("dist")
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_5_0.png)



```python
import matplotlib as mpl
mpl.rcParams
```




    RcParams({'_internal.classic_mode': False,
              'agg.path.chunksize': 0,
              'animation.avconv_args': [],
              'animation.avconv_path': 'avconv',
              'animation.bitrate': -1,
              'animation.codec': 'h264',
              'animation.convert_args': [],
              'animation.convert_path': 'convert',
              'animation.ffmpeg_args': [],
              'animation.ffmpeg_path': 'ffmpeg',
              'animation.frame_format': 'png',
              'animation.html': 'none',
              'animation.mencoder_args': [],
              'animation.mencoder_path': 'mencoder',
              'animation.writer': 'ffmpeg',
              'axes.autolimit_mode': 'data',
              'axes.axisbelow': 'line',
              'axes.edgecolor': 'k',
              'axes.facecolor': 'w',
              'axes.formatter.limits': [-7, 7],
              'axes.formatter.offset_threshold': 4,
              'axes.formatter.use_locale': False,
              'axes.formatter.use_mathtext': False,
              'axes.formatter.useoffset': True,
              'axes.grid': False,
              'axes.grid.axis': 'both',
              'axes.grid.which': 'major',
              'axes.hold': None,
              'axes.labelcolor': 'k',
              'axes.labelpad': 4.0,
              'axes.labelsize': 'medium',
              'axes.labelweight': 'normal',
              'axes.linewidth': 0.8,
              'axes.prop_cycle': cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']),
              'axes.spines.bottom': True,
              'axes.spines.left': True,
              'axes.spines.right': True,
              'axes.spines.top': True,
              'axes.titlepad': 6.0,
              'axes.titlesize': 'large',
              'axes.titleweight': 'normal',
              'axes.unicode_minus': True,
              'axes.xmargin': 0.05,
              'axes.ymargin': 0.05,
              'axes3d.grid': True,
              'backend': 'module://ipykernel.pylab.backend_inline',
              'backend.qt4': 'PyQt4',
              'backend.qt5': 'PyQt5',
              'backend_fallback': True,
              'boxplot.bootstrap': None,
              'boxplot.boxprops.color': 'k',
              'boxplot.boxprops.linestyle': '-',
              'boxplot.boxprops.linewidth': 1.0,
              'boxplot.capprops.color': 'k',
              'boxplot.capprops.linestyle': '-',
              'boxplot.capprops.linewidth': 1.0,
              'boxplot.flierprops.color': 'k',
              'boxplot.flierprops.linestyle': 'none',
              'boxplot.flierprops.linewidth': 1.0,
              'boxplot.flierprops.marker': 'o',
              'boxplot.flierprops.markeredgecolor': 'k',
              'boxplot.flierprops.markerfacecolor': 'none',
              'boxplot.flierprops.markersize': 6.0,
              'boxplot.meanline': False,
              'boxplot.meanprops.color': 'C2',
              'boxplot.meanprops.linestyle': '--',
              'boxplot.meanprops.linewidth': 1.0,
              'boxplot.meanprops.marker': '^',
              'boxplot.meanprops.markeredgecolor': 'C2',
              'boxplot.meanprops.markerfacecolor': 'C2',
              'boxplot.meanprops.markersize': 6.0,
              'boxplot.medianprops.color': 'C1',
              'boxplot.medianprops.linestyle': '-',
              'boxplot.medianprops.linewidth': 1.0,
              'boxplot.notch': False,
              'boxplot.patchartist': False,
              'boxplot.showbox': True,
              'boxplot.showcaps': True,
              'boxplot.showfliers': True,
              'boxplot.showmeans': False,
              'boxplot.vertical': True,
              'boxplot.whiskerprops.color': 'k',
              'boxplot.whiskerprops.linestyle': '-',
              'boxplot.whiskerprops.linewidth': 1.0,
              'boxplot.whiskers': 1.5,
              'contour.corner_mask': True,
              'contour.negative_linestyle': 'dashed',
              'datapath': 'C:\\Anaconda36\\lib\\site-packages\\matplotlib\\mpl-data',
              'date.autoformatter.day': '%Y-%m-%d',
              'date.autoformatter.hour': '%m-%d %H',
              'date.autoformatter.microsecond': '%M:%S.%f',
              'date.autoformatter.minute': '%d %H:%M',
              'date.autoformatter.month': '%Y-%m',
              'date.autoformatter.second': '%H:%M:%S',
              'date.autoformatter.year': '%Y',
              'docstring.hardcopy': False,
              'errorbar.capsize': 0.0,
              'examples.directory': '',
              'figure.autolayout': False,
              'figure.dpi': 72.0,
              'figure.edgecolor': (1, 1, 1, 0),
              'figure.facecolor': (1, 1, 1, 0),
              'figure.figsize': [6.0, 4.0],
              'figure.frameon': True,
              'figure.max_open_warning': 20,
              'figure.subplot.bottom': 0.125,
              'figure.subplot.hspace': 0.2,
              'figure.subplot.left': 0.125,
              'figure.subplot.right': 0.9,
              'figure.subplot.top': 0.88,
              'figure.subplot.wspace': 0.2,
              'figure.titlesize': 'large',
              'figure.titleweight': 'normal',
              'font.cursive': ['Apple Chancery',
                               'Textile',
                               'Zapf Chancery',
                               'Sand',
                               'Script MT',
                               'Felipa',
                               'cursive'],
              'font.family': ['sans-serif'],
              'font.fantasy': ['Comic Sans MS',
                               'Chicago',
                               'Charcoal',
                               'ImpactWestern',
                               'Humor Sans',
                               'xkcd',
                               'fantasy'],
              'font.monospace': ['DejaVu Sans Mono',
                                 'Bitstream Vera Sans Mono',
                                 'Computer Modern Typewriter',
                                 'Andale Mono',
                                 'Nimbus Mono L',
                                 'Courier New',
                                 'Courier',
                                 'Fixed',
                                 'Terminal',
                                 'monospace'],
              'font.sans-serif': ['DejaVu Sans',
                                  'Bitstream Vera Sans',
                                  'Computer Modern Sans Serif',
                                  'Lucida Grande',
                                  'Verdana',
                                  'Geneva',
                                  'Lucid',
                                  'Arial',
                                  'Helvetica',
                                  'Avant Garde',
                                  'sans-serif'],
              'font.serif': ['DejaVu Serif',
                             'Bitstream Vera Serif',
                             'Computer Modern Roman',
                             'New Century Schoolbook',
                             'Century Schoolbook L',
                             'Utopia',
                             'ITC Bookman',
                             'Bookman',
                             'Nimbus Roman No9 L',
                             'Times New Roman',
                             'Times',
                             'Palatino',
                             'Charter',
                             'serif'],
              'font.size': 10.0,
              'font.stretch': 'normal',
              'font.style': 'normal',
              'font.variant': 'normal',
              'font.weight': 'normal',
              'grid.alpha': 1.0,
              'grid.color': '#b0b0b0',
              'grid.linestyle': '-',
              'grid.linewidth': 0.8,
              'hatch.color': 'k',
              'hatch.linewidth': 1.0,
              'hist.bins': 10,
              'image.aspect': 'equal',
              'image.cmap': 'viridis',
              'image.composite_image': True,
              'image.interpolation': 'nearest',
              'image.lut': 256,
              'image.origin': 'upper',
              'image.resample': True,
              'interactive': True,
              'keymap.all_axes': ['a'],
              'keymap.back': ['left', 'c', 'backspace'],
              'keymap.forward': ['right', 'v'],
              'keymap.fullscreen': ['f', 'ctrl+f'],
              'keymap.grid': ['g'],
              'keymap.home': ['h', 'r', 'home'],
              'keymap.pan': ['p'],
              'keymap.quit': ['ctrl+w', 'cmd+w'],
              'keymap.save': ['s', 'ctrl+s'],
              'keymap.xscale': ['k', 'L'],
              'keymap.yscale': ['l'],
              'keymap.zoom': ['o'],
              'legend.borderaxespad': 0.5,
              'legend.borderpad': 0.4,
              'legend.columnspacing': 2.0,
              'legend.edgecolor': '0.8',
              'legend.facecolor': 'inherit',
              'legend.fancybox': True,
              'legend.fontsize': 'medium',
              'legend.framealpha': 0.8,
              'legend.frameon': True,
              'legend.handleheight': 0.7,
              'legend.handlelength': 2.0,
              'legend.handletextpad': 0.8,
              'legend.labelspacing': 0.5,
              'legend.loc': 'best',
              'legend.markerscale': 1.0,
              'legend.numpoints': 1,
              'legend.scatterpoints': 1,
              'legend.shadow': False,
              'lines.antialiased': True,
              'lines.color': 'C0',
              'lines.dash_capstyle': 'butt',
              'lines.dash_joinstyle': 'round',
              'lines.dashdot_pattern': [4.8, 1.2, 0.8, 1.2],
              'lines.dashed_pattern': [2.8, 1.2],
              'lines.dotted_pattern': [1.1, 1.1],
              'lines.linestyle': '-',
              'lines.linewidth': 1.5,
              'lines.marker': 'None',
              'lines.markeredgewidth': 1.0,
              'lines.markersize': 6.0,
              'lines.scale_dashes': True,
              'lines.solid_capstyle': 'projecting',
              'lines.solid_joinstyle': 'round',
              'markers.fillstyle': 'full',
              'mathtext.bf': 'sans:bold',
              'mathtext.cal': 'cursive',
              'mathtext.default': 'it',
              'mathtext.fallback_to_cm': True,
              'mathtext.fontset': 'dejavusans',
              'mathtext.it': 'sans:italic',
              'mathtext.rm': 'sans',
              'mathtext.sf': 'sans',
              'mathtext.tt': 'monospace',
              'nbagg.transparent': True,
              'patch.antialiased': True,
              'patch.edgecolor': 'k',
              'patch.facecolor': 'C0',
              'patch.force_edgecolor': False,
              'patch.linewidth': 1.0,
              'path.effects': [],
              'path.simplify': True,
              'path.simplify_threshold': 0.1111111111111111,
              'path.sketch': None,
              'path.snap': True,
              'pdf.compression': 6,
              'pdf.fonttype': 3,
              'pdf.inheritcolor': False,
              'pdf.use14corefonts': False,
              'pgf.debug': False,
              'pgf.preamble': [],
              'pgf.rcfonts': True,
              'pgf.texsystem': 'xelatex',
              'plugins.directory': '.matplotlib_plugins',
              'polaraxes.grid': True,
              'ps.distiller.res': 6000,
              'ps.fonttype': 3,
              'ps.papersize': 'letter',
              'ps.useafm': False,
              'ps.usedistiller': False,
              'savefig.bbox': None,
              'savefig.directory': '~',
              'savefig.dpi': 'figure',
              'savefig.edgecolor': 'w',
              'savefig.facecolor': 'w',
              'savefig.format': 'png',
              'savefig.frameon': True,
              'savefig.jpeg_quality': 95,
              'savefig.orientation': 'portrait',
              'savefig.pad_inches': 0.1,
              'savefig.transparent': False,
              'scatter.marker': 'o',
              'svg.fonttype': 'path',
              'svg.hashsalt': None,
              'svg.image_inline': True,
              'text.antialiased': True,
              'text.color': 'k',
              'text.dvipnghack': None,
              'text.hinting': 'auto',
              'text.hinting_factor': 8,
              'text.latex.preamble': [],
              'text.latex.preview': False,
              'text.latex.unicode': False,
              'text.usetex': False,
              'timezone': 'UTC',
              'tk.window_focus': False,
              'toolbar': 'toolbar2',
              'verbose.fileo': 'sys.stdout',
              'verbose.level': 'silent',
              'webagg.open_in_browser': True,
              'webagg.port': 8988,
              'webagg.port_retries': 50,
              'xtick.bottom': True,
              'xtick.color': 'k',
              'xtick.direction': 'out',
              'xtick.labelsize': 'medium',
              'xtick.major.bottom': True,
              'xtick.major.pad': 3.5,
              'xtick.major.size': 3.5,
              'xtick.major.top': True,
              'xtick.major.width': 0.8,
              'xtick.minor.bottom': True,
              'xtick.minor.pad': 3.4,
              'xtick.minor.size': 2.0,
              'xtick.minor.top': True,
              'xtick.minor.visible': False,
              'xtick.minor.width': 0.6,
              'xtick.top': False,
              'ytick.color': 'k',
              'ytick.direction': 'out',
              'ytick.labelsize': 'medium',
              'ytick.left': True,
              'ytick.major.left': True,
              'ytick.major.pad': 3.5,
              'ytick.major.right': True,
              'ytick.major.size': 3.5,
              'ytick.major.width': 0.8,
              'ytick.minor.left': True,
              'ytick.minor.pad': 3.4,
              'ytick.minor.right': True,
              'ytick.minor.size': 2.0,
              'ytick.minor.visible': False,
              'ytick.minor.width': 0.6,
              'ytick.right': False})



## 6.1 繪圖視窗之設定


```python
plt.figure(figsize = (9, 6.6))
plt.plot(speed, dist, "o")
plt.xlabel("speed")
plt.ylabel("dist")
plt.margins(0.05, 0.05)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_8_0.png)


## 6.2 常用的圖形參數


```python
plt.ion()
```


```python
plt.figure(1)
plt.plot(speed, dist)
```




    [<matplotlib.lines.Line2D at 0x551e4239b0>]




![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_11_1.png)



```python
plt.figure(2)
plt.plot(speed, dist ,"g-", linewidth = 2)
```




    [<matplotlib.lines.Line2D at 0x551e4b18d0>]




![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_12_1.png)



```python
plt.figure(3)
plt.plot (speed, dist, "ro")
```




    [<matplotlib.lines.Line2D at 0x551e539518>]




![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_13_1.png)



```python
plt.figure(4)
plt.plot(speed, dist, "^",  markeredgecolor = "blue",  markerfacecolor = "yellow",  markersize = 12)
```




    [<matplotlib.lines.Line2D at 0x551e604320>]




![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_14_1.png)



```python
plt.figure(5)
plt.plot(speed, dist, color= "green", linewidth = 2, linestyle = "dashed", marker = "v", markeredgecolor = "red", markerfacecolor = "white", markersize = 12)
```




    [<matplotlib.lines.Line2D at 0x551e6901d0>]




![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_15_1.png)



```python
plt.figure(6)
plt.plot(speed, dist, "g--v", linewidth = 2, markeredgecolor = "red", markerfacecolor = "white", markersize = 12)
```




    [<matplotlib.lines.Line2D at 0x551e712c88>]




![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_16_1.png)



```python
plt.figure(7)
plt.scatter(speed, dist, s = 30, marker = 'D')
```




    <matplotlib.collections.PathCollection at 0x551e79c828>




![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_17_1.png)



```python
plt.figure('6.2.1')
x = np.arange(21)
colors = ['blue', 'green', 'red', 'yellow', 'black', 'crimson', 'cyan', 'magenta', 'chartreuse', 'burlywood']
markers = ['.', 'o', 'v', '^', '<',  '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']
for i in x:
    plt.scatter(i, i, s = (i%10*10+50), marker = markers[i], c = colors[i%10])

plt.margins(0.5, 0.5)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_18_0.png)



```python
plt.figure('6.2.1')
x = np.arange(21)
colors = ['blue', 'green', 'red', 'yellow', 'black', 'crimson', 'cyan', 'magenta', 'chartreuse', 'burlywood']
markers = ['.', 'o', 'v', '^', '<',  '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']
for i in x:
    plt.scatter(i, i, s = (i%10*10+50), marker = markers[i], c = colors[i%10])

```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_19_0.png)


## 6.3 座標軸與刻度


```python
plt.figure('6.3.1', figsize = (4.5, 3.3))
plt.xlim(3, 27)
plt.ylim(0, 128)
plt.plot(speed, dist, 'gv')
plt.xlabel('speed')
plt.ylabel('dist')
plt.grid(color = 'orangered')
plt.xticks((5, 10, 15, 20, 25))
plt.yticks((25, 50, 75, 100, 125))
plt.minorticks_on()
plt.tick_params(which = 'minor', direction = 'out', length = 3, width = 2, colors = 'b', top = 0, right = 0)
plt.tick_params(which = 'major', direction = 'in', length = 6, width = 2, colors = 'r', top = 0, right = 0)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_21_0.png)



```python
import numpy as np
import matplotlib.pyplot as plt

plt.figure('6.3.2', edgecolor = 'white', facecolor = 'white')
x = np.arange(11)
colors = np.arange(11)
sizes = 100-np.arange(11) % 4 * 20
plt.axis([0., 10., 0., 10.])
plt.scatter(x, x, s = sizes, c = colors)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.xticks(x, ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K' ))
plt.yticks(x, rotation = 90)

plt.tick_params(axis = 'x', which = 'major', direction = 'out', color = 'black', labelcolor = 'red', width = 2)

plt.tick_params(axis = 'y', which = 'major', direction = 'out', color = 'Chartreuse', labelcolor = 'BlueViolet', width = 2)
plt.margins(0.1,0.1)

ax = plt.gca()
ax.spines['right'].set_color('Gold')
ax.spines['right'].set_bounds(2, 10)
ax.spines['left'].set_color('Chartreuse')
ax.spines['top'].set_color('Aqua')
ax.spines['top'].set_bounds(0, 8)

ax.spines['bottom'].set_color('black')
ax.spines['bottom'].set_position(('data', -0.5))
ax.spines['top'].set_position(('data', 10.5))
ax.spines['left'].set_position(('data', -0.5))
ax.spines['right'].set_position(('data', 10.5))

ax2 = ax.twiny()
ax2.set_xticks(x)
ax2.set_xticklabels(['0', '1', '2', '3', '4', '5', '6', '7', '8','', ''], color = 'Magenta')
ax2.tick_params(direction = 'out', color = 'Aqua', pad = 15, width = 2)

ax3 = ax.twinx()
ax3.set_yticklabels(['', '20', '40', '60', '80', '100'])
ax3.tick_params(direction = 'out', color = 'gold', pad = 25, width = 2)

plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_22_0.png)


## 6.4 加入文字


```python
plt.figure('6.4.1', figsize = (4.5, 3.3))
plt.plot(speed, dist, 'bo', label = 'braking distance to speed')
plt.title("car data")
plt.text(20, 100, "text here", fontsize = 16, color = "skyblue")
plt.text(14.8, 120, "top", color = "green")
plt.text(4, 60, "left", rotation = "vertical", color = "red")
plt.annotate("bottom ", xy = (14.4, 5), color = "blue")
plt.annotate("right ", xy = (25, 60), rotation = "vertical", color = "black")
plt.legend(loc = "best")
plt.margins(0.05, 0.05)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_24_0.png)



```python
plt.figure('6.4.2', 'legend', figsize = (4.5,3.3))
```


```python
plt.figure('6.4.2', figsize = (4.5,3.3))
marker1 = plt.plot(speed, dist, 'bo')
plt.title('car data')
plt.legend(['braking distance to speed'], loc = 0, numpoints = 1)
plt.margins(0.05, 0.05)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_26_0.png)



```python
plt.figure('6.4.3', figsize = (12, 12))
plt.xlim(0, 6)
plt.ylim(0, 6)

plt.text(2, 1, r'$\alpha > \beta$', fontsize = 20)

plt.text(2, 2, r'$\alpha_i < \beta_i$', fontsize = 20)

plt.text(2, 3, r'$x^2+y^3$', fontsize = 20)

plt.text(2, 4, r'$\frac{2}{5x}$', fontsize = 20)

plt.text(2, 5, r'$\binom{3}{6}$', fontsize = 20)

plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_27_0.png)



```python
plt.figure('6.4.4.left', figsize = (12,12))
plt.plot(range(10), range(10), 'wo')
plt.text(1, 8, r'$\chi^2= 4.4$', fontsize = 20)
plt.text(1, 7, r'$x^3 = 5.5$', fontsize = 20)
plt.text(1, 6, r'$y_3^2 = 8.8$', fontsize = 20)
plt.text(7, 5, r'$\hat y \pm z$', fontsize = 20)
plt.text(5, 2, r'$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^\frac{-(x-\mu)^2}{2\sigma^2}$', fontsize = 20)
plt.margins(0.05,0.05)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_28_0.png)



```python
x = np.arange(-4, 4, 0.01)
plt.figure('6.4.4.right', figsize = (12,12))
plt.plot(x, np.cos(x), '-')
plt.xlabel(r'$phase \/ angle \/ \phi$', fontsize = 20)
plt.ylabel(r'$\cos(\phi)$', fontsize = 20)
plt.xticks((-np.pi, -np.pi/2, 0, np.pi/2, np.pi), (r'$-\pi$', r'$-2/\pi$', '0', r'$2/\pi$', r'$\pi$'))
plt.yticks((-1.0, -0.5, 0.0, 0.5, 1.0))
plt.margins(0.05, 0.05)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_29_0.png)


## 6.5 多張圈形


```python
plt.figure('subplot_1', figsize= (10,10))

plt.subplot(2, 2, 1)
plt.plot(speed, dist, 'wo', markersize = 15)
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.margins(0.05, 0.05)

plt.subplot(222)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.margins(0.05, 0.05)

plt.subplot(2, 2, 3)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed', fontsize = 15)
plt.ylabel('dist', fontsize = 15)
plt.margins(0.05, 0.05)

plt.subplot(224)
plt.plot(speed, dist, 'wo')
plt.title('cars data', fontsize = 20)
plt.xlabel('speed')
plt.ylabel('dist')
plt.margins(0.05, 0.05)

plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_31_0.png)



```python
plt.figure('subplot_2', figsize= (10,10))

plt.subplot(221)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.margins(0.05, 0.05)

plt.subplot(222)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.yticks(rotation = 90)
plt.margins(0.05, 0.05)

plt.subplot(223)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.xticks(rotation = 90)
plt.margins(0.05, 0.05)

plt.subplot(224)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.margins(0.05, 0.05)

plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_32_0.png)



```python
plt.figure('subplot_3', figsize = (10,10))

plt.subplot2grid((6, 2), (0, 0), rowspan = 2, colspan = 2)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.margins(0.05, 0.05)

plt.subplot2grid((6, 2), (3, 0), rowspan = 3, colspan = 1)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.yticks(rotation = 90)
plt.margins(0.05, 0.05)

plt.subplot2grid((6, 2), (3, 1), rowspan = 3, colspan = 1)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.xticks(rotation = 90)
plt.margins(0.05, 0.05)

plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_33_0.png)



```python
plt.figure('subplot_4', figsize = (10,10))

plt.subplot2grid((6, 3), (0, 0), rowspan = 2, colspan = 2)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.margins(0.05, 0.05)

plt.subplot2grid((6, 3), (3, 0), rowspan = 3, colspan = 2)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.yticks(rotation = 90)
plt.margins(0.05, 0.05)

plt.subplot2grid((6, 3), (3, 2), rowspan = 3, colspan = 1)
plt.plot(speed, dist, 'wo')
plt.title('cars data')
plt.xlabel('speed')
plt.ylabel('dist')
plt.xticks(rotation = 90)
plt.margins(0.05, 0.05)

plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_34_0.png)


## 6.6 加入圖形元件


```python
import numpy as np
import matplotlib.pyplot as plt

plt.figure('6.6.1')
plt.axis([0, 10, 0, 10])
plt.plot([1,2], [8,9], 'y-', linewidth = 2)
plt.plot([2,10], [0,8], '-', linewidth = 3, color = 'gold')
plt.plot([2,3], [6,7], '-o', linewidth = 4, color = 'Violet', markerfacecolor='green', markeredgecolor = 'gold', markersize = 12)
plt.plot([2,3], [5,4], '-^', linewidth = 4, color = 'SandyBrown', markerfacecolor = 'green', markeredgecolor = 'gold', markersize = 12)

plt.axhline(y = 1, linewidth = 1, linestyle = '-', color = 'red')
plt.axhline(y = 2, linewidth = 2, linestyle = '--', color = 'blue')
plt.axhline(y = 3, linewidth = 3, linestyle = '-.', color = 'green')
plt.axvline(x = 6, linewidth = 1, linestyle = '-', color = 'red')
plt.axvline(x = 7, linewidth = 2, linestyle = '--', color = 'blue')
plt.axvline(x = 8, linewidth = 3, linestyle = '-.', color = 'green')
plt.axvspan(9, 9.5, color = 'wheat')
plt.axhspan(0.2, 0.7, color = 'maroon')
plt.arrow(1, 7, 0, -1, linewidth = 3,  head_width = 0.5, head_length = 0.5, color = 'pink')
plt.arrow(2, 8, 1, 1, linewidth = 3,  head_width = 0.3, head_length = 0.3, fc = 'red', ec = 'purple')

plt.annotate('arrowstyle', xy = (5, 8), xytext = (-50, 50), textcoords = 'offset points', arrowprops = dict(arrowstyle = "->"))
plt.annotate('arc', xy = (5, 6), xytext = (-50, 30), textcoords = 'offset points', arrowprops = dict(arrowstyle = "->", connectionstyle = "arc, angleA = 0, armA = 30,rad = 10"))
plt.annotate('angle', xy = (5, 5), xytext = (-50, -50), textcoords = 'offset points', bbox = dict(boxstyle = "round", fc = "0.8"), arrowprops=dict(arrowstyle = "->",connectionstyle = "angle, angleA = 0, angleB = 90, rad = 10"))
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_36_0.png)



```python
plt.figure('6.6.2')
plt.axis([0, 10, 0, 10])

circle1 = plt.Circle((5,5), 4.5, color = 'blue', fill = False, linewidth = 2.0)
circle2 = plt.Circle((3.5, 6.5), 0.5, color = 'blue')
circle3 = plt.Circle((7, 6.5), 0.5, color = 'blue')

rectangle1 = plt.Rectangle((2.5,7.5), 1.5, 0.5, facecolor = 'white', edgecolor = 'black', linewidth = 2.0)
rectangle2 = plt.Rectangle((6.5,7.5), 1.5, 0.5, facecolor = 'white', edgecolor = 'black', linewidth = 2.0)
rectangle3 = plt.Rectangle((5,4.5), 0.5, 2, facecolor = 'gold', edgecolor = 'violet', linewidth = 2.0)
rectangle4 = plt.Rectangle((4.5,1.5), 1.5, 1.5, color = 'red', linewidth=2.0)

polygon1 = plt.Polygon([[4, 3.5],[3.5,3.5],[2.5,2.5]], facecolor = 'orange', edgecolor='black')
polygon2 = plt.Polygon([[6.5, 3.5],[7,3.5],[8,2.5]], facecolor = 'orange', edgecolor = 'black')

fig = plt.gcf()
fig.gca().add_artist(circle1)
fig.gca().add_artist(circle2)
fig.gca().add_artist(circle3)
fig.gca().add_artist(rectangle1)
fig.gca().add_artist(rectangle2)
fig.gca().add_artist(rectangle3)
fig.gca().add_artist(rectangle4)
fig.gca().add_artist(polygon1)
fig.gca().add_artist(polygon2)

plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_37_0.png)


## 6.7 數學函數繪圖


```python
import numpy as np
import matplotlib.pyplot as plt
import os
mywd = "Python-Data-Sets"
os.chdir(mywd)
```


```python
iris = np.loadtxt('iris.txt', usecols = [0,1,2,3])
x = iris[:, 0]
y1 = iris[:, 1]
y2 = iris[:, 2]
y3 = iris[:, 3]
plt.figure('mutline', figsize = (5,5))
plt.plot(x, y1, 'gv', label = 'y1')
plt.plot(x, y2, 'ro', label = 'y2')
plt.plot(x, y3, 'bs', label = 'y3')
plt.xlabel('x')
plt.legend(loc = 0, numpoints = 1)
plt.margins(0.05, 0.05)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_40_0.png)



```python
plt.legend(loc = 0, numpoints = 1, ncol = 3)

plt.legend(loc = 0, numpoints = 1, frameon = False)

plt.figure('mutline_2', figsize = (5,5))
marker1 = plt.scatter(x, y1, s = 30, c = 'red', marker = 'D')
marker2 = plt.scatter(x, y2, s = 30, c = 'green', marker = '1')
marker3 = plt.scatter(x, y3, s = 30, c = 'blue', marker = 'x')
plt.xlabel('x')
plt.legend((marker1, marker2, marker3), ('y1', 'y2', 'y3'), loc = 2)
plt.margins(0.05, 0.05)
plt.show()
```

    C:\Anaconda36\lib\site-packages\matplotlib\axes\_axes.py:545: UserWarning: No labelled objects found. Use label='...' kwarg on individual plots.
      warnings.warn("No labelled objects found. "



![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_41_1.png)



![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_41_2.png)



```python
x = np.linspace(-np.pi, np.pi, 101)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)+np.cos(x)
plt.figure("triangle function", figsize = (4.5,3.3))
plt.plot(x, y1, "r-", x, y2, 'g--', x, y3, "b--")
plt.xlabel('x')
plt.xticks((-np.pi, -np.pi/2, 0, np.pi/2, np.pi), (r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'))
plt.yticks((-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5))
plt.margins(0.05, 0.05)
plt.legend(('y1', 'y2', 'y3'), loc = 2)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_42_0.png)



```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = 0.01 * x**3 * np.cos(x) - 0.2 * x**2 * np.sin(x) + 0.05*x - 1
    return y

a = np.linspace(-10, 10, 101)
plt.figure('6.7.1')
plt.plot(a, f(a), 'k-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_43_0.png)



```python
f = lambda x: 0.01*x**3*np.cos(x) - 0.2*x**2*np.sin(x) + 0.05*x - 1
g = lambda x: 10*np.cos(x) * np.sin(x)

a = np.linspace(-10, 10, 101)
plt.figure('6.7.2')
plt.plot(a, f(a), 'r-', a, g(a), 'b--')
plt.xlabel('x')
plt.legend(('f', 'g'))
plt.margins(0.05, 0.05)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_44_0.png)



```python
f = lambda x: 0.01*x**3*np.cos(x) - 0.2*x**2*np.sin(x) + 0.05*x - 1

a = np.linspace(-10, 10, 101)
plt.figure('6.7.3')
plt.fill(a, f(a), 'r')
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_45_0.png)



```python
f = lambda x: 0.01*x**3*np.cos(x) - 0.2*x**2*np.sin(x) + 0.05*x - 1
g = lambda x: 10 * np.cos(x) * np.sin(x)

a = np.linspace(-10, 10, 101)
y1 = f(a)
y2 = g(a)
plt.figure('6.7.4.left')
plt.fill_between(a, y1, y2)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_46_0.png)



```python
plt.figure('6.7.4.right')
plt.fill_between(a, y1, y2, where = y2 >= y1, facecolor = 'green', interpolate = True)
plt.fill_between(a, y1, y2, where = y2 <= y1, facecolor = 'red', interpolate = True)
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_47_0.png)


## 6.8 等高圖與速度向量圖

## 6.9 習題


```python
x = np.linspace(-10, 10, 51)
y = np.linspace(-10, 10, 41)
X,Y = np.meshgrid(x, y)
a = 10*(np.exp(-((X + 3)**2 + (Y + 3)**2) / 10) - np.exp(-((X - 3)**2 + (Y-3)**2) / 10))
plt.figure('contour_1')
c = plt.contour(x, y, a)
plt.clabel(c)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

    C:\Anaconda36\lib\site-packages\matplotlib\contour.py:370: RuntimeWarning: invalid value encountered in true_divide
      dist = np.add.reduce(([(abs(s)[i] / L[i]) for i in range(xsize)]), -1)



![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_50_1.png)



```python
v = [-8, -6, -4, -2 ,0 , 2, 4, 6, 8]
plt.figure('contour_2')
c = plt.contour(x, y, a, v)
plt.clabel(c)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_51_0.png)



```python
plt.figure('contour_3¬_left')
c = plt.contour(x, y ,a)
plt.clabel(c, colors = 'black')
d = plt.contourf(x, y, a)
plt.colorbar(d, orientation = 'vertical')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

    C:\Anaconda36\lib\site-packages\matplotlib\contour.py:370: RuntimeWarning: invalid value encountered in true_divide
      dist = np.add.reduce(([(abs(s)[i] / L[i]) for i in range(xsize)]), -1)



![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_52_1.png)



```python
v = [-8, -6, -4, -2 ,0 , 2, 4, 6, 8]
plt.figure('contour_3¬_right')
c = plt.contour(x, y, a, v)
plt.clabel(c, colors = 'black')
d = plt.contourf(x, y, a, v)
plt.colorbar(d, orientation = 'vertical')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_53_0.png)



```python
x = np.linspace(0, 10, 21)
y = np.linspace(0, 10, 21)
X,Y = np.meshgrid(x, y)
u = 10 * np.sin(X)
v = 10 * np.sin(Y)
plt.figure('vector field')
q = plt.quiver(X, Y, u, v, angles = 'xy')
plt.quiverkey(q, 1, 10.5, 10, "10 m/s", coordinates = 'data')
xl = plt.xlabel('x (km) ')
yl = plt.ylabel('y (km) ')
plt.show()

#########
```


![png](Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_files/Ch06_Python%E7%B9%AA%E5%9C%96_Matplotlib_54_0.png)



```python

```
