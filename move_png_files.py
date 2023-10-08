

import glob
import shutil
import os
import time

program_start = time.time()

try:

    src_dir = "C:\GExports"
    dst_dir = "C:\GExtracts_PNG"
    for pngfile in glob.iglob(os.path.join(src_dir, "\**\*.png"), recursive=True):
        # print({jpgfile})
        shutil.copy(pngfile, dst_dir)

except:
    print("We got an error")

program_end = time.time()

print("Time taken to execute this program :", (program_end-program_start) * 10**3, "ms")