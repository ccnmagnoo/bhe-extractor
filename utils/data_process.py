from dataclasses import fields
from os import DirEntry
from re import Pattern
from libs.manager import CONTEXT
from models.DataPattern import InvoiceAdapter
from libs.manager import Provider


def process_content_files(source:list[DirEntry[str]],pattern_model):
    pass

def text_to_data(file:DirEntry[str],model:Provider):
    "extract data from txt file"
    print('processing string content in:',file)

    container:dict[str,list] = {}

    with open(file,'rb') as txt_file:

        content = str(txt_file.read(),encoding='ansi')
        print('reading:',file.name)
        
        invoice_model: InvoiceAdapter[Pattern] = CONTEXT[model]['pattern']

        for field in fields(invoice_model):
            # loop in invoice patter for regex compiler tool
            compiler:Pattern[str] = getattr(invoice_model,field.name)
            result = compiler.findall(content)
            
            print('result for',field.name,'is',result)
            
            container[field.name] = result

        txt_file.close()
        

    return container

def data_to_fmt(data:dict[[str],str],model:Provider):
    pass