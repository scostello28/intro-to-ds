import pandas as pd
pd.options.display.width = 180
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.style.use('ggplot')
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

'''close all plots'''
plt.close('all')

'''import iris dataset'''
iris = datasets.load_iris()
# print(iris.DESCR)

'''Create Iris DataFrame'''
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
cols = iris_df.columns.tolist()
cols = [col.replace(' ', '_') for col in cols]
cols = [col.replace('_(cm)', '') for col in cols]
iris_df.columns = cols


'''add target and label columns'''
target_name_list = [iris.target_names[i] for i in iris.target]
iris_df['target'] = iris.target
iris_df['label'] = target_name_list

'''look at data summary stats'''
# print(iris_df.info())
# print(iris_df.describe())
print(iris_df.head())

'''scatter plot for each feature colored by target'''
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1) #?????
for target, color in zip(iris_df.target.unique(), ['r', 'g', 'b']):
    sub_df = iris_df.query('target == @target')
    #what the hell is @target?? loops through printing the first target in red, then the next in green, then the last in blue.
    ax.scatter(x=sub_df.sepal_length.values, y=sub_df.sepal_width.values, color=color, label=iris.target_names[target], s=30)
    # what is s=30?
ax.legend(loc='best')
ax.set_xlabel('Sepal Length', size=15)
ax.set_ylabel('Sepal Width', size=15)
plt.show()

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1) #?????
for target, color in zip(iris_df.target.unique(), ['r', 'g', 'b']):
    sub_df = iris_df.query('target == @target')
    ax.scatter(x=sub_df.petal_length.values, y=sub_df.petal_width.values, color=color, label=iris.target_names[target], s=30)
    # what is s=30?
ax.legend(loc='best')
ax.set_xlabel('Petal Length', size=15)
ax.set_ylabel('Petal Width', size=15)
plt.show()

'''Logistic Regression'''
X = iris_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
# by convention the data is labeled as X
y = iris_df.label.values
# by convention the target is labeled as y
logistic_model = LogisticRegression()
logistic_model.fit(X,y)
# we are telling the model to learn (i.e. fit) by taking the data X and its category, so when we get new data it will assign it a category based on the best correlation.
# print(X) # without the .values suffix this data would be represented as a DataFrame
# print(y)

'''Test model with new data!'''
single_point = logistic_model.predict(np.array([[4.5, 3.3, 1.6, 0.2]]))[0]
# print('Single point prediciton: {}'.format(single_point))
multi_point = logistic_model.predict(np.array([[7.2, 2.8, 6.6, 2], [6.2, 2.5, 3.6, 2], [4.7, 3.6, 1.9, .1]]))
print('Mulit point prediciton: {}'.format(multi_point))

'''See how our model will predict all data points'''
# print(logistic_model.predict(X))

'''measure accuracy by testing model with guesses vs acutal categories'''
# print(logistic_model.score(X,y))
# score = .96.  This is very high but the model was trained on the same data that it was tested on so this is referred to as training accuracy.  We ideally would liek to see how the model perfoms on new data.

'''train model with portion of data and test on untrained data'''
# This is how we test our model.  We train it on the majority of the data then let it guess on the rest.
# BUT we actually know the answers to the remaining data.  SO we will see how it predicts with the answers we already know.
# If we just put in new data and didn't have an answer we wouldn't have any clue how good it actuallu was.

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# why 42??
logistic_model2 = LogisticRegression()
logistic_model2.fit(X_train, y_train)
# print(logistic_model2.score(X_test, y_test))
