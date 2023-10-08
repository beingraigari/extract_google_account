

import glob
import shutil
import os
import time

program_start = time.time()

try:

    src_dir = "C:\GExports"
    dst_dir = "C:\GExtracts_JSON"
    for docfile in glob.iglob(os.path.join(src_dir, "**\*.json"), recursive=True):
        # print({jpgfile})
        shutil.copy(docfile, dst_dir)

except:
    print("We got an error")

program_end = time.time()

print("Time taken to execute this program :", (program_end-program_start) * 10**3, "ms")