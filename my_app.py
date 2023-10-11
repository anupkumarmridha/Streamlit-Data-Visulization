import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from pandas._libs.hashtable import value_count
#title for web app 
st.title("State's Data Analysis")

@st.cache_data 
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

    type_count = df['type'].value_counts()
    type_fig, ax = plt.subplots()
    type_count.plot.pie(ax=ax, figsize=(12, 6), autopct='%1.1f%%')
    st.pyplot(type_fig)

    feature_selection=st.multiselect(label="Select fetures for compare all states",options=numeric_cols)

    if feature_selection:
        fig=px.line(df, x=df.state, y=feature_selection, title="graph of States")
        st.plotly_chart(fig)
        for feature in feature_selection:
            figPie = px.pie(df, names='state', values=feature)
            st.plotly_chart(figPie)


feature_selection=st.sidebar.multiselect(label="feature to plot",
                                        options=numeric_cols)

mul_state_dropdown=st.sidebar.multiselect(label="Select Multiple States",
                                          options=df.state)

# Create a list of figure objects
figures = []

# Check if multiple states are selected in mul_state_dropdown
if mul_state_dropdown:
    filtered_df = df[df['state'].isin(mul_state_dropdown)]

    if feature_selection:
        # Generate a line chart for the selected states
        fig1 = px.line(filtered_df, x='state', y=feature_selection, title="Comparison of States")
        figures.append(fig1)

        # Generate a bar chart for the selected states
        fig3 = px.bar(filtered_df, x='state', y=feature_selection, title="Comparison of States")
        figures.append(fig3)
        
        # Create a separate DataFrame for the pie chart with both 'state' and the selected feature(s)
        pie_data = filtered_df[['state'] + feature_selection]
        
        # Generate a pie chart for each selected feature
        for feature in feature_selection:
            figPie = px.pie(pie_data, names='state', values=feature)
            figures.append(figPie)

        
# Display the figures
for fig in figures:
    st.plotly_chart(fig)

#display a map
st.map(states)

