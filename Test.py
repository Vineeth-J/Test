import os
import argparse
import glob
import pandas as pd

rootDirectory = os.getcwd()
toolingPath="Tooling/Apps"
srecPath=f"{toolingPath}/Tool.SRECGenerator"
alfaPath=f"{srecPath}/ALFA"
masaPath=f"{srecPath}/MASA"
alfa965Path=f"{srecPath}/ALFA965"

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))



csvFileSearch = glob.glob((f'{alfaPath}/*.csv'))
  

  
for file in csvFileSearch:
	data_frame = pd.DataFrame()
	content = []
	for filename in csvFileSearch:
		df = pd.read_csv(filename, index_col=None, sep=';')
		var=df.iloc[14][4]
		
	
		df.iloc[14][4]=df.iloc[14][4].replace('RCAR3_Calib', 'RCAR3_Calib_China')



		df.to_csv(filename, index=False)
		
		print('success')
	exit()



   
		

    
    
    
        
