import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) Cole McNally')

df = pd.read_csv('housing.csv')
value_filter = st.slider('Minimal Median House Value:',0, 500001, 200000)

proximity_filter = st.sidebar.multiselect(
    'Choose the location typer',
    df.ocean_proximity.unique())

df = df[df.median_house_value <= value_filter]
df = df[df.ocean_proximity.isin(proximity_filter)]

income_filter = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

if income_filter == 'Low':
    df = df[df.median_income <=2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]
    
st.subheader('See more filters in the sidebar:')

st.map(df)

st.subheader('Histogram of the Median House Value')

fig,ax = plt.subplots()
ax.hist([df.median_house_value], bins=30)
st.pyplot(fig)