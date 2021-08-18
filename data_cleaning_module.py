"This module cleans the extracted dataset and put it in shape for visualizations"
"""# **DATA CLEANING**"""
def data_cleaning(df):
    import pandas as pd
    'Extract  hour from dataframe'
    
    df['datetime']= pd.to_datetime(df['datetime'])
    df['Hour']=df['datetime'].dt.hour
    df.drop('datetime', axis=1, inplace=True)

    'Extract the streets names from location column'

    streets=list()
    for i in df['location'].values:
        try:
            streets.append(i['street']['name'])
        except:
            streets.append('None')
    
    df['location']=streets

    'Drop operation_name column due to lots of missing values and fill all missing/absent values as unknown'
    df=df.drop('operation_name', axis=1)
    global df_clean
    df=df.fillna('Unknown')
    df_clean=df


