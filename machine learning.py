import pandas
from sklearn.linear_model import LinearRegression
#import matplotlib.pyplot as plot
data = pandas.read_csv('iphone_price.csv')
#plot.scatter(data['version'], data['price'])
#plot.show()

model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[14]]))
print(model.predict([[22]]))
print(model.predict([[30]]))
