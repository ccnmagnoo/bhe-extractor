from os import DirEntry
from models.DataPattern import PatternModel,chilquinta


def process_content_files(source:list[DirEntry[str]],pattern_model:PatternModel):
    return None

def text_to_data(file:DirEntry[str],patter_model:PatternModel):
    "extract data from txt file"
    print('processing string content in:',file)


    with open(file,'rb') as f:
        content = str(f.read(),encoding='ansi')
        print('file:',file.name)
        
        for key,compiler in patter_model.items():
            result = compiler.findall(content)
            print('result for',key,'is',result)
        f.close()


    return None
