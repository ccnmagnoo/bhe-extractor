import os

from utils.get_all_pdf import get_all_pdf
from utils.text_process import pdf_to_text, text_to_file
SOURCE = "../../../crcam/OneDrive - Ministerio de Energia/Proyectos Públicos/PV Museo HN Valparaíso/consumos"
TARGET = 'content'
# source = "../../../crcam/Downloads/mhnv"


scan = get_all_pdf(source=SOURCE)
filename = list(scan)[0]



content = pdf_to_text(source_path=SOURCE+'/'+filename.name)
text_to_file(output_filepath=SOURCE+'/'+TARGET+'/'+filename.name+'.txt',content=content)