import csv
import numpy as np

def getDataSource(data_path):
    Size_of_tv=[]
    Marks_In_Percantage=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
        correaltion.append(float(row["\tcorrealtion"]))
    return{"x":Size_of_tv,"y":Average_time_spent}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation is ",correlation[0,1])

def setup():
    data_path="correaltion.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()    