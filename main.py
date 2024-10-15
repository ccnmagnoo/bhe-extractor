import os

from utils.text_process import pdf_to_text, text_to_file
source = "../../../crcam/OneDrive - Ministerio de Energia/Proyectos Públicos/PV Museo HN Valparaíso/consumos"
target = 'content'
# source = "../../../crcam/Downloads/mhnv"


scan = os.scandir(path=source)
filename = list(scan)[0]
filepath = source+'/'+filename.name


content = pdf_to_text(source_path=filepath)
text_to_file(output_filepath=source+'/'+target+'/'+filename.name+'.txt',content=content)