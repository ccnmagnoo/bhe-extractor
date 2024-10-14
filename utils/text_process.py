import PyPDF2 as pypdf

def text_extract(*,filepath:str)->str:
    "given a filename return text"
    with open(filepath,'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ''

        for page in reader.pages:
            text += page.extract_text()
        print('extracted from:',filepath)
        return text
    
def text_to_file(*,filepath:str,content:str):
    "store given text"
    with open (filepath+'.txt','w',encoding='utf-8') as doc:
        doc.write(content)
        doc.close()
        print('stored text:',filepath)