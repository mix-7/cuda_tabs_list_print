Плагин создан для формирования списка фафлов открытых вкладок в консоли.
сделан по примеру из
CudaText API - Free Pascal wiki
https://wiki.freepascal.org/CudaText_API
--
ed_handles

ed_handles()

Returns range object: it contains int handles of all editor tabs. Pass each handle to Editor() to make editor object from handle.

Example code, which shows filenames of all tabs:

    #show all file names in console
    for h in ed_handles():
        e = Editor(h)
        print(e.get_filename())
 
Author: mix-7, https://github.com/mix-7
License: MIT


