from os import DirEntry, scandir # lint: disable
import re

filetype_pattern=re.compile(r'^.\w{3}$')


def get_all_file_paths(source:str,filetype:str)->list[DirEntry[str]]:
    "get all pdf files from a certain directory"
    list_of_files:list[DirEntry[str]]= list(scandir(source))

    filter_callable = _gen_is_filetype(filetype)

    filtered:list[DirEntry[str]] = list(filter(filter_callable,list_of_files))
    print('found', len(filtered),'PDF file(s)' )
    return filtered

def _gen_is_filetype(filetype:str):
    if filetype_pattern.search(filetype) is None:
        raise ValueError("filetype has to have '.abc' format")

    return lambda entry: entry.name.endswith(filetype)