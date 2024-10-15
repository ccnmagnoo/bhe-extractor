from os import DirEntry, scandir

def get_all_pdf(source:str)->list[DirEntry[str]]:
    "get all pdf files from a certain directory"
    list_of_files = list(scandir(source))
    filtered = list(filter(_is_pdf,list_of_files)) 
    print('found', len(filtered),'PDF file(s)' )
    return filtered

def _is_pdf(entry:DirEntry[str]):
    return entry.name.endswith('.pdf')