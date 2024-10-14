import os

from utils.text_process import text_extract, text_to_file
# source = "../../../crcam/OneDrive - Ministerio de Energia/Proyectos Públicos🏥/PV Museo HN Valparaíso/consumos"
source = "../../../crcam/Downloads/mhnv"


scan = os.scandir(path=source)
filename = list(scan)[0]
filepath = source+'/'+filename.name
print('filename',source+'/'+filename.name)

content = text_extract(filepath=filepath)
text_to_file(filepath=filepath,content=content)