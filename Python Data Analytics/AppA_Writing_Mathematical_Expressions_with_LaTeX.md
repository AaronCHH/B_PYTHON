
# Appendix A: Writing Mathematical Expressions with LaTeX
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Appendix A: Writing Mathematical Expressions with LaTeX](#appendix-a-writing-mathematical-expressions-with-latex)
  * [A.1 With matplotlib](#a1-with-matplotlib)
  * [A.2 With IPython Notebook in a Markdown Cell](#a2-with-ipython-notebook-in-a-markdown-cell)
  * [A.3 With IPython Notebook in a Python 2 Cell](#a3-with-ipython-notebook-in-a-python-2-cell)
  * [A.4 Subscripts and Superscripts](#a4-subscripts-and-superscripts)
  * [A.5 Fractions, Binomials, and Stacked Numbers](#a5-fractions-binomials-and-stacked-numbers)
  * [A.6 Radicals](#a6-radicals)
  * [A.7 Fonts](#a7-fonts)
  * [A.8 Accents](#a8-accents)

<!-- tocstop -->


* http://matplotlib.org/users/mathtext.html.

## A.1 With matplotlib


```python
import matplotlib.pyplot as plt
%matplotlib inline
```

## A.2 With IPython Notebook in a Markdown Cell

```tex
$$c = \sqrt{a^2 + b^2}$$
```

$$c = \sqrt{a^2 + b^2}$$

## A.3 With IPython Notebook in a Python 2 Cell


```python
from IPython.display import display, Math, Latex
display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))
```


$$F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx$$


## A.4 Subscripts and Superscripts

```tex
r'$\alpha_i > \beta_i$'
```

$\alpha_i > \beta_i$


```python
r'$\sum_{i=0}^\infty x_i$'
```

$\sum_{i=0}^\infty x_i$

## A.5 Fractions, Binomials, and Stacked Numbers


```python
r'$\frac{3}{4} \binom{3}{4} \stackrel{3}{4}$'
```

$\frac{3}{4} \binom{3}{4} \stackrel{3}{4}$

## A.6 Radicals


```python
r'$\sqrt{2}$'
```

$\sqrt{2}$

## A.7 Fonts


```python
from IPython.display import display, Math, Latex
display(Math(r'\mathrm{Roman}'))
display(Math(r'\mathit{Italic}'))
display(Math(r'\mathtt{Typewriter}'))
display(Math(r'\mathcal{CALLIGRAPHY}'))
```


$$\mathrm{Roman}$$



$$\mathit{Italic}$$



$$\mathtt{Typewriter}$$



$$\mathcal{CALLIGRAPHY}$$


## A.8 Accents


```python
\acute a or \'a
\bar a
\breve a
\ddot a or \"a
\dot a or \.a
\grave a or \`a
\hat a or \^a
\tilde a or \~a
\vec a
\overline{abc}
```

$\acute a$

$\bar a$

$\breve a$

$\ddot a$

$\dot a$

$\grave a$

$\hat a$

$\tilde a$

$\vec a$

$\overline{abc}$


```python

```
