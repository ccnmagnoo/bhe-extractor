from utils.data_process import  process_txt_files
from utils.data_storage import data_to_excel
from utils.get_all_pdf import get_all_file_paths
from pprint import pp

from utils.text_process import process_pdf_files
#working directory
SOURCE = "../../../crcam/Downloads/puchuncaví"
TARGET = SOURCE+'/'+'content'
# source = "../../../crcam/Downloads/mhnv"

#get source files paths
scan_files = get_all_file_paths(source=SOURCE,filetype='.pdf')

#extract text from source to target folder
process_pdf_files(output_subfolder=TARGET,files=scan_files)

#fetch text files
content_files = get_all_file_paths(TARGET,'.txt')

#extract data from files
data = process_txt_files(model='Chilquinta_2',files=content_files)

#to file
data_to_excel(data,TARGET)