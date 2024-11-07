from models.DataPattern import Invoice
import pandas as pd
from pandas import DataFrame

def data_to_excel(data:list[Invoice],output_folder:str)->None:
    data:DataFrame = pd.DataFrame(data=data,index=None)
    data.to_csv(f'output_folder/export.csv')
    