# import os
from cudatext import *
from cudax_lib import get_translation

_   = get_translation(__file__)  # I18N

class Command:
    
    def run(self):
#        msg_box(s, MB_OK)
#        CudaText API - Free Pascal wiki
#https://wiki.freepascal.org/CudaText_API
#--
#ed_handles
#
#ed_handles()
#
#Returns range object: it contains int handles of all editor tabs. Pass each handle to Editor() to make editor object from handle.
#
#Example code, which shows filenames of all tabs:

    #show all file names in console
        print("Tab list:")
        print("=====================================================================:")
        for h in ed_handles():
            e = Editor(h)
            print(e.get_filename()) 
        print("=====================================================================:")



