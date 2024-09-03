import yfinance as yf
import streamlit as st
import pandas as pd 


colors = ['', 
          'yellow', 'orange', 
          'red', 'blue', 'green',
          'purple', 'pink', 'white',
          'brown', 'black'
]

#HEADER COLOR SELECTION
selected_color = st.selectbox(
    'Select a color for the header:',
    options=colors
)

#GRPAH COLOR
selected_graph_color = st.color_picker(
    'Pick a color for the graphs:', '#00f900'
)

start_date = '2005-5-31'

end_date = '2024-8-31'

ticker_symbol = 'GOOGL'

ticker_data = yf.Ticker(ticker=ticker_symbol)

ticker_df = ticker_data.history(
    period='1d',
    start='2005-5-31',
    end='2024-8-31'
)

#COLOR CHECK
if selected_color:
    st.markdown(
        f'''
            <h1 style="color:{selected_color};"> Stock Price App </h1>
            <h4 style="color:{selected_color};"> Shown are the stock closing price and volume of Google from</h4>
            <h4 style="color:{selected_graph_color};">{start_date} to {end_date}</h4>
        ''',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f'''
            <h1> Stock Price App </h1>
            <h4> Shown are the stock closing price and volume of Google from</h4>
            <h4>{start_date} to {end_date}</h4>
        ''',
        unsafe_allow_html=True
    )

#DISPLAY GRAPHS WITH COLOR
st.line_chart(ticker_df.Close, color=selected_graph_color)
st.line_chart(ticker_df.Volume, color=selected_graph_color)
# st.line_chart(ticker_df.Open, line_color=selected_graph_color)
# st.line_chart(ticker_df.Low, line_color=selected_graph_color)
# st.line_chart(ticker_df.High, line_color=selected_graph_color)
