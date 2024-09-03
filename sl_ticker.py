import streamlit as st
import pandas as pd
import plotly.express as px


stock_info_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

try:
    stock_data = pd.read_html(stock_info_url)[0]
except ValueError:
    st.error('Failed to load data from website.')
    

if not stock_data.empty:

    df = pd.DataFrame(stock_data)
    
    st.title('S&P 500 Stock Info')

    st.sidebar.header('Settings')

    cols = df.columns.tolist()

    selected_cols = st.multiselect(
        'Select columns to display',
        options=cols,
        default=[]
    )

    st.dataframe(df[selected_cols])

    if not selected_cols:
        st.markdown(
            '''
                <p style="color:yellow;">
                Graph will show once options are selected.
                </p>
            ''',
            unsafe_allow_html=True
        )

    else:
        x_axis = st.selectbox('Select X-axis', 
                              options=selected_cols
        )
        y_axis = st.selectbox('Select Y-axis',
                               options=selected_cols
        )
        
        color = st.selectbox('Select Color',
                             options=selected_cols,
                             index=0
        )
        # size = st.selectbox('Select Size',
        #                     options=selected_cols,
        #                     index=0
        # )

        fig = px.scatter(
            data_frame=df,
            x=x_axis,
            y=y_axis,
            color=color,
            title=f'Stock Data: {x_axis} | {y_axis}',
            height=600,
            width=1000
        )

        
        
        st.plotly_chart(figure_or_data=fig)



