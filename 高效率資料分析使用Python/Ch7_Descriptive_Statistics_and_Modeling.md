
# Chapter7 Descriptive Statistics and Modeling
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter7 Descriptive Statistics and Modeling](#chapter7-descriptive-statistics-and-modeling)
	* [7.1 Datasets](#71-datasets)
		* [7.1.1 Wine Quality](#711-wine-quality)
		* [7.1.2 Customer Chum](#712-customer-chum)
	* [7.2 Wine Quality](#72-wine-quality)
		* [7.2.1 描述性統計](#721-描述性統計)
		* [7.2.2 分組、色階分布圖與t檢定](#722-分組-色階分布圖與t檢定)
		* [7.2.3 成對關係與相關性](#723-成對關係與相關性)
		* [7.2.4 使用最小二平方估計法的線性迴歸](#724-使用最小二平方估計法的線性迴歸)
		* [7.2.5 解譯係數](#725-解譯係數)
		* [7.2.6 標準化自變數](#726-標準化自變數)
		* [7.2.7 進行預測](#727-進行預測)
	* [7.3 Customer Churn](#73-customer-churn)

<!-- tocstop -->


## 7.1 Datasets

### 7.1.1 Wine Quality

### 7.1.2 Customer Chum

## 7.2 Wine Quality

### 7.2.1 描述性統計


```python
# %load statistics/wine_quality.py
#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm


# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())

# Display descriptive statistics for all variables
print(wine.describe())

# Identify unique values
print(sorted(wine.quality.unique()))

# Calculate value frequencies
print(wine.quality.value_counts())

# Display descriptive statistics for quality by wine type
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantiles
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

# Calculate correlation matrix for all variables
print(wine.corr())

# Look at relationship between pairs of variables
# Take a "small" sample of red and white wines for plotting
def take_sample(data_frame, replace=False, n=200):
	return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]
reds = wine.loc[wine['type']=='red', :]
whites = wine.loc[wine['type']=='white', :]
reds_sample = take_sample(wine.loc[wine['type']=='red', :])
whites_sample = take_sample(wine.loc[wine['type']=='white', :])
wine_sample = pd.concat([reds_sample, whites_sample])
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1.,0.)

reds_sample = reds.ix[np.random.choice(reds.index, 100)]
whites_sample = whites.ix[np.random.choice(whites.index, 100)]
wine_sample = pd.concat([reds_sample, whites_sample], ignore_index=True)

print(wine['in_sample'])
print(pd.crosstab(wine.in_sample, wine.type, margins=True))

sns.set_style("dark")
sns.set_style("darkgrid", {"legend.scatterpoints": 0})
pg = sns.PairGrid(wine_sample, hue="type", hue_order=["red", "white"], \
palette=dict(red="red", white="white"), hue_kws={"marker": ["o", "s"]}, vars=['quality', 'alcohol', 'residual_sugar'])
pg.x = wine_sample.ix[wine_sample['type']=='red', 'quality']
pg = pg.map_diag(plt.hist)
pg.x = wine_sample.ix[wine_sample['type']=='white', 'quality']
pg = pg.map_diag(plt.hist)
pg = pg.map_offdiag(plt.scatter, edgecolor="black", s=10, alpha=0.25)
#plt.show()

g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci": False, "x_jitter": 0.25, "y_jitter": 0.25}, \
hue='type', diag_kind='hist', diag_kws={"bins": 10, "alpha": 1.0}, palette=dict(red="red", white="white"), \
markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
sns.set_style({'legend.frameon': True,'legend.numpoints': 0,'legend.scatterpoints': 0})
wine_all_plot = sns.pairplot(wine, kind='reg', hue='type', palette=dict(red="red", white="white"), markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
wine_sample_plot = sns.pairplot(wine_sample, kind='reg', hue='type', palette=dict(red="red", white="white"), markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])

wine['ln_fixed_acidity'] = np.log(wine.ix[:, 'fixed_acidity'])
sns.distplot(wine.ix[:, 'fixed_acidity'])
sns.distplot(wine.ix[:, 'ln_fixed_acidity'])
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14, \
		horizontalalignment='center', verticalalignment='top',
		x=0.5, y=0.999)
#plt.show()

# Look at the distribution of quality by wine type
red_wine = wine.ix[wine['type']=='red', 'quality']
white_wine = wine.ix[wine['type']=='white', 'quality']

sns.set_style("dark")
print(sns.distplot(red_wine, \
		norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine, \
		norm_hist=True, kde=False, color="white", label="White wine"))
sns.axlabel("Quality Score", "Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
#plt.show()

# Test whether mean quality is different between red and white wines
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f  pvalue: %.4f' % (tstat, pvalue))

# Fit a multivariate linear regression model
#wine_standardized = (wine - wine.mean()) / wine.std()
#formula_all = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
#formula_all = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
#formula = 'quality ~ residual_sugar + alcohol'
lm = ols(my_formula, data=wine).fit()
#lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
#lm = smf.glm(formula_all, data=wine_standardized, family=sm.families.Gaussian()).fit()
print(lm.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
print("\nCoefficients:\n%s" % lm.params)
print("\nCoefficient Std Errors:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))

# Fit a multivariate linear model with standardized independent variables
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()
wine_standardized = pd.concat([dependent_variable, independent_variables_standardized], axis=1)
lm_standardized = ols(my_formula, data=wine_standardized).fit()
print(lm_standardized.summary())

# Predict quality scores for "new" observations
new_observations = wine.ix[wine.index.isin(xrange(10)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)

```

### 7.2.2 分組、色階分布圖與t檢定

### 7.2.3 成對關係與相關性

### 7.2.4 使用最小二平方估計法的線性迴歸

### 7.2.5 解譯係數

### 7.2.6 標準化自變數

### 7.2.7 進行預測

## 7.3 Customer Churn


```python
# %load statistics/customer_churn.py
#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
print(churn.head())
print(churn.describe())


# Calculate descriptive statistics for grouped data
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length', 'custserv_calls']].agg(['count', 'mean', 'std']))

# Specify different statistics for different variables
print(churn.groupby(['churn']).agg({'day_charge' : ['mean', 'std'],
				'eve_charge' : ['mean', 'std'],
				'night_charge' : ['mean', 'std'],
				'intl_charge' : ['mean', 'std'],
				'account_length' : ['count', 'min', 'max'],
				'custserv_calls' : ['count', 'min', 'max']}))

# Create total_charges, split it into 5 groups, and
# calculate statistics for each of the groups
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
						 churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 5, precision=2)
def get_stats(group):
	return {'min' : group.min(), 'max' : group.max(),
			'count' : group.count(), 'mean' : group.mean(),
			'std' : group.std()}
grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())

# Split account_length into quantiles and
# calculate statistics for each of the quantiles
factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])
grouped = churn.custserv_calls.groupby(factor_qcut)
print(grouped.apply(get_stats).unstack())

# Create binary/dummy indicator variables for intl_plan and vmail_plan
# and join them with the churn column in a new DataFrame
intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
print(churn_with_dummies.head())

# Split total_charges into quartiles, create binary indicator variables
# for each of the quartiles, and add them to the churn DataFrame
qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
churn_with_dummies = churn.join(dummies)
print(churn_with_dummies.head())

# Create pivot tables
print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], \
						aggfunc='mean', fill_value='NaN', margins=True))

# Fit a logistic regression model
dependent_variable = churn['churn01']
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()
#logit_model = smf.glm(output_variable, input_variables, family=sm.families.Binomial()).fit()
print(logit_model.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(logit_model))
print("\nCoefficients:\n%s" % logit_model.params)
print("\nCoefficient Std Errors:\n%s" % logit_model.bse)
#logit_marginal_effects = logit_model.get_margeff(method='dydx', at='overall')
#print(logit_marginal_effects.summary())

print("\ninvlogit(-7.2205 + 0.0012*mean(account_length) + 0.4443*mean(custserv_calls) + 0.0729*mean(total_charges))")

def inverse_logit(model_formula):
	from math import exp
	return (1.0 / (1.0 + exp(-model_formula)))*100.0

at_means = float(logit_model.params[0]) + \
	float(logit_model.params[1])*float(churn['account_length'].mean()) + \
	float(logit_model.params[2])*float(churn['custserv_calls'].mean()) + \
	float(logit_model.params[3])*float(churn['total_charges'].mean())

print(churn['account_length'].mean())
print(churn['custserv_calls'].mean())
print(churn['total_charges'].mean())
print(at_means)
print("Probability of churn when independent variables are at their mean values: %.2f" % inverse_logit(at_means))

cust_serv_mean = float(logit_model.params[0]) + \
	float(logit_model.params[1])*float(churn['account_length'].mean()) + \
	float(logit_model.params[2])*float(churn['custserv_calls'].mean()) + \
	float(logit_model.params[3])*float(churn['total_charges'].mean())

cust_serv_mean_minus_one = float(logit_model.params[0]) + \
		float(logit_model.params[1])*float(churn['account_length'].mean()) + \
		float(logit_model.params[2])*float(churn['custserv_calls'].mean()-1.0) + \
		float(logit_model.params[3])*float(churn['total_charges'].mean())

print(cust_serv_mean)
print(churn['custserv_calls'].mean()-1.0)
print(cust_serv_mean_minus_one)
print("Probability of churn when account length changes by 1: %.2f" % (inverse_logit(cust_serv_mean) - inverse_logit(cust_serv_mean_minus_one)))

# Predict churn for "new" observations
new_observations = churn.ix[churn.index.isin(xrange(10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)

# Fit a logistic regression model
output_variable = churn['churn01']
vars_to_keep = churn[['account_length', 'custserv_calls', 'total_charges']]
inputs_standardized = (vars_to_keep - vars_to_keep.mean()) / vars_to_keep.std()
input_variables = sm.add_constant(inputs_standardized, prepend=False)
logit_model = sm.Logit(output_variable, input_variables).fit()
#logit_model = smf.glm(output_variable, input_variables, family=sm.families.Binomial()).fit()
print(logit_model.summary())
print(logit_model.params)
print(logit_model.bse)
#logit_marginal_effects = logit_model.get_margeff(method='dydx', at='overall')
#print(logit_marginal_effects.summary())

# Predict output value for a new observation based on its mean standardized input values
input_variables = [0., 0., 0., 1.]
predicted_value = logit_model.predict(input_variables)
print("Predicted value: %.5f") % predicted_value
```


```python

```


```python

```
