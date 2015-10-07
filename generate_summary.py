import pandas as pd

data = pd.read_csv('kawasaki.csv')
data.head()

print(data.race.value_counts())

data['race_new'] = 'Other'
data.loc[data.race==4, 'race_new'] = 'White'
data.loc[data.race==3, 'race_new'] = 'Black'
data.loc[data.race==1, 'race_new'] = 'Asian'
data.loc[data.race==8, 'race_new'] = 'Hispanic'
print(data.race_new.value_counts())

summary = (data.race_new.value_counts()/data.shape[0]).round(2)

summary['foo'] = 'bar'
summary = summary.drop('foo')
sexcount = data.sex.value_counts()
print(sexcount)
summary['Male:Female'] = float(sexcount.ix[1])/sexcount.ix[0]
print(summary)

def getage(td):
    tdr = repr(td)
    return int(tdr[tdr.index('\'')+1:tdr.find('days')])/365.25

dob = pd.to_datetime(data.dob)
adm = pd.to_datetime(data.date_admission)
age = adm-dob
age = age[age>0]

import numpy as np
medstr = repr(age.median())
summary['Median age'] = np.round(getage(age.median()),1)
summary['Age range'] = np.round(getage(age.min()),2), np.round(getage(age.max()), 2)
summary['Subjects'] = data.shape[0]

summary.to_csv('demographics.csv', index=True)

cc = ['clinical_criteria___0','clinical_criteria___1','clinical_criteria___2','clinical_criteria___3','clinical_criteria___4']

clinical = data[cc].mean().round(2)
clinical.index = 'Fever','Rash','Conjunctivitis','Mucositis','Cervical node'
print(clinical)

clinical.to_csv('clinical.csv')