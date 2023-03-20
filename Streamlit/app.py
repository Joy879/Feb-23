import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

## TEXT ,HEADINGS, CODE
st.title("Revenue Analysis")
# st.header('My header')
# st.subheader('My sub')
# st.markdown('Markdown')
# st.text('Fixed width text')
#  # see *
# st.write('Most objects') # df, err, func, keras!

# st.code('for i in range(8): foo()')
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# * optional kwarg unsafe_allow_html = True
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
## GRAPHS
# st.line_chart(chart_data)
# st.area_chart(chart_data)
# st.bar_chart(chart_data)

df=pd.read_csv("dataonline.csv")
df["Revenue"]=df["UnitPrice"]*df["Quantity"]
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
df["InvoiceMonth"]=pd.DatetimeIndex(df["InvoiceDate"]).month
df["InvoiceYear"]=pd.DatetimeIndex(df["InvoiceDate"]).year

plt.figure(figsize=(6,7))
sns.barplot(data=df, x='InvoiceMonth', y='Revenue', hue='InvoiceYear', estimator=np.sum)
plt.title("Total Revenue per month")
plt.savefig('Total Revenue')

st.pyplot(plt)

df = px.data.gapminder()
fig = px.choropleth(df,
                    locations="iso_alpha",
                    color="pop", # lifeExp is a column of gapminder
                    hover_name="country",
                    hover_data=['lifeExp', 'continent'],
                    animation_frame='year')
# st.pyplot(fig)
st.plotly_chart(fig)

# st.altair_chart(data)
# st.vega_lite_chart(data)



# st.bokeh_chart(data)
# st.pydeck_chart(data)
# st.deck_gl_chart(data)
# st.graphviz_chart(data)


# st.map(data)
## TABLES

## MAPS

# selectbox("3 OPTIONS")

# if selection == a:
    # st

## WIDGETS - GIVE THE USER A OPTION TO PICK SOMETHING SO THAT THE VIEW CHANGES