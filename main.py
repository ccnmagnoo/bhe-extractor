import os

from utils.get_all_pdf import get_all_pdf
from utils.text_process import pdf_to_text, process_files, text_to_file

#working directory
SOURCE = "../../../crcam/OneDrive - Ministerio de Energia/Proyectos Públicos/PV Museo HN Valparaíso/consumos"
TARGET = 'content'
# source = "../../../crcam/Downloads/mhnv"


scan_files = get_all_pdf(source=SOURCE)

process_files(output_subfolder=SOURCE+'/'+TARGET,files=[scan_files[0],scan_files[1]])

# content = pdf_to_text(source_path=filename.path)
# text_to_file(output_filepath=SOURCE+'/'+TARGET+'/'+filename.name+'.txt',content=content)
