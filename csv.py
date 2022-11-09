import os
import argparse
import glob

rootDirectory = os.getcwd()
toolingPath="Tooling/Apps"
srecPath=f"{toolingPath}/Tool.SRECGenerator"
alfaPath=f"{srecPath}/ALFA"
masaPath=f"{srecPath}/MASA"
alfa965Path=f"{srecPath}/ALFA965"

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

csvFileSearch = glob.glob((f'{alfaPath}/*.csv'))
# reading the CSV file


for file in csvFileSearch:
    if file.endswith ('.csv'):
        text = open(file, "r")
        text = ''.join([i for i in text]) 
        text = text.replace("RCAR3_Calib", "RCAR3_Calib_China") 
        x = open(file,"w")
        x.writelines(text)
        x.close()

print('success')




  




