import pandas as pd
import streamlit as st
import base64


st.title('NBA Player Stats Explorer')

st.markdown('''
This app performs simple webscraping of NBA player stats data.
* **Python libraries:** base64, pandas, streamlit
* **Data source:** Basketball-reference.com
''')

st.sidebar.header('User Input Features')

selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2020))))

# WEBSCRAPE
def load_data(year):
    try:
        url = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_per_game.html'
        html = pd.read_html(url, header=0)
        df = html[0]
        raw = df.drop(df[df.Age == 'Age'].index)
        raw = raw.fillna(0)
        player_stats = raw.drop(['Rk'], axis=1)
        return player_stats
    except Exception as e:
        st.error(f'Error: {e}')
        return pd.DataFrame()

player_stats = load_data(selected_year)

# SIDEBAR

sorted_unique_team = sorted(player_stats.Tm.unique())
selected_team = st.sidebar.multiselect(
    'Team', sorted_unique_team, sorted_unique_team
)

unique_position = ['C', 'PF', 'SF', 'PG', 'SG']
selected_position = st.sidebar.multiselect(
    'Position', unique_position, unique_position
)

df_selected_team = player_stats
[
    (player_stats.Tm.isin(selected_team)) 
    & (player_stats.Pos.isin(selected_position))
]

st.header('Display Player Stats of Selected Team(s)')

#TABLE DESCRIPTION
st.write('Data Dimension: ' + str(df_selected_team.shape[0])
+ ' rows and ' + str(df_selected_team.shape[1])
)

#DATAFRAME
st.dataframe(df_selected_team)

def download_file(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(download_file(df=df_selected_team))

