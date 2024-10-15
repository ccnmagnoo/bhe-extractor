import os
import PyPDF2 as pypdf

def pdf_to_text(*,source_path:str)->str:
    "given a filename return text"
    with open(source_path,'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ''

        if len(reader.pages)<=0:
            raise ValueError("is not a pdf")

        for page in reader.pages:
            text += page.extract_text()
        print('extracted from:',source_path)
        return text

def text_to_file(*,output_filepath:str,content:str):
    "store given text"

    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

    with open (output_filepath,'w',encoding=None) as doc:
        doc.write(content)
        doc.close()
        print('stored text:',output_filepath)

def process_pdf_files(output_subfolder:str,files:tuple[os.DirEntry[str]]):
    print(len(files),"PDF(s) file(s) ready to process")

    for file in files:
        content = pdf_to_text(source_path=file.path)
        text_to_file(output_filepath=output_subfolder+'/'+file.name+'.txt',content=content)

    print(len(files),"PDF(s) file(s) processed")
    return None