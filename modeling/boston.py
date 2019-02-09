import pandas as pd
pd.options.display.width = 180
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.style.use('ggplot')
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''close all plots'''
plt.close('all')

'''import boston dataset'''
boston = datasets.load_boston()
# print(boston.DESCR)

'''Create boston DataFrame'''
cols = [name.lower() for name in boston.feature_names]
boston_df = pd.DataFrame(data=boston.data, columns=cols)
# print(boston_df.head())

'''add target and label columns'''
boston_df['medv'] = boston.target

'''look at data summary stats'''
# print(boston_df.info())
# print(boston_df.describe())

'''scatter plot for each feature colored by target'''
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1) #this is where the axis is set??
for feature, color in zip(['crim', 'lstat', 'age'], ['r', 'g', 'b']):
    ax.scatter(x=boston_df[feature].values, y=boston_df.medv.values, color=color, alpha=0.3, label=feature)
ax.legend(loc='best')
ax.set_ylabel('Median Value', size=15)
# plt.show()

'''Linear Regression'''
X = boston_df.drop('medv', axis=1).values
# by convention the data is labeled as X
y = boston_df.medv.values
# by convention the target is labeled as y
linear_model = LinearRegression()
linear_model.fit(X,y)
score = linear_model.score(X, y)
print('All data: {}'.format(score))
# # we are telling the model to learn (i.e. fit) by taking the data X and its category, so when we get new data it will assign it a category based on the best correlation.
# # print(X) # without the .values suffix this data would be represented as a DataFrame
# # print(y)

'''train model with portion of data and test on untrained data'''
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# why 42??
linear_model2 = LinearRegression()
linear_model2.fit(X_train, y_train)
print('Test date {}'.format(linear_model2.score(X_test, y_test)))
