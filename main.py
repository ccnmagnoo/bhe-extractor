from utils.data_process import  process_content_files
from utils.get_all_pdf import get_all_file_paths
#working directory
SOURCE = "../../../crcam/OneDrive - Ministerio de Energia/Proyectos Públicos/PV Museo HN Valparaíso/consumos"
TARGET = SOURCE+'/'+'content'
# source = "../../../crcam/Downloads/mhnv"

#get files paths
#scan_files = get_all_file_paths(source=SOURCE,filetype='.pdf')

#extract text
#process_pdf_files(output_subfolder=TARGET,files=scan_files)

#extract files
scan_txt = get_all_file_paths(TARGET,'.txt')

#extract data from files
res = process_content_files(output_folder=TARGET,model='Chilquinta',files=scan_txt)
print(res[23])