import pandas as pd
print("Hello User")
print ('========================================================')
print ("This program extracts/scrap stop and search by force data via API and performs visualization tasks on the dataset")
print ('========================================================')
print('Program is currently fetching the dataset from the uk police database, kindly await while the fetch completes; This may take up to 30 minutes')
print ('========================================================')
print('Also note that internet connection is highly needed for this process, Please keep your internet connection on')
print ('========================================================')
import data_scraping_via_api_module
data_scraping_via_api_module.data_extraction()
df=data_scraping_via_api_module.df
print ('Downloaded extracted Dataset for consequent use, check the root file')
df.to_csv('data.csv')
print ("Data fetching completed, now cleaning the data")
import data_cleaning_module
data_cleaning_module.data_cleaning(df)

print ("Data cleaning completed, Visual charts coming up")
print ('========================================================')
print ("The produced visual Charts will open in a new matplotlib window, Note that you have to CLOSE each figure generated to open the NEXT: ")
df_viz=data_cleaning_module.df_clean
import visualization_module
visualization_module.plot1(df_viz)
visualization_module.plot2(df_viz)
visualization_module.plot3(df_viz)
visualization_module.plot4(df_viz)
visualization_module.plot5(df_viz)
visualization_module.plot6(df_viz)
visualization_module.plot7(df_viz)
visualization_module.plot8(df_viz)
visualization_module.plot9(df_viz)
visualization_module.plot10(df_viz)
visualization_module.plot11(df_viz)
visualization_module.plot12(df_viz)
visualization_module.plot13(df_viz)
visualization_module.plot14(df_viz)
visualization_module.plot15(df_viz)
visualization_module.plot16(df_viz)
visualization_module.plot17(df_viz)



