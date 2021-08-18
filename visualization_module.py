"This module write respective functions that generates the visual charts and perform unit testing on each function" 
"""# **VISUALIZATIONS**"""




def plot1(df):
    import pandas as pd
    import matplotlib.pyplot as plt

    """Line graph showing the number of stop and search by force for each force"""
    df['force_ids'].value_counts().to_frame().sample(frac=1).plot(kind='line', figsize=(15,8))
    plt.xlabel('Force')
    plt.ylabel('Count')
    plt.title('Line graph showing the number of stop and search by force for each force')
    plt.show()
    

      

      

    """Gender distribution visualization using countplot"""
def plot2(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(15,8))
    import seaborn as sns
    sns.countplot(x=df['gender'])
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.title('Gender distribution visualization using countplot')
    plt.show()
  

      
def plot3(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    """Age range distribution visualization using Countplot"""
    
    fig, ax = plt.subplots(figsize=(15,8))
    import seaborn as sns
    sns.countplot(x=df['age_range'])
    plt.xlabel('Age-range')
    plt.ylabel('Count')
    plt.title('Age range distribution visualization using Countplot')
    plt.show()
  
      


def plot4(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt      
    
    """Pie chart showing comparison of outcome_linked_to_object_of_search"""
  
    df['outcome_linked_to_object_of_search'].value_counts().to_frame().plot(kind='pie',autopct='%1.1f%%', y='outcome_linked_to_object_of_search', figsize=(15,8))
    plt.title('Pie chart showing comparison of outcome_linked_to_object_of_search')
    plt.show()
  




def plot5(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt     
    
    """Stacked bar chart showing trend for the "removal_of_more_than_outer_clothing" and 'outcome'"""
  
    df.groupby('removal_of_more_than_outer_clothing')['outcome'].value_counts().to_frame().rename(columns={'outcome':'count'}).\
    reset_index().pivot("removal_of_more_than_outer_clothing", 'outcome',	'count').plot(kind='barh',stacked=True, width=0.5,figsize=(15,8))
    plt.xlabel('Count')
    plt.title('Stacked bar chart showing trend for the "removal_of_more_than_outer_clothing" and "outcome" ')
    plt.show()
  
      



def plot6(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt      
    
    """Stacked bar chart showing trend for the "removal_of_more_than_outer_clothing" and 'object_of_search'"""
  
    df.groupby('removal_of_more_than_outer_clothing')['object_of_search'].value_counts().to_frame().rename(columns={'object_of_search':'count'}).\
    reset_index().pivot("removal_of_more_than_outer_clothing", 'object_of_search',	'count').plot(kind='bar', stacked=True, width=0.3, figsize=(15,8))
    plt.ylabel('Count')
    plt.title('Stacked bar chart showing trend for the "removal_of_more_than_outer_clothing" and "object_of_search" ')
    plt.show()
  



def plot7(df):
    try:
        import pandas as pd
        import matplotlib.pyplot as plt      
        
        """How many teenagers were stopped and searched by Cleveland Police in the month of march 2021"""
      
        df[df['force_ids']=='cleveland'].value_counts('age_range').to_frame().plot(kind='bar', color='black', figsize=(15,8))
        plt.ylabel('Count')
        plt.title('How many teenagers were stopped and searched by Cleveland Police in the month of march 2021')
        plt.show()
    except:
        pass





      
def plot8(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    """Tree maps showing proportion of self_defined_ethnicity"""
    'Some processing on self_defined_ethnicity to extract specific ethnicity names'
    self_defined_ethnicity_extract=list()
    for i in df['self_defined_ethnicity'].values:
      self_defined_ethnicity_extract.append(i[:5])
    df['self_defined_ethnicity_extract']=self_defined_ethnicity_extract
    df['self_defined_ethnicity_extract'].replace('Unkno', 'Unknown', inplace=True)
    import squarify

    # Prepare Data
    df_treemap = df.groupby('self_defined_ethnicity_extract').size().reset_index(name='counts')
    labels = df_treemap.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
    sizes = df_treemap['counts'].values.tolist()
    colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

    # Draw Plot
    plt.figure(figsize=(12,8), dpi= 80)
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
    plt.title('Tree maps showing proportion of self_defined_ethnicity')
    plt.show()




def plot9(df):
    
    import squarify
    import pandas as pd
    import matplotlib.pyplot as plt
    
    """Tree maps showing proportion of officer_defined_ethnicity"""
    df_treemap = df.groupby('officer_defined_ethnicity').size().reset_index(name='counts')
    labels = df_treemap.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
    sizes = df_treemap['counts'].values.tolist()
    colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

    # Draw Plot
    plt.figure(figsize=(12,8), dpi= 80)
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
    plt.title('Tree maps showing proportion of officer_defined_ethnicity')
    plt.show()


def plot10(df):
   
    import pandas as pd
    import matplotlib.pyplot as plt
    
    """Grouped bar chart showing trend of distribution for officer_defined_ethnicity and self_defined_ethnicity"""
    df1=df['officer_defined_ethnicity'].value_counts().to_frame()
    df2=df['self_defined_ethnicity_extract'].value_counts().to_frame()
    df3=pd.concat([df1,df2], axis=1)

  
    df3.plot(kind='bar', figsize=(15,8))
    plt.ylabel('Count')
    plt.xlabel('Ethnicity')
    plt.title('Grouped bar chart showing trend of distribution for officer_defined_ethnicity and self_defined_ethnicity')
    plt.show()
  



      
def plot11(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    """A pie chart to show the proportion of time office officer_defined_ethnicity tallies with the self_defined_ethnicity"""

    Tally=0
    Not_Tally=0


    for a,b in zip(df['officer_defined_ethnicity'].values, df['self_defined_ethnicity_extract'].values):
      if a==b:
        Tally=Tally+1
      else:
        Not_Tally=Not_Tally + 1

    df4=pd.DataFrame({'Tally':[Tally], 'Not_Tally':[Not_Tally]}).transpose().plot(kind='pie',y=0,autopct='%1.1f%%', figsize=(15,8))

    plt.title('pie chart to show the proportion of time office officer_defined_ethnicity tallies with the self_defined_ethnicity')
    plt.show()




def plot12(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    """A Grouped bar chart showing distribution of 'Arrest' and 'A no further action disposal' per object_of_search"""

    df5=df.groupby('object_of_search')['outcome'].value_counts().to_frame().rename(columns={'outcome':'count'}).reset_index()
    df5=df5[df5['outcome'].isin(['Arrest', 'A no further action disposal']) ]

  
    df5.pivot("object_of_search", 'outcome',	'count').plot(kind='bar', figsize=(15,8))
    plt.ylabel('Count')
    plt.title('Grouped bar chart showing distribution of "Arrest" and "A no further action disposal" per object_of_search')
    plt.show()
  



      
def plot13(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    """Top 5 locations with highest search record?"""
  
    df['location'].value_counts().to_frame().drop('None').head(5).sample(frac=1).plot(kind='bar', figsize=(15,8))
    plt.ylabel('Count')
    plt.xlabel('Location')
    plt.title('Top 5 locations with highest search record?')
    plt.show()
  


def plot14(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt      
    
    """Top 5 locations with highest arrest made?"""

    df_h=df.groupby('location')['outcome'].value_counts().to_frame().rename(columns={'outcome':'count'}).reset_index()
    df_h=df_h[df_h['outcome']=='Arrest']
    dfh=df_h.sort_values('count', ascending=False).drop(1).head(5).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(15,8))

    # Draw the stem and circle
    ax.stem(dfh['location'],dfh['count'], basefmt=' ')

    # Start the graph at 0
    ax.set_ylim(0, 200)

    plt.ylabel('Count')
    plt.xlabel('Location')
    plt.title('Top 5 locations with highest arrest made?')
    plt.show()




  
def plot15(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    """Donut chart showing proportion of search types"""
    
    df_t=df['type_'].value_counts().to_frame().reset_index()
    colors= ['#FF0000', '#0000FF', '#FFFF00']
    labels=['Person search','Person and Vehicle search','Vehicle search']
    # Pie Chart
    df_t['type_'].plot(kind='pie', colors=colors,labels=labels, autopct='%1.1f%%', pctdistance=0.85,figsize=(15,8))
      
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
      
    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)
    plt.title('Donut chart showing proportion of search types')
    plt.show()





def plot16(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    """Area graph showing number of arrests and no further action disposal by the hour"""
    dfh=df.groupby('Hour')['outcome'].value_counts().to_frame().rename(columns={'outcome':'count'}).reset_index()
    dfh=dfh[dfh['outcome'].isin(['Arrest', 'A no further action disposal']) ]

 
    dfh.pivot('Hour', 'outcome', 'count').plot(kind='area', figsize=(15,8))
    plt.ylabel('Count')
    plt.title('Area graph showing number of arrests and no further action disposal by the hour')
    plt.show()
  




      
def plot17(df):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    """Propotion of legislation power used for search"""
    df_waffle=df['legislation'].value_counts().to_frame()
    df_waffle['perc']=(df_waffle['legislation']/df_waffle['legislation'].sum()) * 100
    df_waffle.reset_index(inplace=True)
    df_waffle.rename(columns={'index': 'legislation_act'}, inplace=True)
    df_waffle.drop([4,5,6,7,8,9,10], inplace=True)
    from pywaffle import Waffle
    

      # To plot the waffle Chart
    fig = plt.figure(
        FigureClass = Waffle,
        rows = 5,
        title={'label': 'Propotion of legislation power used for search', 'loc': 'left'},
        values = df_waffle.perc,
        labels = ['{} {:.1f}%'.format(k, v) for k, v in zip(df_waffle.legislation_act,df_waffle.perc)], 
        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(df_waffle.perc),'fontsize': 12, 'framealpha': 0},
        figsize=(20,12)
    )
