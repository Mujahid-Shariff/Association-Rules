# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 23:38:05 2022

@author: admin
"""
#Mujahid Shariff
#pip install apyori

#Question 1 - Movies

#data preprocessing
import pandas as pd
df=pd.read_csv("my_movies.csv")
df.shape

df.head()

#creating for loop for all the rows to transform data from rows to columns
trans = []
for i in range(0,5):
    trans.append([str(df.values[i,j]) for j in range(0, 15)])


print(trans)

trans[0]
trans[1]
trans[2]

#Appliying Apriori using the below parameters gives 6 rules as result
from apyori import apriori
rules = apriori(transactions = trans, 
                min_support = 0.005, 
                min_confidence = 0.4, 
                min_lift = 2, min_length = 2, max_length = 3)

rules
results = list(rules)
len(results)



#accessing the data in results

#RelationRecord(items=frozenset({'Harry Potter1', 'Green Mile'}), 
#support=0.2, 
#ordered_statistics=[OrderedStatistic(items_base=frozenset({'Green Mile'}), 
                                  #items_add=frozenset({'Harry Potter1'}), 
                                  #confidence=1.0, 
                                  #lift=5.0

results[0]
results[0][0]
results[0][1] # support
results[0][2] 
results[0][2][1]
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

#creating empty library to save the data
b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,6):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

#Appliying Apriori using the below parameters gives 1 rule as result, 
                         #here we changed support to 0.005 and left =3
from apyori import apriori
rules = apriori(transactions = trans, 
                min_support = 0.004, 
                min_confidence = 0.5, 
                min_lift = 3, min_length = 2, max_length = 2)

rules
results = list(rules)
len(results)

results[0]
results[0][0]
results[0][1] # support
results[0][2] 
results[0][2][1]
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,1):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

#Appliying Apriori using the below parameters gives 6 rules as result, 
                         #here we changed support to 0.008 and left =2 and confidence = 0.06
from apyori import apriori
rules = apriori(transactions = trans, 
                min_support = 0.08, 
                min_confidence = 0.06, 
                min_lift = 2, min_length = 2, max_length = 2)
rules
results = list(rules)
len(results)

results[0]
results[0][1] # support
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,1):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

#2
#Appliying Apriori using the below parameters gives 1 rule as result, 
                         #here we changed support to 0.3
from apyori import apriori
rules = apriori(transactions = trans, 
                min_support = 0.3, 
                min_confidence = 0.06, 
                min_lift = 2, min_length = 2, max_length = 2)
rules
results = list(rules)
len(results)

results[0]
results[0][1] # support
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,1):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

#3 - Data Visvualization using Histogram, Scatterplot etc

#boxplot
df_new.boxplot(column="Support",vert=False) #boxplot for Support
df_new.boxplot(column="Confidence",vert=False) #boxplot for Confidence
df_new.boxplot(column="lift",vert=False) #boxplot for lift

#Histogram
df_new["Support"].hist() #Histogram for Support
df_new["Confidence"].hist() #Histogram for Confidence
df_new["lift"].hist() #Histogram for lift
 
#scatterplot

df_new.plot.scatter("Base Item","Support") #scatterplot for base Item and Support

#bar graph and Pie chart

t1=df_new["lift"].value_counts()

#bar graph
t1.plot(kind="bar")

#pie chart
t1.plot(kind='pie')



#Q2 - Book.Csv
import pandas as pd
df=pd.read_csv("book (1).csv")
df.shape

df.head()

'''
#creating for loop for all the rows to transform data from rows to columns
trans = []
for i in range(0,5):
    trans.append([str(df.values[i,j]) for j in range(0, 11)])


print(trans)

trans[0]
trans[1]
trans[2]
'''


#Appliying Apriori using the below parameters gives 23 rules as result
from apyori import apriori
rules = apriori(transactions = df, 
                min_support = 0.03, 
                min_confidence = 0.4, 
                min_lift = 3, min_length = 1, max_length = 2)

rules
results = list(rules)
len(results)

results[0]
results[0][1] # support
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,23):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

#
#Appliying Apriori using the below parameters gives 34 rules as result, changin confidence = 0.3 and lift = 2
from apyori import apriori
rules = apriori(transactions = df, 
                min_support = 0.03, 
                min_confidence = 0.3, 
                min_lift = 2, min_length = 1, max_length = 2)

rules
results = list(rules)
len(results)

results[0]
results[0][1] # support
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,23):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

#Appliying Apriori using the below parameters gives 11 rules as result, changing minimum support = 0.06 and lift = 4
from apyori import apriori
rules = apriori(transactions = df, 
                min_support = 0.006, 
                min_confidence = 0.3, 
                min_lift = 4, min_length = 1, max_length = 2)

rules
results = list(rules)
len(results)

results[0]
results[0][1] # support
results[0][2][0][1] # base item
results[0][2][0][0] # add item
results[0][2][0][2] # confidence
results[0][2][0][3] # lift

b = []
a = []
s = []
c = []
l = []
y=["Base Item", "Add Item", "Support", "Confidence", "lift"]

for i in range(0,23):
    b.append(results[i][2][0][1]) # base item
    a.append(results[i][2][0][0]) # add item
    s.append(results[i][1]) # support
    c.append(results[i][2][0][2]) # confidence
    l.append(results[i][2][0][3]) # lift

df_new = pd.concat([pd.DataFrame(b),
           pd.DataFrame(a),
           pd.DataFrame(s),
           pd.DataFrame(c),
           pd.DataFrame(l)],axis=1)

df_new.columns=y
df_new

#3 - Data Visvualization using Histogram, Scatterplot etc

#boxplot
df_new.boxplot(column="Support",vert=False) #boxplot for Support
df_new.boxplot(column="Confidence",vert=False) #boxplot for Confidence
df_new.boxplot(column="lift",vert=False) #boxplot for lift

#Histogram
df_new[("Support")].hist() #Histogram for Support
df_new["Confidence"].hist() #Histogram for Confidence
df_new["lift"].hist() #Histogram for lift
 
#scatterplot

df_new.plot.scatter("Base Item","Support") #scatterplot for base Item and Support

#bar graph and Pie chart

t1=df_new["lift"].value_counts()

#bar graph
t1.plot(kind="bar")

#pie chart
t1.plot(kind='pie')





