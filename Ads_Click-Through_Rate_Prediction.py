#!/usr/bin/env python
# coding: utf-8

# Import Libraries
import streamlit as st
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import  LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from imblearn.under_sampling import RandomUnderSampler
import datetime
from category_encoders import HashingEncoder
from xgboost import XGBClassifier
import pickle

st.title('Ads Click-Through Rate (CTR) Prediction')
'It is a Ads Click-Through Rate (CTR) Prediction, I am working on a binary classification problem in order to identify whether is worth or not a company should spend their money on digital advertising.' 


#filesize=int(os.popen("wc -l data/test").readline().split()[0])
filesize=508159
chunksize=round(filesize/100)
#@st.cache
def load_data():
    convs={'timestamp':'uint32','bidfloor':'int32','verticals_0':'uint16','support_id':'float32',
           'verticals_1':'uint16','verticals_2':'uint16','vertical_3':'uint16','ad_id':'uint16',
           'bid_price':'int32', 'won_price':'int32'}
    reader=pd.read_csv("data/test",na_values='None',  dtype=convs, usecols=lambda x: x not in
                       ['bidid','format','device_type','device_os'], iterator=True)
    return reader.get_chunk(chunksize)

st.write('## Importating data')
data_load_state=st.info('Loading data...')

chunks=[]
latest_iteration = st.empty()
bar= st.progress(0)
for i in range(1,51):
    chunks.append(load_data())
    bar.progress(i*2)
    
    
test = pd.concat([chunk for chunk in chunks])
test.dropna(inplace=True)
ds= test.copy(deep=True)
if test.empty:
    data_load_state.text('Error')
else:
    data_load_state.text('Done!')
    

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.dataframe(test)

st.write(test.shape)


objects = {'scaler':np.NaN, 'features':np.NaN, 'hashing_enc':np.NaN }
for o in objects:
    infile = open(o,'rb')
    objects[o] = pickle.load(infile)
    infile.close()

model = XGBClassifier({'nthread': 4})  # init model
model.load_model('model.json')  # load data
st.write('## Preprocessing ')
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

#encoding verticals columns
latest_iteration.text('encoding verticals columns...')

test = objects['hashing_enc'].transform(test)

bar.progress(40)

#drop null rows
latest_iteration.text('remove unusefull columns...')
test= test.dropna()


def resumed(x):
    if x==0:
        return 1
    else:
        return 0
bar.progress(50)


#create won_floor
latest_iteration.text('create new features...')
test['won_floor']=test.won_price-test.bidfloor
test.won_floor=test.won_floor.apply(resumed)
#create bid_floor feature
test['bid_floor']=test.bid_price-test.bidfloor
#create won_bid feature
test['won_bid']=test.won_price-test.bid_price
bar.progress(60)

#transform device_language
latest_iteration.text('transform device_language column...')
main_lang=['fr_FR', 'en_EN', 'tr_TR']
test.loc[~(test.device_language.isin(main_lang)),'device_language']='other'
bar.progress(70)

#Time feature: timestamp
latest_iteration.text('create time features...')

def tran_hour(x):
    x = x % 100
    if x in range(0,6):
        return 1
    elif x in range(6,11):
        return 2
    elif x in range(11,13):
        return 3
    elif x in range(13,18):
        return 4
    elif x in range(18,20):
        return 5
    else:
        return 6

test['timestamp'] = pd.to_datetime(test.timestamp, unit='s')
test['day of the month'] = test['timestamp'].dt.day
test["day of the week"] = test['timestamp'].dt.dayofweek
test['hour'] = test['timestamp'].dt.hour
test['hour'] = test.hour.apply(tran_hour)
test = test.drop(['timestamp'], axis=1)
bar.progress(80)


#convert categorical columns
latest_iteration.text('converting categorical features...')

cols=['support_type', 'device_language', 'device_model', 'support_id', 'device_id', 'user_id']

for col in cols:
    test[col] = test[col].astype('str')
    test[col] = LabelEncoder().fit_transform(test[col])
    
for col in cols[:4]:
    test[col] = test[col].astype('category')
    test[col] = LabelEncoder().fit_transform(test[col])

bar.progress(90)

    
#Normalization
latest_iteration.text('Normalization...')
test.loc[:, cols] = objects['scaler'].fit_transform(test[cols])
bar.progress(100)
latest_iteration.text('')
st.success('Done!')

st.write('## Classification ')
st.write(test.columns)
#Predictive Modeling
test = test[objects['features']]
model._le = LabelEncoder().fit(['0', '1'])
y_pred = model.predict(test)
ds['clicked']=y_pred
st.write('10 first rows')
st.dataframe(ds[:20])

st.write('Click Through Rate=(Total Clicks on Ad) / (Total Impressions)' )

st.write('CTR= ',ds['clicked'].mean())

