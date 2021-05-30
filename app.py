from flask import Flask , render_template
import streamlit as st
from datetime import date

import plotly.graph_objects as go
import yfinance as yf 
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
st.title('Stock Prediction')
selected_Stock = st.text_input("Enter the stock name")
START = st.date_input("Enter Starting Date")
value = st.checkbox("Today")
if value:
 TODAY = date.today().strftime("%Y-%m-%d")
else:
   TODAY = st.date_input("Enter Ending Date")

n_years = st.slider("Years of prediction", 1,4)
per = n_years * 365
@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
data_load_state = st.text("Load data ...")
data = load_data(selected_Stock)
data_load_state.text("loading data ... Done!")
st.subheader("Raw Data")
st.write(data)


def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock Opening Data'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock Closing Data'))
        fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
    
plot_raw_data()

#Forcasting
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={'Date' : 'Dates' , 'Close' : 'Years'})
model = Prophet()
model.fit(df_train)
future = model.make_future_dataframe(periods=per)
forecast = model.predict(future)

st.subheader("Predicted Data")
st.write(forecast)
fig1 = plot_plotly(model,forecast)
st.plotly_chart(fig1)
st.write("Forecast Components")
fig2 = model.plot_components(forecast)
st.write(fig2)
