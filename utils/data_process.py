from dataclasses import fields
from os import DirEntry
from re import Pattern
from models.DataPattern import InvoicePattern


def process_content_files(source:list[DirEntry[str]],pattern_model):
    pass

def text_to_data(file:DirEntry[str],patter_model:InvoicePattern):
    "extract data from txt file"
    print('processing string content in:',file)


    with open(file,'rb') as txt_file:

        content = str(txt_file.read(),encoding='ansi')
        print('reading:',file.name)

        for field in fields(patter_model):
            compiler:Pattern[str] = getattr(patter_model,field.name)
            result = compiler.findall(content)

            print('result for',field.name,'is',result)

        txt_file.close()

    return None
