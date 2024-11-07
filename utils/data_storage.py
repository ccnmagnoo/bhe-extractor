import pandas as pd
from pandas import DataFrame
from models.DataPattern import Invoice


def data_to_excel(data:list[Invoice],output_folder:str)->None:
    """export data to file"""
    data:DataFrame = pd.DataFrame(data=data,index=None)
    data[['desde','hasta']] = pd.DataFrame(data['period'].tolist(),index = data.index)
    data.drop(columns=['period'])
    
    data.to_csv(f'{output_folder}/export.csv',sep=';')
    
    print('data export to: ',f'{output_folder}/export.csv')
    