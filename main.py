from utils.data_process import  text_to_data, data_to_fmt
from utils.get_all_pdf import get_all_file_paths
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
print(raw_data:=text_to_data(scan_txt[0],'Chilquinta'))
print(fmt_data:=data_to_fmt(raw_data,'Chilquinta'))
