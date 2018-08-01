
import pandas as pd
import numpy as np


#Series
print pd.Series(np.arange(5))


#Data frames

#Create DF
print pd.DataFrame(np.random.randn(3,4))
print pd.DataFrame(np.random.randn(3,4) ,index=list('XYZ'), columns=list('ABCD'))
df1 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

#View DF
print df1.head()  #.tail(number)
print df1.index   #df.columns , df.values, sort_index, sort_values
print df1.describe()


#Selecting a row/ a column. it is like a JSON
print df1['C']
print df1.loc[0:2,['A','D']]
print df1[df1.E == "test"]


#Reindexing 
print df1
print df1.reindex(index=[2,1,3,0], columns=list(df1.columns) + ['G'])

#plotting
df2 = pd.DataFrame(np.random.randn(10, 4),  columns=['A', 'B', 'C', 'D'])
print df2
df2.plot()
df2.plot.hist()

#Read data from file
pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",").plot()