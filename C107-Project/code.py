import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

fig =  go.Figure(go.Bar(x = df.groupby("level")["attempt"].mean(), y =["Level 1","Level 2","Level 3","Level 4"], orientation = "h"))
fig.show()

print(df.groupby("level")["attempt"].mean())
