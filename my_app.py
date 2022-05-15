import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from pandas._libs.hashtable import value_count
#title for web app 
st.title("State's Data Analysis")

@st.cache
def load_data():
    #Function for load data
    df = pd.read_json("stateData.json")

    # rename columns
    df.rename(columns={'per capita income':'perCapitaIncomeInDoller','literacy rate':'literacyRate','health index rank':'healthIndexRank' }, inplace=True)
    
    #remove doller sign     
    
    p = df['perCapitaIncomeInDoller']
    p = df['perCapitaIncomeInDoller'].str.replace('$', '')
    p=p.apply(float)
    df['perCapitaIncomeInDoller']=p

    # partition of numeric data frame
    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns

    # filter unique type
    type_column = df['type']
    unique_type = type_column.unique()

    # partition of objects data frame
    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns

    return df, numeric_cols, text_cols, unique_type

df, numeric_cols, text_cols, unique_type=load_data()


states=pd.read_csv("poptable.csv")

# print(unique_type)
# print(numeric_cols)
# print(type(df.perCapitaIncomeInDoller))

# give sidebar title
st.sidebar.title("settings")

# add checkbox to side bar
check_box=st.sidebar.checkbox(label="Display dataset")


if check_box:
    # display data frame
    st.dataframe(df)
    st.header("Data Visulization")

    area_fig=px.bar(df, x=df.state, y=df.area, title="Bar Graph of area", color=df.state)
    st.plotly_chart(area_fig)
    
    pop_fig=px.bar(df, x=df.state, y=df.population, title="Bar Graph of population", color=df.state)
    st.plotly_chart(pop_fig)

    # remove doller symbol
    
    # df=df.sort_values(by='perCapitaIncomeInDoller', ascending=True)
    
    capitalIncome_fig=px.bar(df, x=df.state, y=df.perCapitaIncomeInDoller, title="Bar Graph of Capital Income", color=df.state)
    capitalIncome_fig.update_layout(width=800)
    st.write(capitalIncome_fig)

    literacyRate_fig=px.bar(df, x=df.state, y=df.literacyRate, title="Bar Graph of Leteracy Rate", color=df.state)
    literacyRate_fig.update_layout(width=800)
    st.write(literacyRate_fig)

    healthIndexRank_fig=px.bar(df, x=df.state, y=df.healthIndexRank, title="Bar Graph of health Index Rank", color=df.state)
    healthIndexRank_fig.update_layout(width=800)
    st.write(healthIndexRank_fig)

    def autopct(pct): # only show the label when it's > 10%
        return ('%.2f' % pct)

    # type_count=df['type'].value_counts()
    # print(type_count)
    # type_fig=type_count.plot(subplots=True,kind='pie',figsize=(28,12), autopct=autopct)
    # plt.show(type_fig)
    # st.pyplot(type_fig)

    feature_selection=st.multiselect(label="Select fetures for compare all states",options=numeric_cols)

    if feature_selection:
        fig=px.line(df, x=df.state, y=feature_selection, title="graph of States")
        st.plotly_chart(fig)


feature_selection=st.sidebar.multiselect(label="feature to plot",
                                        options=numeric_cols)
state_dropdown = st.sidebar.selectbox(label="states",
                                      options=df.state)

# mul_state_dropdown=st.sidebar.multiselect(label="Select Multiple States",options=df.state)
# if mul_state_dropdown:
#     if feature_selection:
#         fig=px.line(df, x=df.state, y=feature_selection, title="graph of States")
#         st.plotly_chart(fig)

# match state with dropdown state
df = df[df['state']==state_dropdown]

df_features = df[feature_selection]

plotly_figure = px.bar(data_frame=df_features,
                      x=df_features.index, y=feature_selection,
                      title=(str(state_dropdown)))

# display plotly chart
st.plotly_chart(plotly_figure)



#     'state':df.state,
#     'population':df.population,
#     'perCapitaIncome':df.perCapitaIncome
# }
# df=pd.DataFrame(state_population_income)
# df=df.groupby('state')[['population','perCapitaIncome']].sum()
# st.write(df)
# st.bar_chart(df,height=500,width=1000)

# st.subheader("States compare with Per capital Income")

# state_option=df['state'].unique().tolist()
# state=st.multiselect('Which state would you like to see?', state_option)

# df=df[df['state'].isin(state)]

# fig1=px.bar(df, x="state", y="perCapitaIncome", color="state", hover_name="state", range_y=[0,5])
# fig1.update_layout(width=800)
# st.write(fig1)

# st.map(states)