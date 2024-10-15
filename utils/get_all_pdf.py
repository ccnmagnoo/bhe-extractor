from os import DirEntry, scandir

def get_all_file_paths(source:str,filetype:str)->list[DirEntry[str]]:
    "get all pdf files from a certain directory"
    list_of_files = list(scandir(source))
    
    filter_callable = _gen_is_filetype(filetype)
    
    filtered = list(filter(filter_callable,list_of_files)) 
    print('found', len(filtered),'PDF file(s)' )
    return filtered

def _gen_is_filetype(filetype:str):
        return lambda entry: entry.name.endswith(filetype)