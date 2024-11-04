from dataclasses import fields
from datetime import datetime
from os import DirEntry
from re import Pattern
from typing import Callable
from libs.manager import CONTEXT
from models.DataPattern import Invoice, InvoiceAdapter
from libs.manager import Provider


def process_content_files(source:list[DirEntry[str]],pattern_model):
    pass

type Raw = InvoiceAdapter[list[str],list[tuple[str]]]

def text_to_data(file:DirEntry[str],model:Provider)->Raw:
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

    raw_data:InvoiceAdapter[list[str],list[tuple[str]]] = InvoiceAdapter(**container)


    return raw_data

def data_to_fmt(raw_data:Raw,model:Provider)->Invoice:
    """Raw str Invoice Data to Invoice Object with proper type"""
    transformer: InvoiceAdapter[Callable,Callable[[tuple,str],datetime]] = CONTEXT[model]['transformer']

    container:dict = {}

    for field in fields(raw_data):
        raw_param = getattr(raw_data,field.name)
        convert_fun  = getattr(transformer,field.name)

        fmt_param = convert_fun(raw_param)

        container[field.name] = fmt_param

    return Invoice(**container)