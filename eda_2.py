print('Exploratory Data Analysis')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df=pd.read_csv('Data.csv')
df=df.astype(int)
new_val=df.groupby('col1')['col2'].sum(axis=1)