from dataclasses import fields
from os import DirEntry
from re import Pattern
from models.DataPattern import InvoicePattern, PatternModel,chilquinta


def process_content_files(source:list[DirEntry[str]],pattern_model:PatternModel):
    return None

def text_to_data(file:DirEntry[str],patter_model:InvoicePattern):
    "extract data from txt file"
    print('processing string content in:',file)


    with open(file,'rb') as f:
        
        content = str(f.read(),encoding='ansi')
        print('file:',file.name)
        
        for field in fields(patter_model):
            key:str = field.name
            compiler:Pattern[str] = getattr(patter_model,key)
            result = compiler.findall(content)
            print('result for',key,'is',result)
        f.close()


    return None
