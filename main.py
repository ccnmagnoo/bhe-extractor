from utils.get_all_pdf import get_all_pdf
from utils.text_process import process_files

#working directory
SOURCE = "../../../crcam/OneDrive - Ministerio de Energia/Proyectos Públicos/PV Museo HN Valparaíso/consumos"
TARGET = SOURCE+'/'+'content'
# source = "../../../crcam/Downloads/mhnv"


scan_files = get_all_pdf(source=SOURCE)

process_files(output_subfolder=TARGET,files=scan_files)

# content = pdf_to_text(source_path=filename.path)
# text_to_file(output_filepath=SOURCE+'/'+TARGET+'/'+filename.name+'.txt',content=content)
