from utils.data_process import  text_to_data
from utils.get_all_pdf import get_all_file_paths
from utils.text_process import process_pdf_files
from models.DataPattern import chilquinta
#working directory
SOURCE = "../../../crcam/OneDrive - Ministerio de Energia/Proyectos Públicos/PV Museo HN Valparaíso/consumos"
TARGET = SOURCE+'/'+'content'
# source = "../../../crcam/Downloads/mhnv"

#get files paths
#scan_files = get_all_file_paths(source=SOURCE,filetype='.pdf')

#extract text
#process_pdf_files(output_subfolder=TARGET,files=scan_files)

#extract data
scan_txt = get_all_file_paths(TARGET,'.txt')
print(scan_txt[0])
text_to_data(scan_txt[0],chilquinta)

# content = pdf_to_text(source_path=filename.path)
# text_to_file(output_filepath=SOURCE+'/'+TARGET+'/'+filename.name+'.txt',content=content)
